# Generated by Django 4.0.5 on 2022-07-05 22:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0018_alter_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
