NOM_FITXER_ACCIONS = "menuAccions.txt"
NOM_FITXER_SORTIDA = "estudiants.txt"
MISSATGE_ERROR = "\n\tERROR!\n\tCal que el valor estigui dins de l'interval!\n\tSi us plau, torna a intentar-ho!\n"
MISSATGE_DEMANAR_OPCIO = "\tEntra una de les següents opcions"
MISSATGE_OPCIO_SORTIDA = "0. Sortir."

# Diccionari per emmagatzemar els estudiants
estudiants = {}

# Funció per pintar un títol
def pintaTitol(titolAMostrar):
    print(titolAMostrar)
    subratlla(len(titolAMostrar))

# Funció per subratllar amb asteriscs
def subratlla(midaLinia):
    print("*" * midaLinia)

# Funció per mostrar el menú llegint del fitxer
def mostraMenu():
    pintaTitol("Menú Principal")
    try:
        with open(NOM_FITXER_ACCIONS, "r", encoding="utf-8") as fitxer:
            opcions = fitxer.readlines()
        for i, opcio in enumerate(opcions, start=1):
            print(f"{i}. {opcio.strip()}")
        print(MISSATGE_OPCIO_SORTIDA)
        subratlla(14)
    except FileNotFoundError:
        print("Error: No s'ha trobat el fitxer de menú.")

# Funció per guardar els estudiants al fitxer
def guardarEstudiants():
    with open(NOM_FITXER_SORTIDA, "w", encoding="utf-8") as fitxer:
        for nom, hores in estudiants.items():
            fitxer.write(f"{nom} - {hores} hores\n")

# Funció per carregar estudiants d'un fitxer
def carregarEstudiants():
    try:
        with open(NOM_FITXER_SORTIDA, "r", encoding="utf-8") as fitxer:
            for linia in fitxer:
                nom, hores = linia.strip().split(" - ")
                estudiants[nom] = int(hores.split(" ")[0])
    except FileNotFoundError:
        print("No s'ha trobat el fitxer d'estudiants. Se'n crearà un de nou.")
    except ValueError:
        print("Error en carregar estudiants: Format incorrecte.")

# Funció per afegir un estudiant
def afegirEstudiant():
    nom = input("Introdueix el nom de l'estudiant: ")
    if nom in estudiants:
        print("Aquest estudiant ja està registrat!")
        return
    try:
        hores = int(input("Introdueix el nombre d'hores: "))
        estudiants[nom] = hores
        print("Estudiant afegit correctament!")
    except ValueError:
        print("Si us plau, introdueix un nombre vàlid d'hores.")

# Funció per eliminar un estudiant
def eliminarEstudiant():
    nom = input("Introdueix el nom de l'estudiant a eliminar: ")
    if nom in estudiants:
        del estudiants[nom]
        print("Estudiant eliminat correctament!")
    else:
        print("Aquest estudiant no existeix.")

# Funció per modificar les hores d'un estudiant
def modificarHores():
    nom = input("Introdueix el nom de l'estudiant a modificar: ")
    if nom in estudiants:
        try:
            novesHores = int(input("Introdueix el nou nombre d'hores: "))
            estudiants[nom] = novesHores
            print("Hores modificades correctament!")
        except ValueError:
            print("Si us plau, introdueix un nombre vàlid d'hores.")
    else:
        print("Aquest estudiant no existeix.")

# Funció per mostrar tots els estudiants
def mostrarEstudiants():
    if not estudiants:
        print("No hi ha estudiants registrats.")
        return
    pintaTitol("Llista d'Estudiants")
    for nom, hores in estudiants.items():
        print(f"{nom}: {hores} hores")
    subratlla(20)

if __name__ == "__main__":
    carregarEstudiants()
    while True:
        mostraMenu()
        try:
            opcio = int(input(f"{MISSATGE_DEMANAR_OPCIO} (0..5): "))
            if opcio == 0:
                print("Fins la propera!")
                guardarEstudiants()
                break

            elif opcio == 1:
                afegirEstudiant()
            elif opcio == 2:
                eliminarEstudiant()
            elif opcio == 3:
                modificarHores()
            elif opcio == 4:
                mostrarEstudiants()
            else:
                print(MISSATGE_ERROR)
        except ValueError:
            print(MISSATGE_ERROR)
