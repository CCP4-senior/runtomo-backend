# Generated by Django 4.0.5 on 2022-06-24 03:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_description_event_image_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 3, 1, 50, 846699, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 3, 1, 50, 847054, tzinfo=utc)),
        ),
    ]