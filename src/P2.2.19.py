

def main():
    #Entrada
    #Procesamiento
    num = 0
    lista = ["Primera cosa","Segunda cosa","Tercera cosa"]
    while num != 3:
        try:
            num = int(input(print("Introduce el número correspondiente para seleccionar una opción:\n 1) Comenzar programa \n 2)Imprimir listado \n 3) Finalizar programa")))
        except: ValueError or num != 1 or num != 2 or num != 3
        if num == 1 or num == 2:
            print(lista)
    #Salida
    print("Fin del programa")
if __name__ == '__main__':
    main()