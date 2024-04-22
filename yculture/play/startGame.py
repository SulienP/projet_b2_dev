from play.models import Question, Reponse
import random

class StartGame():
    def __init__(self, player):
        self.get_question_and_response()
    
    def get_question_and_response(self):
        random_questions = []
        response_choice = []
        for _ in range(5):
            value = random.randint(1, 20)  
            question_by_id = Question.objects.get(id=value)
            random_questions.append(question_by_id)
            responses_by_question = Reponse.objects.filter(id_question_id=value)
            response_choice.append(responses_by_question)
        return random_questions, response_choice