# Generated by Django 4.0.5 on 2022-07-02 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='profile',
        ),
    ]
