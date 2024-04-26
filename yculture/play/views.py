from django.shortcuts import redirect, render
        
from play.models import Question, Reponse,MatchMeking
import random

from accounts.models import Player
from play.add_data import data


def play(request):
    current_user = request.user
    if request.method == 'POST':
        selected_answer = request.POST.get('selected_answer')
        print("Selected answer:", selected_answer)


    if current_user.isInGame:
            return redirect('index')
        
    question, response = gamemanager(request)
    return render(request, 'play/play.html', {'question': question, "response": response})
def gamemanager(request):
    current_user = request.user
    
    if not current_user.isInGame:
        print("je passe ici")
        user_id = current_user.id
        player = Player.objects.get(id=user_id)
        player.isInGame = True
        player.save()

        question, response = StartGame.get_question_and_response() 
        return question, response
    
    return None, None

   
#     current_user = request.user
#     user_id = request.session.get('user_id')
#     player = MatchMeking.objects.filter(id_user=user_id).first()
#     print(player)
#     # data()
#     if not player:
#         new_player = MatchMeking.objects.create(id_user=user_id, userRank=1, isInGame=False)
#         new_player.save()
#         StartGame()
#         new_player.delete()
#         question, response = StartGame.get_question_and_response()
#         return question, response
#     else:    
#         return "noPlay"
#  # players = MatchMeking.objects.all()[:2]

#         # if len(players) == 2:
#         #     GA.StartGame(players)
#         #     for player in players:
#         #         player.delete()
        
        
        



class StartGame():
    
    @staticmethod
    def get_question_and_response():
        random_questions = []
        response_choice = []
        for _ in range(5):
            value = random.randint(1, 20)  
            question_by_id = Question.objects.get(id=value)
            random_questions.append(question_by_id)
            responses_by_question = Reponse.objects.filter(id_question_id=value)
            response_choice.append(responses_by_question)
        return random_questions, response_choice
    
    def game(self,player,request):
        self.question , self.reponse = self.get_question_and_response()
        player_id = request.user.id
        
