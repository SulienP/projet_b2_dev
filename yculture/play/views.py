from play.gamemanager import gamemanager
from django.shortcuts import redirect, render

def play(request):
    value = gamemanager(request)
    print(len(value))
    print(value)
    if (len(value) > 1):
        return render(request, 'play/play.html', {'value': value})
    else:
        return redirect('index')