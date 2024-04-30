from django.shortcuts import redirect, render
from play.models import Question, Reponse
import random
from accounts.models import Player
from .data import data

def play(request):
    current_user = request.user
    if current_user.is_authenticated:

        if request.method == 'POST':
            selected_answer = request.POST.get('selected_answer')
            StartGame.game(current_user, selected_answer)
        if current_user.isInGame:
            return redirect('index')
        if current_user.numberGamePlay != 4 :
            question, response = gamemanager(request)
            return render(request, 'play/play.html', {'question': question, "response": response})
        else :
            current_user.numberGamePlay = 0
            current_user.isInGame = False
            current_user.save()
            return redirect('index')
    else:
        question, response = gamemanager(request)
        return render(request, 'play/play.html', {'question': question, "response": response})


def gamemanager(request):
    current_user = request.user
    #data()
    if current_user.is_authenticated:
        current_user.numberGamePlay += 1
        current_user.save()
        if current_user.numberGamePlay == 5:
            current_user.numberGamePlay = 0
            current_user.isInGame = False
            current_user.save()
            print("jepasseicic")
            return redirect('index')
        if not current_user.isInGame:
            user_id = current_user.id
            player, created = Player.objects.get_or_create(id=user_id)
            player.isInGame = True
            player.save()
            question, response = StartGame.get_question_and_response() 
            return question, response
    else:
        question, response = StartGame.get_question_and_response() 
        return question, response



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


def contribution(request):
    if request.method == "POST":
        question_text = request.POST.get("question")
        if not question_text:
            return render(request, 'play/contribution.html', {'error_message': "La question ne peut pas être vide"})

        new_question = Question.objects.create(question=question_text)
        
        correct_answer_index = int(request.POST.get("correct"))

        for i in range(1, 5):
            answer_text = request.POST.get(f"answer{i}")
            if not answer_text:
                return render(request, 'play/contribution.html', {'error_message': f"La réponse {i} ne peut pas être vide"})
            is_correct = i == correct_answer_index
            Reponse.objects.create(id_question=new_question, response=answer_text, isTheResponse=is_correct)

        return render(request, 'play/contribution.html')
    
    else:
        return render(request, 'play/contribution.html')
    