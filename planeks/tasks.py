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

    with open('media/content/{}__{}.csv'.format(pk, date), mode='w') as csv_file:
        
        fieldnames =  list(data.keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        row = dict()
        writer.writeheader()
        for _ in range(10):
            for col in fieldnames:
                row[col] = getattr(Faker(), data[col])()
            writer.writerow(row)
        del row
        gen = GeneratedSchema.objects.get(pk=pk)
        gen.status = True
        print(os.path.join(settings.MEDIA_ROOT,'content/{}__{}.csv'.format(pk, date)))
        gen.csv='/content/{}__{}.csv'.format(pk, date)
        gen.save()
