# Generated by Django 3.1.6 on 2021-02-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0007_schemas_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemas',
            name='fields',
            field=models.JSONField(default={}),
        ),
    ]
