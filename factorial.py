def factorial(numero):
    result = 1
    for i in range(1, int(numero) + 1):
        result *= i
        print(i)
    return result

print('El factorial es {0}'.format(factorial(5)))