

def main():
    #Entrada
    altura = int(input("Introduce la altura del triángulo a dibujar:\n"))
    #Procesamiento
    cont = 0
    lista = []
    while cont < altura:
        lista.append("*")
        lista_unida = ''.join(map(str, lista))
        print(lista_unida)
        cont += 1
    #Salida
if __name__ == '__main__':
    main()