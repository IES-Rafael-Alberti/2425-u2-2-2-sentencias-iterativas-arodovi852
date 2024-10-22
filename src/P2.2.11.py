

def main():
    #Entrada
    palabra = input("Introduce una palabra:\n")
    #Procesamiento
    cont = 1
    lista = list(palabra)
    while (cont - 1) < len(palabra):
        print(lista[len(palabra) - cont])
        cont += 1
    #Salida
if __name__ == '__main__':
    main()