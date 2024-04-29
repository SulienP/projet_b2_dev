from django.shortcuts import redirect, render
from.add_data import data
from play.models import Question, Reponse
import random
from accounts.models import Player
from play.add_data import data

def play(request):
    current_user = request.user
    if request.method == 'POST':
        selected_answer = request.POST.get('selected_answer')
        StartGame.game(current_user, selected_answer)

    if current_user.isInGame:
        return redirect('index')
        
    question, response = gamemanager(request)
    return render(request, 'play/play.html', {'question': question, "response": response})

def gamemanager(request):
    current_user = request.user
    # data()
    if not current_user.isInGame:
        user_id = current_user.id
        player, created = Player.objects.get_or_create(id=user_id)
        player.isInGame = True
        player.save()
        question, response = StartGame.get_question_and_response() 
        return question, response
    else:
        return None, None

class StartGame:
    
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
    
    @staticmethod
    def game(current_player, answer):
        if answer is not None:
            get_response_information = Reponse.objects.get(id=answer)
            print(get_response_information)
            if get_response_information.isTheResponse:
                current_player.point += 5
            else:
                current_player.point -= 5
            if current_player.point < 0:
                current_player.point = 0  
            current_player.save()

        return redirect('index')
    

from play.models import Question
from play.models import Reponse

def contribution(request):
    if request.method == "POST":
        new_question = Question(question=request.POST.get("question"))
        new_question.save()
        
        last_question_id = Question.objects.latest('id').id

        new_answer = Reponse(id_question=last_question_id, response=request.POST.get("answer"), isTheResponse=True)
        new_answer.save()

        return render(request, 'play/contribution.html')
    else:
        return render(request, 'play/contribution.html', {'error_message': "La question ne peut pas être vide"})

    '''
    if request.method == "POST":
        question = request.POST.get("question")
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        login(request, user)
        return redirect('index')
    '''

    return render(request, 'play/contribution.html')
