# Generated by Django 4.0.5 on 2022-07-02 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_age'),
        ('events', '0013_remove_event_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]