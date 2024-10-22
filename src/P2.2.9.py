

def main():
    #Entrada
    contraseña = input("Introduce una contraseña:\n")
    #Procesamiento
    contraseña_2 = None
    while contraseña_2 != contraseña:
        contraseña_2 = input("Introduce de nuevo la contraseña:\n")
        if contraseña_2 != contraseña:
            print("La contraseña no es correcta")
    #Salida
    print("La contraseña es correcta")
if __name__ == '__main__':
    main()