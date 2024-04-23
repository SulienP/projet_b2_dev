from play.gamemanager import gamemanager
from django.shortcuts import render

def play(request):
    value = gamemanager()
    return render(request, 'play/play.html', {'value': value})
