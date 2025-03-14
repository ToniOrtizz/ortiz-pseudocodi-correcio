vNomsPersonatges = []
vClassesPersonatges = []
vNivellsPoderPersonatges = []


def afegirPersonatge(nomRebut, classeRebuda, poderRebut):

    if poderRebut < 0:
        print("ERROR: el nivell de poder es incorrectra ja q no pot ser negatiu.")
        return
    vNomsPersonatges.append(nomRebut)
    vClassesPersonatges.append(classeRebuda)
    vNivellsPoderPersonatges.append(poderRebut)

    print(f"personatje {nomRebut} registrat bee!")
def determinarRangPersonatge(poder):

    if poder <= 100:
        return "NOVATOo"
    elif poder <= 250:
        return "EXPERT"
    elif poder <= 400:
        return "MAESTRO"
    else:
        return "Llegenda"
def mostrarPersonatges():

    if not vNomsPersonatges:
        print("No hi ha personatges registrats.")
        return

    print("\nLlista de personatges:")
    for i in range(len(vNomsPersonatges)):
        nom = vNomsPersonatges[i]
        classe = vClassesPersonatges[i]
        poder = vNivellsPoderPersonatges[i]
        rang = determinarRangPersonatge(poder)
        print(f"Nom: {nom}, Classe: {classe}, Poder: {poder}, Rang: {rang}")


if __name__ == "__main__":
    """
               Funció principal que mostra el menú i gestiona les opcions de l'usuari
               """
    while True:
        print("\n=== Gestió de Personatges d'un Videojoc ===")
        print("1. Afegir un nou personatge")
        print("2. mostrar tots els personatges")
        print("3. Sortir del menu")

        opcio = input("Tria una opció: ")

        if opcio == "1":
            nom = input("Introdueix el nom del personatge: ")
            classe = input("introdueix la classe del personatge: ")
            try:
                poder = int(input("inotrdueix el nivel de poderm del teu personatge: "))
                afegirPersonatge(nom, classe, poder)
            except ValueError:
                print("Error: El nivell de poder ha de ser un número enter.")
        elif opcio == "2":
            mostrarPersonatges()
        elif opcio == "3":
            print("Sortint del programa...")
            break
        else:
            print("Opció no vàlida. Torna a intentar-ho.")







