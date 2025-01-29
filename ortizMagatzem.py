


def afegirProducte(noms, quantitats, preus, nom, quantitat, preu):

    noms.append(nom)
    quantitats.append(quantitat)
    preus.append(preu)


def calcularValorTotal(noms, quantitats, preus):

    valor_total = sum(quantitats[i] * preus[i] for i in range(len(noms)))
    return valor_total



if __name__ == "__main__":
    noms = []
    quantitats = []
    preus = []

    contador = 0

    while True:
        print("\nGestió del Magatzem")
        print("1. Afegir un nou produce")
        print("2. mirar el valor total del magatzem")
        print("3. llista de productes")
        print("4. sortida")

        triaopcio = input("agafa una opció: ")

        if triaopcio == "1":
            nom = input("Nom del producte: ")
            quantitat = int(input("Quantitat : "))
            preu = float(input("Preu : "))
            afegirProducte(noms, quantitats, preus, nom, quantitat, preu)
            print(f"Producte {nom} afegit correctament")

        elif triaopcio == "2":
            valor_total = calcularValorTotal(noms, quantitats, preus)
            print(f"El valor total del magatzem és: {valor_total:.2f}€")

        elif triaopcio == "3":
           while contador < len(noms):
               print(f"{contador + 1}. nom {noms[contador]},preu {preus[contador]},quantitat  {quantitats[contador]}")
               contador += 1

        elif triaopcio == "4":
            print("Sortint del programa. Fins aviat!")
            break

        else:
            print("Opció no vàlida. Si us plau, tria una opció correcta.")


