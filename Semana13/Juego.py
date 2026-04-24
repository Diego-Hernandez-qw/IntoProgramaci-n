# ahoracado
# 1 solicitar la palabra
# 2 validar que no este none
# 3 saber el tama;o de la palabra
# 4 solicitar una letra
# compara la letra con las pabra


def solicitarPalabra():
    palabra = input("ingrese una palabra")
    palabra = palabra.lower()
    return palabra


def ListaACompletar(palabraAcomparar):
    listaACompletar = [None] * len(palabraAcomparar)
    return listaACompletar


def SolicitarLetra():
    letra = input("ngrese una letra")
    letra = letra.lower()
    return letra


## la cantidad el elenentios que tiene un arreglo


# una lista va a tener 0 o muchos elementos
# nuna lista puede tener objertos vacios
