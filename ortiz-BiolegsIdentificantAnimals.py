if __name__ == '__main__':
    posicion = int()
    longitud_vectores = int()
    primera_coleccion = list()
    segunda_coleccion = list()
    comunes = list()
    exclusivos_primera = list()
    exclusivos_segunda = list()

    longitud_vectores = int(input("Entra la longitud dels vectors: "))

    for _ in range(longitud_vectores):
        primera_coleccion.append("")
        segunda_coleccion.append("")

    print("Introdueix els animals per a la primera col·lecció")
    for posicion in range(longitud_vectores):
        primera_coleccion[posicion] = input(f"Animal {posicion + 1} de {longitud_vectores}: ")

    print("Introdueix els animals per a la segona col·lecció")
    for posicion in range(longitud_vectores):
        segunda_coleccion[posicion] = input(f"Animal {posicion + 1} de {longitud_vectores}: ")

    for animal in primera_coleccion:
        if animal in segunda_coleccion:
            comunes.append(animal)
        else:
            exclusivos_primera.append(animal)

    for animal in segunda_coleccion:
        if animal not in primera_coleccion:
            exclusivos_segunda.append(animal)

    print("Especies comunes: ", comunes)
    print("Especies excluisves col·leció 1: ", exclusivos_primera)
    print("Especies excluisves col·leció 2: ", exclusivos_segunda)
