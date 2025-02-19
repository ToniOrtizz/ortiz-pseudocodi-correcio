def comptarLineas():
    if __name__ == '__main__':
        nom_fitxer = "frases.txt"
        comptador_linies = 0
        # Obrim el fitxer en mode lectura ("r")
        with open(nom_fitxer, "r") as fitxer:
            linia = fitxer.readline()
            while (linia):
                comptador_linies += 1
                # Llegim cada línia i la mostrem amb el número corresponent
                linia = fitxer.readline()
            print(f"El fitxer {nom_fitxer} té {comptador_linies} línies.")


# Declaració de constants
NOM_FITXER_MENU_PRINCIPAL = "menuPrincipal.txt"
MISSATGE_ERROR = "\n\tERROR!\n\tCal que el valor estigui dins de l'interval!\n\tSi us plau, torna a intentar-ho!\n"
MISSATGE_DEMANAR_OPCIO = "Entra una de les següents opcions"
MISSATGE_OPCIO_SORTIDA = "0 - Sortir."

"""
Nom: existeixElFitxer
Descripció: Funció inicialitzar totes les llistes
    que es faran servir durant l'aplicació
===== Dades d'entrada =====
@param: [OPCIONAL] nomFitxer de tipus cadena
    És una cadena amb el nom del fitxer que volem
    esbrinar si existeix o no existeix.
    Si no es rep cap valor, el valor per defecte
    és NOM_FITXER_ALUMNES.
===== Dades a tornar =====
@return: existeix de tipus boolea.
    torna True si existeix el fitxer amb nom nomFitxer
    torna False si NO existeix el fitxer amb nom nomFitxer
"""
def existeixElFitxer(nomFitxer):
    existeix = False
    try:
        with open(nomFitxer, "r") as fitxer:
            existeix = True
    except FileNotFoundError:
        print(f"\tERROR! el fitxer {nomFitxer} no existeix!")
    finally:
        return existeix


"""
Nom: inicialitzaVector
Descripció: Funció inicialitzar totes les llistes
    que es faran servir durant l'aplicació
===== Dades d'entrada =====
@param: midaVector de tipus enter
    És la mida inicial que ha de tenir el vector
    un cop estigui inicialitzat.
===== Dades a tornar =====
@return: vectorInicialitzat de tipus list.
    És un vector inicialitzat a la mida que 
    sha rebut amb el paràmetre midaVector.
"""
def inicialitzaVector(midaVector):
    # Definició de variables
    pos = int()
    vectorInicialitzat = list()
    # Inicialització de variables
    pos = 0
    while (pos < midaVector):
        vectorInicialitzat.append("")
        pos += 1
    return vectorInicialitzat

"""
Nom: pintaTitol
Descripció: Funció que mostra el titol que 
    rebrà com a paràmetre
===== Dades d'entrada =====
@param: titolAMostrar de tipus cadena
    És la cadena que cal mostrar
===== Dades a tornar =====
@return: cap, no retorna res, només mostra per 
    consola la cadena rebuda
"""
def pintaTitol(titolAMostrar,caracter="*"):
    print(titolAMostrar)

"""
Nom: subratlla
Descripció: Funció que pinta
    un fila d'asteriscos per consola,
    la mida d'aquesta fila dependrà
    de l'enter que rebi com a paràmetre.
===== Dades d'entrada =====
@param: midaLinia de tipus enter
    És la mida de la fila d'asteriscos a mostrar
@param: [OPCIONAL] caracter de tipus cadena
    És el caracter que cal pintar, 
===== Dades a tornar =====
@return: cap, no retorna res, només mostra per 
    consola la cadena rebuda
"""
def subratlla(midaLinia,caracter="*"):
    print(caracter * midaLinia)

"""
Nom: tornaCadenaDOpcions
Descripció: Funció que retorna una cadena
    amb un seguit de números, que van des 
    del zero fins al número rebut amb el
    paràmetre quantitatOpcions, i que
    estiguin separat amb comes.
===== Dades d'entrada =====
@param: quantitatOpcions tipus enter
    És el número fins al qual ha d'arribar
    la cadena a tornar.
===== Dades a tornar =====
@return: cadenaOpcions de tipus cadena
    cadena que va des del zero, fins al
    número rebut amb el paràmetre quantitatOpcions,
    i que estiguin separat amb comes.
"""
def tornaCadenaDOpcions(quantitatOpcions):
    # Definició de variables
    cadenaOpcions = str()
    pos = int()
    # Inicialització de variables
    cadenaOpcions = "(0,"
    pos = 1
    while (pos <= quantitatOpcions):
        cadenaOpcions += str(pos)
        if (pos < (quantitatOpcions)):
            cadenaOpcions += ","
        else:
            cadenaOpcions += ")"
        pos += 1
    return cadenaOpcions


"""
Nom: mostraMenu
Descripció: Funció que mostra un menú
    amb les opcions a escollir per l'usuari.
    I mostrarà un missatge en cas de que l'usuari
    entri un valor que no es troba dins de les
    possibles opcions.
===== Dades d'entrada =====
@param: nomFitxer de tipus cadena
    Amb el nom a on es troben les opcions
    a mostrar com a menu.
@param: titolMenu de tipus cadena
    Títol que es vol mostrar com a títol
    del menu.
@param: [OPCIONAL] cadenaError de tipus cadena
    Cadena que es mostrarà en cas de que l'usuari
    entri un valor que no es troba dins de les
    possibles opcions.
    Si no es rep cap valor, es prendrà con a valor
    per defecte MISSATGE_ERROR.
===== Dades a tornar ======
@return: cap
    mostra per consola un menú amb les 
    opcions a escollir per l'usuari.
======== Important ========
    Aquesta funció fa servir les funcions
        tornaCadenaDOpcions, pintaTitol i subratlla
"""
def mostraMenu(titolMenu,
               cadenaDemanaOpcions = MISSATGE_DEMANAR_OPCIO,
               cadenaError = MISSATGE_ERROR):
    # Definició de variables
    # Inicialització de variables
    nomFitxer = NOM_FITXER_MENU_PRINCIPAL

    if existeixElFitxer(nomFitxer):
        pintaTitol(titolMenu)
        subratlla(len(titolMenu))
        with open(nomFitxer, "r") as fitxer:
            index = 0
            linia = fitxer.readline()
            while (linia):
                index += 1
                # Llegim cada línia i la mostrem amb el número corresponent
                print(f"{index} - {linia}", end="")
                linia = fitxer.readline()
            print()
            print(MISSATGE_OPCIO_SORTIDA)
            subratlla(len(titolMenu))
            print(f"{cadenaDemanaOpcions} {tornaCadenaDOpcions(index)}: ", end="")
    else:
        print(f"ERROR! No existeix el fitxer {nomFitxer} per poder mostrar el menú!")

"""
Nom: comptaLiniesFitxer
Descripció: Funció que retorna el nombre 
    de línies que conté el fitxer rebut amb el
    paràmetre nomFitxer.
===== Dades d'entrada =====
@param: nomFitxer tipus cadena
    nom del fitxer del qual volem comptar
    les línies que té.
===== Dades a tornar =====
@return: quatitatLinies de tipus enter
    el nombre de línies que conté el fitxer
    rebut amb el paràmetre nomFitxer.
"""
def comptaLiniesFitxer(nomFitxer):
    quatitatLinies = 0
    with open(nomFitxer, "r") as fitxer:
        linia = fitxer.readline()
        while (linia):
            quatitatLinies += 1
            # Llegim cada línia i la mostrem amb el número corresponent
            linia = fitxer.readline()
    return quatitatLinies

"""
Nom: obteOpcionsSegonsFitxer
Descripció: Funció que retorna un vector 
    amb les opcions que calen per un menú.
    Els elements del vector a tornar, és una seqüència
    de nombres que van des del zero fins a la 
    quantitats de línies que té un fitxer.
    Ja que aquest fitxer conté les opcions que 
    volem mostrar al menú.
===== Dades d'entrada =====
    nom del fitxer del qual volem comptar
    les línies que té.
===== Dades a tornar =====
@return: vectorOpcions de tipus vector
    conté laa seqüència de nombres que van des
    del zero fins a la quantitats de línies que té un fitxer.
======== Important ========
    Aquesta funció fa servir la funció
        comptaLiniesFitxer
"""
def obteOpcionsSegonsFitxer(nomFitxer):
    vectorOpcions = list()
    quantitatDOpcions = comptaLiniesFitxer(nomFitxer)
    pos = 0
    vectorOpcions.append(pos)
    mida = quantitatDOpcions
    while(pos <= mida):
        pos += 1
        vectorOpcions.append(pos)
    return vectorOpcions

"""
Nom: tornaOpcioMenu
Descripció: Funció que mostra un menú
    amb les opcions a escollir per l'usuari, i li
    demana a l'usuari que escolli una.
===== Dades d'entrada =====
@param: titolMenu de tipus cadena
    Cadena amb el títol del menú
@param: [OPCIONAL] nomFitxer de tipus cadena
    Cadena que es el nom del fitxer que 
    conté les opcions a mostrar.
    Si no es rep cap valor, es prendrà con a valor
    per defecte NOM_FITXER_ALUMNES.
@param: [OPCIONAL] cadenaError de tipus cadena
    Cadena que es mostrarà en cas de que l'usuari
    entri un valor que no es troba dins de les
    possibles opcions.
    Si no es rep cap valor, es prendrà con a valor
    per defecte MISSATGE_ERROR.
===== Dades a tornar =====
@return: cap
    mostra per consola un menú amb les 
    opcions a escollir per l'usuari.
======== Important ========
    Aquesta funció fa servir les funcions
        obteOpcions, mostraMenu
"""
def tornaOpcioMenu(titolMenu,
        nomFitxer=NOM_FITXER_MENU_PRINCIPAL,
        cadenaError=MISSATGE_ERROR):
    # Definició de variables
    opcionsAEscollir = list()
    opcioLlegida = int()
    # Inicialització de variables