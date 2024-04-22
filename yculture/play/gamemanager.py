import play.startGame as SG

def gamemanager():
    value =""
    players = ["player1", "plaer20"]
    if len(players) <= 5 :
        SG.startGame(players)
        value = "start game"
        return value
    else:
        value =" oneplayer en trop"
        return value
    

