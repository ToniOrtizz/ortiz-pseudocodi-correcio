import os


# Constants
NOM_FITXER_VEHICLES = "flotaVehicles.txt"

# Llistes per emmagatzemar la informació
matricules = []
models = []
anys = []
quilometratges = []
preusPerDia = []

def mostraMenu():
    print("\nMenú Principal")
    print("**************")
    print("1. Afegir un nou vehicle")
    print("2. Esborrar un vehicle existent")
    print("3. Mostrar tots els vehicles que tenim")
    print("4. Calcular les estadístiques dels vehicles")
    print("0. Sortir")
    print("**************")

def carregarDades():
    """Carrega les dades del fitxer en les llistes."""
    if os.path.exists(NOM_FITXER_VEHICLES):
        with open(NOM_FITXER_VEHICLES, "r") as fitxer:
            for linia in fitxer:
                dades = linia.strip().split("#")
                matricules.append(dades[0])
                models.append(dades[1])
                anys.append(int(dades[2]))
                quilometratges.append(int(dades[3]))
                preusPerDia.append(float(dades[4]))

def guardarDades():
    """Guarda les dades de les llistes en el fitxer."""
    with open(NOM_FITXER_VEHICLES, "w") as fitxer:
        for i in range(len(matricules)):
            fitxer.write(f"{matricules[i]}#{models[i]}#{anys[i]}#{quilometratges[i]}#{preusPerDia[i]}\n")

def afegirVehicle():
    """Afegeix un nou vehicle a la llista."""
    matricula = input("Introdueix la matrícula: ")
    if matricula in matricules:
        print("Aquest vehicle ja existeix!")
        return
    model = input("Introdueix el model: ")
    any_fabricacio = int(input("Introdueix l'any de fabricació: "))
    quilometratge = int(input("Introdueix el quilometratge: "))
    preu_per_dia = float(input("Introdueix el preu per dia: "))

    matricules.append(matricula)
    models.append(model)
    anys.append(any_fabricacio)
    quilometratges.append(quilometratge)
    preusPerDia.append(preu_per_dia)
    print("Vehicle afegit correctament!")

def mostrarFlota():
    """Mostra tots els vehicles registrats."""
    if not matricules:
        print("No hi ha vehicles registrats.")
        return
    print("\nLlista de vehicles")
    print("******************")
    for i in range(len(matricules)):
        print(f"{models[i]} ({anys[i]}) - {quilometratges[i]} km - {preusPerDia[i]} €/dia, matrícula {matricules[i]}")
    print("******************")

def calcularEstadistiques():
    """Calcula i mostra estadístiques de la flota."""
    if not matricules:
        print("No hi ha vehicles registrats.")
        return

    max_km_index = quilometratges.index(max(quilometratges))
    min_km_index = quilometratges.index(min(quilometratges))
    max_any_index = anys.index(max(anys))
    min_any_index = anys.index(min(anys))
    max_preu_index = preusPerDia.index(max(preusPerDia))
    min_preu_index = preusPerDia.index(min(preusPerDia))

    preu_mitja = sum(preusPerDia) / len(preusPerDia)

    print("\nEstadístiques de la flota")
    print("*************************")
    print(f"El vehicle amb més quilometratge és el {models[max_km_index]} amb {quilometratges[max_km_index]} km.")
    print(f"El vehicle amb menys quilometratge és el {models[min_km_index]} amb {quilometratges[min_km_index]} km.")
    print(f"El vehicle més antic és el {models[min_any_index]} ({anys[min_any_index]}).")
    print(f"El vehicle més nou és el {models[max_any_index]} ({anys[max_any_index]}).")
    print(f"El preu mitjà de lloguer per dia és de {preu_mitja:.2f} €.")
    print(f"El vehicle més car de llogar és el {models[max_preu_index]} amb {preusPerDia[max_preu_index]} €/dia.")
    print(f"El vehicle més econòmic de llogar és el {models[min_preu_index]} amb {preusPerDia[min_preu_index]} €/dia.")
    print("*************************")

def esborrarVehicle():
    """Esborra un vehicle donada la matrícula."""
    matricula = input("Introdueix la matrícula del vehicle a esborrar: ")
    if matricula in matricules:
        index = matricules.index(matricula)
        del matricules[index]
        del models[index]
        del anys[index]
        del quilometratges[index]
        del preusPerDia[index]
        print("Vehicle esborrat correctament!")
    else:
        print("No s'ha trobat cap vehicle amb aquesta matrícula.")



# Executa el programa si s'executa directament aquest fitxer
if __name__ == "__main__":

        carregarDades()

        while True:
            mostraMenu()
            opcio = input("Escull una opció: ")

            if opcio == "1":
                afegirVehicle()
            elif opcio == "2":
                esborrarVehicle()
            elif opcio == "3":
                mostrarFlota()
            elif opcio == "4":
                calcularEstadistiques()
            elif opcio == "0":
                guardarDades()
                print("Dades guardades. Sortint del programa.")
                break
            else:
                print("Opció no vàlida, torna-ho a intentar.")

