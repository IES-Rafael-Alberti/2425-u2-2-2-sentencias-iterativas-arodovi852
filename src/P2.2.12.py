

def main():
    #Entrada
    palabra = input("Introduce una palabra:\n")
    letra = input("Introduce una letra para buscar en la palabra:\n")
    #Procesamiento
    cont = 0
    lista = list(palabra)
    apariciones = 0
    while cont < len(palabra):
        if lista[cont] == letra:
            apariciones += 1
        cont += 1
    #Salida
    print("La letra aparece %d veces" % (apariciones))
if __name__ == '__main__':
    main()