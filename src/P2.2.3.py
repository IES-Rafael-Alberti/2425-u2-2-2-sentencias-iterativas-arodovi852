

def main():
    #Entrada
    num = int(input("Introduce un número:\n"))
    #Procesamiento
    cont = 1
    lista = []
    posicion_lista = 0
    while cont <= num:
        if cont == num or cont == num - 1:
            lista.insert(posicion_lista, cont)
            cont += 2
            posicion_lista += 1
        else:
            lista.insert(posicion_lista, cont)
            lista.append(",")
            cont += 2
            posicion_lista += 2
    lista_unida = ''.join(map(str, lista))
    #Salida
    print(lista_unida)
if __name__ == '__main__':
    main()