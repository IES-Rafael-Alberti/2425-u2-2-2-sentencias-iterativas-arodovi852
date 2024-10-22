

def main():
    #Entrada
    #Procesamiento
    monto = 1
    suma = 0
    while monto != 0:
        monto = int(input(print("Introduce un monto")))
        if monto >= 0:
            suma += monto
        else: print("Número inválido")
    if suma >= 1000:
        suma = suma*0.9
    #Salida
    print("Total a pagar = ", suma)
if __name__ == '__main__':
    main()