# Generated by Django 3.0.7 on 2020-07-15 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0020_auto_20200715_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='description',
            field=models.TextField(default=models.TextField()),
        ),
        migrations.AlterField(
            model_name='blog',
            name='new_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 15, 14, 22, 16, 943359)),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 7, 15, 14, 22, 16, 940429)),
        ),
        migrations.AlterField(
            model_name='new',
            name='new_date_upload',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 14, 22, 16, 940429)),
        ),
    ]
