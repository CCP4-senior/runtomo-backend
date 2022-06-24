# Generated by Django 4.0.5 on 2022-06-23 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_date_alter_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 21, 49, 24, 722387)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 21, 49, 24, 722387)),
        ),
    ]
