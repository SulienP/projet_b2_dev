from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def index(request):
    if request.user.is_authenticated:
        User = get_user_model()
        current_user = User.objects.get(pk=request.user.pk)
        current_user.isInGame = False
        current_user.save()
    return render(request, 'home/index.html')



def play(request):
    if request.method == 'POST':
        return HttpResponse("La lecture a été lancée!") 
    else:
        return HttpResponse("Erreur: méthode non autorisée.")
