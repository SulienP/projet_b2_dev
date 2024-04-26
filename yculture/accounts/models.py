from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    profil_photo = models.ImageField(upload_to="profil_photo", blank=True, null=True)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name_plural = "Player"
