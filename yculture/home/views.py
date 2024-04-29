from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from home.fill_db import fill_db

from accounts.models import Player

def index(request):
    #fill_db()
    if request.user.is_authenticated:
        User = get_user_model()
        current_user = User.objects.get(pk=request.user.pk)
        current_user.isInGame = False
        current_user.save()
    players_ordered_by_points = Player.objects.all().order_by('-point')

    return render(request, 'home/index.html',{'players': players_ordered_by_points})



def play(request):
    if request.method == 'POST':
        return HttpResponse("La lecture a été lancée!") 
    else:
        return HttpResponse("Erreur: méthode non autorisée.")
