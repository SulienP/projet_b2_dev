from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Reponse(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse = models.CharField(max_length=255)
    vrai_faux = models.BooleanField()

    def __str__(self):
        return self.reponse
