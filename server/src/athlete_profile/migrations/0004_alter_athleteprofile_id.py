# Generated by Django 4.1.2 on 2022-11-01 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('athlete_profile', '0003_alter_athleteprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('51de06aa-798f-4bd2-8f2d-e00f7ce09152'), primary_key=True, serialize=False),
        ),
    ]
