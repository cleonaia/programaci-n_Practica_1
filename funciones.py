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

def _figura_nom(figura):
    noms = {
        ROCK: "Pedra",
        PAPER: "Paper",
        SCISSORS: "Tisores",
        LIZARD: "Llangardaix",
        SPOCK: "Spock"
    }
    return noms.get(figura, "Desconegut")

import random 

if __name__ == "__main__":
    PresentacioJoc()

    nom_jugador = input("Introdueix el teu nom: ")
    random.seed(nom_jugador)

    total_partides = LlegirSenar()

    guanys_necessaris = total_partides // 2 + 1

    guanys_sheldon = 0
    guanys_jugador = 0
    llista_sheldon = []
    llista_jugador = []

    while guanys_sheldon < guanys_necessaris and guanys_jugador < guanys_necessaris:
        sheldon_eleccio = random.randint(1, 5)
    
    MenuRPSLS()

    eleccio_jugador = LlegirNombre(1, 5)

    resultat = JocRPSLS(sheldon_eleccio, eleccio_jugador)

    MissatgeRPSLS(sheldon_eleccio, eleccio_jugador)
    if resultat == 1:
        print("Guanya Sheldon Cooper!!!")
    elif resultat == 2:
        print(f"Guanya {nom_jugador}!!!")
    else:
        pass

    print(f"Marcador -- Sheldon: {guanys_sheldon} | {nom_jugador}: {guanys_jugador}\n")

    if guanys_sheldon > guanys_jugador:
        print("El guanyador és Sheldon")
    else:
        print(f"El guanyador és {nom_jugador}")
    
    sheldon_noms = [_figura_nom(x) for x in llista_sheldon]
    jugador_noms = [_figura_nom(x) for x in llista_jugador]
    print("Figures Sheldon:", sheldon_noms)
    print(f"Figures {nom_jugador}:", jugador_noms)
    




    




