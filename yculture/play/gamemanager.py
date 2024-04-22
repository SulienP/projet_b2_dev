import play.game as GA

def gamemanager():
    value =""
    players = ["player1", "plaer20"]
    if len(players) <= 5 :
        GA.StartGame(players)
        return "allquestion"        
    else:
        value =" oneplayer en trop"
        return value
    

