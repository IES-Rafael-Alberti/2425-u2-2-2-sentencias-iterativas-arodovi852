

def main():
    #Entrada
    num = int(input("Introduce un número:\n"))
    #Procesamiento
    cont = 0
    lista = []
    posicion_lista = 0
    while cont <= num:
        if cont == num:
            lista.insert(posicion_lista, num - cont)
            cont += 1
            posicion_lista += 1
        else:
            lista.insert(posicion_lista, num - cont)
            lista.append(",")
            cont += 1
            posicion_lista += 2
    lista_unida = ''.join(map(str, lista))
    #Salida
    print(lista_unida)
if __name__ == '__main__':
    main()