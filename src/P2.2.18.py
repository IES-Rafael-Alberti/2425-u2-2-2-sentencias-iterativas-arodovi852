

def main():
    #Entrada
    #Procesamiento
    num = 1
    pares = []
    lista = []
    while num != "-1":
        suma = 0
        cont = 0
        num = input(print("Introduce un número. Para terminar de sumar, introduce -1:"))
        if num != "-1":
            num = int(num)
            lista = list(map(int, str(num)))
            while cont < len(lista):
                suma += lista[cont]
                cont += 1
            print("La suma de los dígitos es", suma)
            if num % 2 == 0:
                pares.append(num)
    #Salida
    print("Los pares fueron", pares)
if __name__ == '__main__':
    main()
