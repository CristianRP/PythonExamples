def fibo(num):
    fibonacci = []
    x = 0
    y = 1
    for n in range(num):
        fibonacci.append(x + y)
        aux = x + y
        x = y
        y = aux
    return fibonacci

print(fibo(100))