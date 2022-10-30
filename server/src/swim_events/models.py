from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from swim_meet.models import SwimMeet
from athlete_profile.models import AthleteProfile

# Create your models here.


class SwimEvents(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=100)
    heat = models.IntegerField()
    time = models.DecimalField(max_digits=4, decimal_places=2)
    swim_meet = models.ForeignKey(SwimMeet, on_delete=models.RESTRICT)
    athlete = models.ManyToManyField(
        AthleteProfile, related_name='swimmer_event')
