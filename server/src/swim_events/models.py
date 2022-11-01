from email.policy import default
from django.db import models
import uuid
from swim_meet.models import SwimMeet
from athlete_profile.models import AthleteProfile

# Create your models here.


class SwimEvent(models.Model):
    event = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=100)
    heats = models.IntegerField()
    time = models.DecimalField(max_digits=4, decimal_places=2)
    swim_meet = models.ForeignKey(SwimMeet, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class SwimHeat(models.Model):
    heat_no = models.IntegerField(default=1)
    event = models.ForeignKey(SwimEvent, on_delete=models.RESTRICT)

    def __str__(self):
        return "Heat %s-%s" % (self.heat_no, self.event.name)


class SwimmerEvent(models.Model):
    comp = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    athlete = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(SwimEvent, on_delete=models.CASCADE)
    heat = models.ForeignKey(SwimHeat, on_delete=models.RESTRICT)
    swim_time = models.DecimalField(max_digits=5, decimal_places=4)

    def __str__(self):
        return f'{self.athlete.firstname}-{self.event.name}'
