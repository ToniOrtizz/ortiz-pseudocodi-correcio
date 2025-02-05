def afegir_Estudiat(nomsEstudiants, horesEstudi):
    nom = input("Introdueix el nom de l'estudiant: ")
    hores = -1
    while hores < 0:
        hores = float(input("Introdueix les hores d'estudi setmanals: "))

    index = 0
    while index < len(nomsEstudiants):
        index += 1

    nomsEstudiants += [nom]
    horesEstudi += [hores]


def modificar_Hores(nomsEstudiants, horesEstudi):
    nom = input("Introdueix el nom de l'estudiant a modificar: ")
    index = 0
    trobat = False
    while index < len(nomsEstudiants):

        if nomsEstudiants[index] == nom:
            hores = float(input("Introdueix el nou nombre d'hores: "))
            horesEstudi[index] = hores
            trobat = True
        index += 1
    if not trobat:
        print("Estudiant no existent.")

def mostrar_Estudiants(nomsEstudiants, horesEstudi):
    if len(nomsEstudiants) == 0:
        print("No hi ha estudiants registrats.")
    else:
        print("Llista d'estudiants i hores d'estudi:")
        index = 0
        while index < len(nomsEstudiants):
            print(nomsEstudiants[index], "-", horesEstudi[index], "hores")
            index += 1

def eliminar_Estudiant(nomsEstudiants, horesEstudi):
    nom = input("Introdueix el nom de l'estudiant que vols eliminar: ")
    index = 0
    trobat = False
    while index < len(nomsEstudiants):
        if nomsEstudiants[index] == nom:
            trobat = True
            break
        index += 1
    if trobat:
        while index < len(nomsEstudiants) - 1:
            nomsEstudiants[index] = nomsEstudiants[index + 1]
            horesEstudi[index] = horesEstudi[index + 1]
            index += 1
        nomsEstudiants.pop()
        horesEstudi.pop()
        print("Estudiant eliminat correctament.")
    else:
        print("Estudiant no trobat.")


def calcular_MitjanaHores(horesEstudi):
    if len(horesEstudi) == 0:
        return 0
    suma = 0
    index = 0
    while index < len(horesEstudi):
        suma += horesEstudi[index]
        index += 1
    return suma / len(horesEstudi)



if __name__ == '__main__':


        nomsEstudiants = []
        horesEstudi = []
        while True:
            print("bondia seleciona la opcio mes excitant :")
            print("1. Afegir estudiant")
            print("2. Modificar hores d'estudi")
            print("3. Bworra estudiant")
            print("4. enseña estudiants")
            print("5. Calcular mitjana d'hores d'estudi")
            print("6. Sortir")
            opcio = input("Selecciona una opció: ")
            if opcio == "1":
                afegir_Estudiat(nomsEstudiants, horesEstudi)
            elif opcio == "2":
                modificar_Hores(nomsEstudiants, horesEstudi)
            elif opcio == "3":
                eliminar_Estudiant(nomsEstudiants, horesEstudi)
            elif opcio == "4":
                mostrar_Estudiants(nomsEstudiants, horesEstudi)
            elif opcio == "5":
                print("Mitjana hores:", calcular_MitjanaHores(horesEstudi))
            elif opcio == "6":
                break
            else:
                print("opcio incorrecta,escull un altre opció")