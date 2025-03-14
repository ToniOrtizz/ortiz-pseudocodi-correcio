NOM_FITXER_VEHICLES = "puntuacionsIn.txt"
MISSATGE_ERROR = "\n\tERROR!\n\tCal que el valor estigui dins de l'interval!\n\tSi us plau, torna a intentar-ho!\n"
MISSATGE_DEMANAR_OPCIO = "Entra una de les següents opcions"
MISSATGE_OPCIO_SORTIDA = "0 - Sortir."


# Definició de variables


vPuntuacions=list()






if __name__ == '__main__':

    print(f"Contingut del fitxer '{puntuacionsIn.txt}':")
    print(contingut)

    # Definició de variables
    opcioEscollida = int()
    sortir = bool()
    # Inicialització de variables
    inicialitzaElsVectors()
    quantitatDOpcions = comptaLiniesFitxer(FITXER_MENU)
    cadenaOpcions=ompleCadenaDOpcions()
    ompleOpcionsAEscollir()
    sortir = False

    carregarDades()
    while (sortir != True):
        opcioEscollida = tornaOpcioMenu()
        match(opcioEscollida):
            case 1:
                afegirVehicle()
            case 2:
                esborrarVehicle()
            case 3:
                mostrarFlota()
            case 4:
                calcularEstadistiques()
            case 5:
                modificarDadesVehicle()
            case 0:
                guardarDades()
                print("Fins la propera!")
                sortir = True
            case _:
                print("Funció pendent de desenvolupar!")