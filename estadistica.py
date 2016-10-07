def print_params(params):
    for param in params:
        print(param)

def sum_params(params):
    total = 0
    for param in params:
        total += param
    return total

def average_params(params):
    sum_of_params = sum_params(params)
    average = float(sum_of_params / len(params))
    return average

#para calcular la varianza restamos a cada valor la media
# y los sumamos, luego elevamos al cuadrado y lo dividimos entre 2
def variance_params(params, average):
    count = 0
    for param in params:
        count += (average - float(param)) ** 2
    variance = float(count) / len(params)
    return variance

params = [12, 6, 7, 3, 15, 10, 18, 5]
print("El total de los datos es {0}, la media es {1} y la varianza es {2}"
      .format(sum_params(params), average_params(params), variance_params(params, average_params(params))))