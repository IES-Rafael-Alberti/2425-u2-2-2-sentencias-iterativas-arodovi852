#por terminar
def main():
    #Entrada
    #Procesamiento
    primo = 0
    num = 1
    while num > 0:
        cont = 2
        num = int(input(print("Introduce un número:")))
        if num > 0:
            condicion = True
            while cont < num:
                if num % cont == 0:
                    condicion = False
                cont += 1
            if condicion == True:
                primo += 1
    #Salida
    print("Hubieron %d números primos" % (primo))
if __name__ == '__main__':
    main()