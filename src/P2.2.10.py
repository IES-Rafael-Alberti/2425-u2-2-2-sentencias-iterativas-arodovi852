

def main():
    #Entrada
    num = int(input("Introduce un número para saber si es primo:\n"))
    #Procesamiento
    cont = 2
    primo = True
    while cont < num:
        if num % cont == 0:
            primo = False
        cont += 1
    #Salida
    if primo == True:
        print("El número es primo")
    else: print("El número no es primo")
if __name__ == '__main__':
    main()