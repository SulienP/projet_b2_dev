from play import game as GA
from play.models import MatchMeking


def gamemanager(request):
    current_user = request.user
    username = current_user.username
    user_id = request.session.get('user_id')

    
    # new_match = MatchMeking.objects.create(id_user=current_user, userRank=1, isInGame=False)
    
    
    # new_match.save()

    
    players = MatchMeking.objects.all()[:5]
    print(players[0].id, "player")
    # if len(players) == 5:
    #     GA.StartGame(players)
    #     print("Le jeu a commencé!")
    #     players.delete()
        
    #     return "allquestion"  
    # else:
    #     return "Waiting for more players"  
