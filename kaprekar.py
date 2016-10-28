def kaprekar(numero):
    cuadrado = numero ** 2
    if (cuadrado > 9):
        for i in range(len(str(cuadrado))):
            print(str(cuadrado)[i])
            c = int(str(cuadrado)[0]) + int(str(cuadrado)[1])
        if (c == numero):
            return True
        else:
            return False
    else:
        return False
print(kaprekar(9))