# Generated by Django 4.0.5 on 2022-07-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_participation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
