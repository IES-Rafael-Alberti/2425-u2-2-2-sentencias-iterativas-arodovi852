

def main():
    #Entrada
    cantidad = int(input("Introduce cuánto dinero se va a invertir:\n"))
    interes = int(input("Introduce el interés anual en porcentaje:\n"))
    años = int(input("Introduce los años de la inversión:\n"))
    #Procesamiento
    cont = 0
    while cont < años:
        cantidad *= 1 + interes / 100
        print("El año número %d se obtendrán %d euros" % (cont + 1, cantidad))
        cont += 1
    #Salida
if __name__ == '__main__':
    main()