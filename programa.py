import random

ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

def PresentacioJoc():
    print("Pedra, paper, tisores, llangardaix, Spock és un joc d'atzar ampliació del popular Pedra, paper, tisores. "
    print("Creat per Sam Kass amb Karen Bryla http://www.samkass.com/theories/RPSSL.html. ")
    print("Popularitzat per Sheldon Cooper a la sèrie Big Bang Theory. ")
    print("Es fa servir per solucionar una disputa entre Sheldon i Raj en el capítol The Lizard - Spock Expansion. ")
    print("")
    print("El joc és al millor de N partides on N és un nombre senar ")

def Senar(num):
    return False if num%2 == 0 else (num % 2 != 0)

def LlegirSenar():
    while True:
        num = int(input("Introduir un nombre senar: "))
        if Senar(num):
            return num
        else:
            print("ERROR: El nombre introduït és parell")
    num = int(input("Introduir un nombre senar: "))
    Senar(num)

def MenuRPSLS():
    print("1. Pedra")
    print("2. Paper")
    print("3. Tisores")
    print("4. Llangardaix")
    print("5. Spock")

def LlegirNombre(minim, maxim):
    maxim = 5
    minim = 1
    if minim < maxim:
        entrada = int(input(f"Entra valor entre {minim} i {maxim}: "))
        return entrada
    else:
        print("ERROR: Valor fora de l'interval ")
        LlegirNombre(minim,maxim)
        
def JocRPSLS(player1, player2):
    if player1 == player2:
        return 0  

    guanya = {
        ROCK:[SCISSORS, LIZARD],
        PAPER:[ROCK, SPOCK],
        SCISSORS:[PAPER, LIZARD],
        LIZARD:[SPOCK, PAPER],
        SPOCK:[SCISSORS, ROCK]
    }
    if player2 in guanya[player1]:
        return 1
    else:
        return 2

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

def _figura_nom(x):
    noms = {
        ROCK: "Pedra",
        PAPER: "Paper",
        SCISSORS: "Tisores",
        LIZARD: "Llangardaix",
        SPOCK: "Spock"
    }
    return noms.get(x, "Desconegut")

def main():
    PresentacioJoc()
    player1 = input("Introdueix el teu nom: ")
    random.seed(player1)
    total_partides = LlegirSenar()
    guanys_necessaris = total_partides // 2 + 1
    guanys_sheldon = 0
    guanys_jugador = 0
    llista_sheldon = []
    llista_jugador = []
    opcions = ["Pedra", "Paper", "Tisores", "Llangardaix", "Spock"]
    while guanys_sheldon < guanys_necessaris and guanys_jugador < guanys_necessaris:
        sheldon_choice = random.randint(1, 5)
        MenuRPSLS()
        player_choice = LlegirNombre(1, 5)
        resultat = JocRPSLS(player_choice, sheldon_choice)
        MissatgeRPSLS(player_choice, sheldon_choice)
        llista_sheldon.append(sheldon_choice)
        llista_jugador.append(player_choice)
        figures_sheldon = [opcions[i-1] for i in llista_sheldon]
        figures_jugador = [opcions[i-1] for i in llista_jugador]
        
        if resultat == 2:
            guanys_sheldon += 1
            print("Guanya Sheldon Cooper!!!")
        elif resultat == 1:
            guanys_jugador += 1
            print(f"Guanya {player1}!!!")
        else:
            pass

        print(f"MARCADOR -- Sheldon {guanys_sheldon} {player1} {guanys_jugador}")

    if guanys_sheldon >= guanys_necessaris:
        print("El guanyador és Sheldon")
    else:
        print(f"El guanyador és {player1}")

    print("Figures Sheldon:", figures_sheldon)
    print(f"Figures {player1}:", figures_jugador)
main()
