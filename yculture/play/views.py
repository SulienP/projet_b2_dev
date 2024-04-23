from django.http import HttpResponse
from play.gamemanager import gamemanager

def play(request):
    value = gamemanager()
    return HttpResponse(value)
