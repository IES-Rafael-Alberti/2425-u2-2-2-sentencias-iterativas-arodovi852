

def main():
    #Entrada
    frase = input(print("Introduce una frase"))
    letra = input(print("Introduce una letra"))
    
    #Procesamiento
    cont = 0
    lista = list(frase)
    condicion = False
    while condicion == False and cont < len(frase):
        if lista[cont] == letra:
            condicion = True
        cont += 1
    #Salida
    if condicion == True:
        print("La letra se encontró en la posición", cont)
    else: print("La frase no contenía la letra introducida")
if __name__ == '__main__':
    main()