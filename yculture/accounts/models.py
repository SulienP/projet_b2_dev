from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    isInGame = models.BooleanField(default=False)
    pass

