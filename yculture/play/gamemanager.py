from play import game as GA
from play.models import MatchMeking
from django.shortcuts import redirect

def gamemanager(request):
    current_user = request.user
    user_id = request.session.get('user_id')
    existing_match = MatchMeking.objects.filter(id_user=user_id).first()
    
    if not existing_match:
        new_match = MatchMeking.objects.create(id_user=user_id, userRank=1, isInGame=False)
        new_match.save()
    else:
        players = MatchMeking.objects.all()[:5]

        if len(players) == 2:
            GA.StartGame(players)
            for player in players:
                player.delete()
            return "play"
        else:
            return "noPlay"
    return "noPlay"
