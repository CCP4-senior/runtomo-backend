# Generated by Django 4.0.5 on 2022-06-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0002_rename_wards_ward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='ward_name',
            field=models.CharField(max_length=50),
        ),
    ]
