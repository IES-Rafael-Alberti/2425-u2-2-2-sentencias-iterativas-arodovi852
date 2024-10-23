def main():
    #Entrada
    #Procesamiento
    num = 1
    pares = 0
    impares = 0
    lista = []
    while num != 0:
        cont = 0
        try:
            num = int(input(print("Introduce un número:")))
        except num < 0 or ValueError: print("Introduce valores positivos")
        lista = list(map(int, str(num)))
        while cont < len(lista) and lista[cont] != 0:
            if lista[cont] % 2 == 0:
                pares += 1
            else: impares += 1
            cont += 1
    #Salida
    print("Hubieron %d pares y %d impares" % (pares, impares))
if __name__ == '__main__':
    main()
