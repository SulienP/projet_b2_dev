from play.gamemanager import gamemanager
from django.shortcuts import redirect, render

def play(request):
    return render(request, 'play/play.html')
    '''
    value = gamemanager(request)
    if (value == "play"):
        
        return render(request, 'play/play.html', {'value': value})
    else:
        return redirect('index')
        '''
    