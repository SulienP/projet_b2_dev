from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')


def play(request):
    if request.method == 'POST':
        return HttpResponse("La lecture a été lancée!") 
    else:
        return HttpResponse("Erreur: méthode non autorisée.")
