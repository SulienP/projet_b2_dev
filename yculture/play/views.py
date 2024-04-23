from play.gamemanager import gamemanager
from django.shortcuts import render

def play(request):
    value = gamemanager(request)
    return render(request, 'play/play.html', {'value': value})
