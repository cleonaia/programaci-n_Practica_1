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
    
