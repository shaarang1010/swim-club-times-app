# Generated by Django 4.1.2 on 2022-10-30 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('athlete_profile', '0002_alter_athleteprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('421df7dd-9791-487f-af5b-865b5f6ce91d'), primary_key=True, serialize=False),
        ),
    ]
