from play import game as GA
from play.models import MatchMeking


def gamemanager(request):
    current_user = request.user
    user_id = request.session.get('user_id')

    
    new_match = MatchMeking.objects.create(id_user=user_id, userRank=1, isInGame=False)
    
    
    new_match.save()

    
    players = MatchMeking.objects.all()[:5]
    if len(players) == 5:
        GA.StartGame(players)
        print("Le jeu a commencé!")
        for player in players:
            player.delete()
        
        return "allquestion"  
    else:
        return "Waiting for more players"  
