# Generated by Django 3.1.6 on 2021-02-10 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnschemas',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='schemas.schemas'),
        ),
    ]
