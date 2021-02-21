# Generated by Django 3.1.7 on 2021-02-21 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0015_auto_20210221_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedschema',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='generatedschema',
            name='schemas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas.schemas'),
        ),
    ]
