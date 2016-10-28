lista1 = set([1, 2, 3, 4, 5])
lista2 = set([7, 8])
lista3 = []
def centro(lista1, lista2):
    for i in range(1, len(lista1 | lista2)+2):
        lista3.append(i)
    return set(lista3).symmetric_difference(lista1|lista2)

print("Centro númerico {0}".format(centro(lista1, lista2)))
