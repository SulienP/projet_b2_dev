from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    isInGame = models.BooleanField(default=False)
    point = models.IntegerField(default=0)
    pass

