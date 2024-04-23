import play.game as GA

from play.models import MatchMeking

def gamemanager():
    
    
    
    players = MatchMeking.objects.all()[:5]
     
    if len(players) == 5:
        GA.StartGame(players)
        players.delete()
        return "allquestion"  
    else:
        return "Waiting for more players"
