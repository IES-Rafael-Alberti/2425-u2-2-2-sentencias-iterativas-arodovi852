

def main():
    #Entrada
    #Procesamiento
    num = 1
    mayor = 0
    while num != 0:
       num = int(input(print("Escribe número para determinar un mayor Escribe 0 para terminarlo:")))
       if num > mayor:
          mayor = num
    #Salida
    print("El número mayor es", mayor)
if __name__ == '__main__':
    main()