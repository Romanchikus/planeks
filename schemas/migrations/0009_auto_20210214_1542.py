# Generated by Django 3.1.6 on 2021-02-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0008_auto_20210214_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemas',
            name='fields',
            field=models.JSONField(),
        ),
    ]