

def main():
    #Entrada
    #Procesamiento
    num = 1
    suma = 0
    while num != 0:
       num = int(input(print("Escribe número para ir sumándolos. Escribe 0 para terminar la suma:")))
       suma += num
    #Salida
    print("La suma es", suma)
if __name__ == '__main__':
    main()