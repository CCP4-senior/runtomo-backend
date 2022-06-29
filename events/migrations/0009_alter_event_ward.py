# Generated by Django 4.0.5 on 2022-06-29 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0003_alter_ward_ward_name'),
        ('events', '0008_alter_event_lat_alter_event_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wards.ward'),
        ),
    ]
