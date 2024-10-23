#por terminar
def main():
    #Entrada
    frase = input(print("Introduce un número:"))
    #Procesamiento
    lista = []
    lista = frase.split()
    longitud_mayor = ""
    cont = 0
    while cont < len(lista):
        if len(lista[cont]) > len(longitud_mayor):
            longitud_mayor = lista[cont]
        cont += 1
    palabras = len(lista)
    #Salida
    print("Hubieron %d palabras y la palabra más larga fue %s" % (palabras, longitud_mayor))
if __name__ == '__main__':
    main()