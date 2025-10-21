ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

def MissatgeRPSLS(player1, player2):
    if player1 == player2:
        print("Empat!")
        return

    missatges = {
        (SCISSORS, PAPER): "Scissors cuts Paper",
        (PAPER, ROCK): "Paper covers Rock",
        (ROCK, LIZARD): "Rock crushes Lizard",
        (LIZARD, SPOCK): "Lizard poisons Spock",
        (SPOCK, SCISSORS): "Spock smashes Scissors",
        (SCISSORS, LIZARD): "Scissors decapitates Lizard",
        (LIZARD, PAPER): "Lizard eats Paper",
        (PAPER, SPOCK): "Paper disproves Spock",
        (SPOCK, ROCK): "Spock vaporizes Rock",
        (ROCK, SCISSORS): "Rock crushes Scissors",
    }
    if (player1, player2) in missatges:
        print(missatges[(player1, player2)])
    elif (player2, player1) in missatges:
        print(missatges[(player2, player1)])
    else:
        print("Empat!")


def JocRPSLS(player1, player2):
    if player1 == player2:
        return 0  
    
    guanyadors = {
        ROCK: [SCISSORS, LIZARD],
        PAPER: [ROCK, SPOCK],
        SCISSORS: [PAPER, LIZARD],
        LIZARD: [SPOCK, PAPER],
        SPOCK: [SCISSORS, ROCK],
    }
    
    if player2 in guanyadors[player1]:
        return 1
    else:
        return 2
