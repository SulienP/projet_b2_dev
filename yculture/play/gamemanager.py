import play.startGame as SG

def gamemanager():
    value =""
    players = ["player1", "plaer20"]
    if len(players) <= 5 :
        allquestion = SG.StartGame(players)
        return allquestion
    else:
        value =" oneplayer en trop"
        return value
    

