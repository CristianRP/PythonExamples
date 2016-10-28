from Tools.scripts.treesync import raw_input

lista = ['prueba', 'hola', 'guatemala', 'test']
lista2 = []
def caja_seleccion():
    while True:
        print(lista)
        param = raw_input("Ingresa tu opcion")
        for i in lista:
            if (param.__contains__(i)):
                return lista.index(i)


print(caja_seleccion())