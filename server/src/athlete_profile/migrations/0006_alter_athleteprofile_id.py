# Generated by Django 4.1.2 on 2022-11-01 10:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('athlete_profile', '0005_alter_athleteprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('82d628df-e21a-4f81-9412-f8c8686fd68a'), primary_key=True, serialize=False),
        ),
    ]
