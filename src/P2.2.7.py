

def main():
    #Entrada
    num = int(input("Introduce un número para mostrar su tabla de multiplicar:\n"))
    #Procesamiento
    cont = 1
    while cont <= 10:
        print(num*cont)
        cont += 1
    #Salida
if __name__ == '__main__':
    main()