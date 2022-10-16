from email.policy import default
from random import choices
from django.db import models
import uuid


class AthleteProfile(models.Model):
    RYAN_SQUAD = 'RYA'
    HIGH_PERFORMANCE_SQUAD = 'HGP'
    PERFORMANCE = 'PER'
    FRY_SQUAD = 'FRY'
    DEVELOPMENT_SQUAD = 'DEV'
    HENTSCHEL = 'HEN'
    MASTERS = 'OWM'
    NOVICE = 'NOV'
    SQUAD_OPTIONS_CHOICES = [
        (RYAN_SQUAD, 'Ryan A&B'),
        (HIGH_PERFORMANCE_SQUAD, 'High Performance'),
        (PERFORMANCE, 'Performance'),
        (FRY_SQUAD, 'FRY A&B'),
        (DEVELOPMENT_SQUAD, 'Development'),
        (HENTSCHEL, 'Hentschel'),
        (MASTERS, 'Masters'),
        (NOVICE, 'Novice'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=120)
    squad = models.CharField(
        max_length=3, choices=SQUAD_OPTIONS_CHOICES, default=NOVICE)
    dob = models.DateField()
