vPuntuacions = []

# Llegir dades del fitxer puntuacionsIn.txt
with open("puntuacionsIn.txt", "r") as fitxer_entrada:
    for linia in fitxer_entrada:
        vPuntuacions.append(float(linia.strip()))


print("1. Dades carregades correctament!")

# Mostrar totes les puntuacions guardades
print("2. Les puntuacions registrades son:")
print(", ".join(map(str, vPuntuacions)))

# Calcular la puntuació mínima, màxima i mitjana
suma = 0
min_puntuacio = vPuntuacions[0]
max_puntuacio = vPuntuacions[0]

for puntuacio in vPuntuacions:
    suma += puntuacio
    if puntuacio < min_puntuacio:
        min_puntuacio = puntuacio
    if puntuacio > max_puntuacio:
        max_puntuacio = puntuacio

mitjana_puntuacio = suma / len(vPuntuacions)

# Guardar les dades al fitxer puntuacionsOut.txt
with open("puntuacionsOut.txt", "w") as fitxer_sortida:
    fitxer_sortida.write(f"Puntacio minima: {min_puntuacio}\n")
    fitxer_sortida.write(f"Puntuacio mAxima: {max_puntuacio}\n")
    fitxer_sortida.write(f"Puntuacio mitjana: {round(mitjana_puntuacio, 1)}\n")

print("3. Fitxer amb la puntuació minima, la puntuació maxima i la puntuacio mitjana guardat correctament")
print("Fins a la propera!")














