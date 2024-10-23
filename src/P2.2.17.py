

def main():
    #Entrada
    num = int(input(print("Introduce un número:")))
    #Procesamiento
    lista = list(map(int, str(num)))
    cont = 0
    suma = 0
    while cont < len(lista):
        suma += lista[cont]
        cont += 1
    #Salida
    print("La suma de los dígitos es", suma)
if __name__ == '__main__':
    main()