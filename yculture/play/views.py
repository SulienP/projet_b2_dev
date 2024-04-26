from play.gamemanager import gamemanager
from django.shortcuts import redirect, render
from.add_data import data

def play(request):
    return render(request, 'play/play.html')
    '''
    value = gamemanager(request)
    if (value == "play"):
        
        return render(request, 'play/play.html', {'value': value})
    else:
        return redirect('index')
        '''
    

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
