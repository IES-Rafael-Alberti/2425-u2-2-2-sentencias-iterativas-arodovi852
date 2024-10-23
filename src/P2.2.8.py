

def main():
    #Entrada
    num = int(input("Introduce la altura del triángulo a dibujar:\n"))
    #Procesamiento
    cont = 0
    suma = 1
    lista = []
    while suma <= num:
        lista.insert(0, suma)
        lista_unida = ''.join(map(str, lista))
        print(lista_unida)
        lista.insert(0, " ")
        cont += 1
        suma += 2
    #Salida
if __name__ == '__main__':
    main()