from play import game as GA
from play.models import MatchMeking
from django.shortcuts import redirect
from play.add_data import data

def gamemanager(request):
    current_user = request.user
    user_id = request.session.get('user_id')
    player = MatchMeking.objects.filter(id_user=user_id).first()
    # data()
    if not player:
        new_match = MatchMeking.objects.create(id_user=user_id, userRank=1, isInGame=False)
        new_match.save()
        GA.StartGame()
        player.delete()
        question = GA.get_question_and_response()
        return question
    else:    
        return "noPlay"
 # players = MatchMeking.objects.all()[:2]

        # if len(players) == 2:
        #     GA.StartGame(players)
        #     for player in players:
        #         player.delete()