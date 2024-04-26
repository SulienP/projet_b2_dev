from play.models import Question, Reponse
import random


class StartGame():
            
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
        
