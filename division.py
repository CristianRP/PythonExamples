def dividir(num1, num2):
    if (str(num1).isdigit() and str(num2).isdigit()):
        if (num2 > 0):
            print("Resultado:", num1/num2, "Residuo:", num1%num2)
        else:
            print("El divisor no puede ser cero")
    else:
        print("No se pueden dividir cadenas de texto")

dividir("patito", "pollo")
dividir(13, 0)
dividir(15, 4)