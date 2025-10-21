ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5
def PresentacioJoc():
    print("Pedra, paper, tisores, llangardaix, Spock és un joc d'atzar ampliació del popular Pedra, paper, tisores. Creat per Sam Kass amb Karen Bryla http://www.samkass.com/theories/RPSSL.html. " \
    "Popularitzat per Sheldon Cooper a la sèrie Big Bang Theory. " \
    "Es fa servir per solucionar una disputa entre Sheldon i Raj en el capítol The Lizard - Spock Expansion. " \
    "" \
    "El joc és al millor de N partides on N és un nombre senar ")

def Senar(num):
    return num % 2 == 1 if num != 0 else False

def LlegirSenar():
    while True:
        try:
            num = int(input("Introduir un nombre senar: "))
            if Senar(num):
                return num
            else:
                print("ERROR: El nombre introduït és parell")
        except ValueError:
            print("ERROR: El nombre introduït no és vàlid")

def MenuRPSLS():
    print("Selecciona una opció:")
    print("1. Pedra")
    print("2. Paper")
    print("3. Tisores")
    print("4. Llangardaix")
    print("5. Spock")
    
def LlegirNombre(minim,maxim):
    maxim = 5
    minim = 1

    if minim < maxim:
        print(f"Entra valor entre {maxim} i {minim}")
        return [minim,maxim]
    else:
        print("ERROR: Valor fora de l'interval ")
        LlegirNombre(minim,maxim)

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
PresentacioJoc()
import random
player1 = int(input("Introdueix el teu nom: "))
player2 = int(input("Introdueix el teu nom: "))
random.seed(<player1>)
