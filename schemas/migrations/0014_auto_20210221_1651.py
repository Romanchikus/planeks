# Generated by Django 3.1.7 on 2021-02-21 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0013_auto_20210221_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatedschema',
            old_name='id',
            new_name='shemas',
        ),
    ]
