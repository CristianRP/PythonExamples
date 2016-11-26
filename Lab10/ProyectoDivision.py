def euclides():
    a = int(input("Ingresa el primer número:\n"))
    b = int(input("Ingresa el segundo número:\n"))
    mayor = max(a, b)
    menor = min(a, b)
    while menor != 0:
        x = menor
        menor = mayor % menor
        mayor = x
        try:
            print("{0} = {1} * {2} + {3}".format(x, int(mayor / menor), mayor, menor))
        except ZeroDivisionError:
            print("{0} = 0 * {1} + {2}".format(x, mayor, menor))
    print("EL MCD({0},{1}) = {2}".format(a, b, mayor))


print(euclides())
