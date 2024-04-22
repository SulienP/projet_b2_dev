from django.db import models
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

# class MatchMeking(models.Model):
#     id_user  = models.ForeignKey(User)
#     userRank = models.IntegerField(default= 1)


