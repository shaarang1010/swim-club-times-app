from uuid import uuid4
from django.db import models

# Create your models here.


class SwimMeet(models.Model):
    meet_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255)
