# Generated by Django 4.1.2 on 2022-11-01 10:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('athlete_profile', '0004_alter_athleteprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('260dedf0-3d60-4a77-aa58-864156a0646e'), primary_key=True, serialize=False),
        ),
    ]
