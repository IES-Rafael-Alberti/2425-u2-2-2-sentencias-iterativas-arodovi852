#por terminar
def main():
    #Entrada
    #Procesamiento
    libro = ""
    lista = []
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nums = 0
    linea_completa = 0
    while libro != "*":
        cont = 0
        libro = input(print("Introduce un libro:"))
        print(libro)
        lista = list(libro)
        while cont < len(lista):
            if any((i in lista for i in numeros)):
                nums += 1
            cont += 1
        if libro == "/":
            print("Línea completada. Aparecen %d dígitos" % (nums))
            linea_completa += 1
    #Salida
    print("Se leyeron %d líneas completas" % (linea_completa))
if __name__ == '__main__':
    main()