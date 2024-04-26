from play.gamemanager import gamemanager
from django.shortcuts import redirect, render

def play(request):
    question, response = gamemanager(request)
    if question and response:
        return render(request, 'play/play.html', {'question': question , "response": response})
    else:
        return redirect('index')