from django.http import HttpResponse
from play.gamemanager import gamemanager
def index(request):
    value = gamemanager()
    return HttpResponse(value)

