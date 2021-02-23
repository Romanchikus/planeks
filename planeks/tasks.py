from time import sleep
from planeks.celery import app
import csv
from faker import Faker
from schemas.models import GeneratedSchema
from django.core.files import File
import os
from . import settings

@app.task
def hello_world(title, date, data, iters, pk):

    # print('{}{}.csv'.format(title, date))
    # print(data, '{}{}.csv'.format(title, date))

    with open('media/{}__{}.csv'.format(pk, date), mode='w') as csv_file:
        
        fieldnames =  list(data.keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        row = dict()
        writer.writeheader()
        iters = int(iters)+1
        for _ in range(iters):
            for col in fieldnames:
                if data[col][0] != 'age':
                    row[col] = getattr(Faker(), data[col][0])()
                else:
                    col_min, col_max = data[col][1], data[col][2]
                    try:
                        col_min = int(col_min)
                        if col_min < 0:
                            col_min = 0
                    except (ValueError, TypeError):
                        col_min = 0
                    try:
                        col_max = int(col_max)
                        if col_max < 0:
                            col_max = 100
                    except (ValueError, TypeError):
                        col_max = 100

                    row[col] = Faker().random_int(min=col_min, max=col_max)

            writer.writerow(row)
        del row
        gen = GeneratedSchema.objects.get(pk=pk)
        gen.status = True
        gen.csv='/{}__{}.csv'.format(pk, date)
        gen.save()
