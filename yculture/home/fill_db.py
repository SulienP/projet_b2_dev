from play.models import Question
from play.models import Reponse

def fill_db():
    questions = [
        "Quelle est la capitale de la France ?",
        "Qui a peint 'La Nuit étoilée' ?",
        "Combien de planètes composent notre système solaire ?",
        "Quel est l'organe principal du système respiratoire humain ?",
        "Qui a écrit 'Le Petit Prince' ?",
        "Combien de côtés a un hexagone ?",
        "Quel est le symbole chimique de l'oxygène ?",
        "Quel est l'océan le plus grand du monde ?",
        "Quel est l'organe principal du système digestif humain ?",
        "Quelle est la capitale du Japon ?",
        "Combien de lettres compte le mot 'encyclopédie' ?",
        "Qui a découvert la théorie de la relativité restreinte ?",
        "Quel est le plus grand désert chaud du monde ?",
        "Quelle est la planète la plus proche du soleil ?",
        "Qui a peint 'Les Tournesols' ?",
        "Combien de temps faut-il à la Terre pour effectuer une révolution autour du soleil ?",
        "Quelle est la plus grande île du monde ?",
        "Quel est l'organe principal du système circulatoire humain ?",
        "Qui a écrit 'Les Misérables' ?",
        "Combien de côtés a un pentagone ?",
    ]

    for question in questions:
        new_question = Question(question=question)
        new_question.save()

    reponses = [
        # Réponses pour la question 1
        (1, "Paris", True),
        (1, "Londres", False),
        (1, "Berlin", False),
        (1, "Rome", False),
        # Réponses pour la question 2
        (2, "Vincent van Gogh", False),
        (2, "Pablo Picasso", False),
        (2, "Leonardo da Vinci", True),
        (2, "Claude Monet", False),
        # Réponses pour la question 3
        (3, "8", True),
        (3, "9", False),
        (3, "7", False),
        (3, "6", False),
        # Réponses pour la question 4
        (4, "Les bronches", False),
        (4, "Les poumons", True),
        (4, "Le cerveau", False),
        (4, "Le cœur", False),
        # Réponses pour la question 5
        (5, "Antoine de Saint-Exupéry", True),
        (5, "Victor Hugo", False),
        (5, "Gustave Flaubert", False),
        (5, "Émile Zola", False),
        # Réponses pour la question 6
        (6, "4", False),
        (6, "5", True),
        (6, "6", False),
        (6, "7", False),
        # Réponses pour la question 7
        (7, "O", False),
        (7, "Ox", False),
        (7, "Oxy", False),
        (7, "O2", True),
        # Réponses pour la question 8
        (8, "Pacifique", True),
        (8, "Atlantique", False),
        (8, "Indien", False),
        (8, "Arctique", False),
        # Réponses pour la question 9
        (9, "L'estomac", False),
        (9, "Le foie", False),
        (9, "Le pancréas", False),
        (9, "L'intestin grêle", True),
        # Réponses pour la question 10
        (10, "Tokyo", True),
        (10, "Osaka", False),
        (10, "Kyoto", False),
        (10, "Hiroshima", False),
        # Réponses pour la question 11
        (11, "12", False),
        (11, "13", False),
        (11, "14", False),
        (11, "15", True),
        # Réponses pour la question 12
        (12, "Isaac Newton", False),
        (12, "Albert Einstein", True),
        (12, "Galilée", False),
        (12, "Nicolas Copernic", False),
        # Réponses pour la question 13
        (13, "Le Sahara", False),
        (13, "Le Kalahari", False),
        (13, "Le Gobi", True),
        (13, "L'Atacama", False),
        # Réponses pour la question 14
        (14, "Mercure", True),
        (14, "Vénus", False),
        (14, "Mars", False),
        (14, "Jupiter", False),
        # Réponses pour la question 15
        (15, "Vincent van Gogh", False),
        (15, "Pablo Picasso", False),
        (15, "Claude Monet", True),
        (15, "Édouard Manet", False),
        # Réponses pour la question 16
        (16, "365 jours", False),
        (16, "366 jours", True),
        (16, "364 jours", False),
        (16, "363 jours", False),
        # Réponses pour la question 17
        (17, "Groenland", True),
        (17, "Australie", False),
        (17, "Madagascar", False),
        (17, "Bornéo", False),
        # Réponses pour la question 18
        (18, "Le cœur", True),
        (18, "Le foie", False),
        (18, "Le pancréas", False),
        (18, "Le rein", False),
        # Réponses pour la question 19
        (19, "Victor Hugo", True),
        (19, "Gustave Flaubert", False),
        (19, "Émile Zola", False),
        (19, "Honoré de Balzac", False),
        # Réponses pour la question 20
        (20, "4", False),
        (20, "5", False),
        (20, "6", True),
        (20, "7", False),
    ]

    for id_question, reponse_text, is_true in reponses:
        question = Question.objects.get(pk=id_question)
        nouvelle_reponse = Reponse(id_question=question, response=reponse_text, isTheResponse=is_true)
        nouvelle_reponse.save()
