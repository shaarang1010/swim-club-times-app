from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from swim_meet import SwimMeet

# Create your models here.


class SwimEvents(models.Model):
    id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(max_length=100)
    heat = models.IntegerField()
    time = models.DecimalField(max_digits=4, decimal_places=2)
    swim_meet = models.ForeignKey(SwimMeet, on_delete=models.RESTRICT)
