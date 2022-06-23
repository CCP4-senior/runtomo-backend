# Generated by Django 4.0.5 on 2022-06-23 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='running_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 16, 43, 49, 172149)),
        ),
    ]
