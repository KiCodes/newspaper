# Generated by Django 3.0.7 on 2020-07-15 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0021_auto_20200715_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='content',
        ),
        migrations.AlterField(
            model_name='blog',
            name='new_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 15, 14, 23, 39, 41015)),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 15, 14, 23, 39, 38085)),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_date_upload',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 14, 23, 39, 38085)),
        ),
    ]
