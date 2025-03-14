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
        return "NOVATO"
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






