from django.db import models
from accounts.models import Player

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question



class Reponse(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=255)
    isTheResponse = models.BooleanField()

    def __str__(self):
        return self.response

# ! décommenter et ajouter taff evan

class MatchMeking(models.Model):
    id_user = models.IntegerField(null=True)
    userRank = models.IntegerField(default= 1)
    isInGame = models.BooleanField(default=False)
