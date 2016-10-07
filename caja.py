from random import randint
import string
import random

def cobro():
    print("Bienviendo al sistema de cobro PythonStore")
    print("Ingresa los articulos por cobrar y escribe 'terminar'\npara finalizar la lista.")
    abarrotes = []
    precios = []
    finalice = True
    while finalice:
        producto = input("Ingresa los abarrotes: ")
        if (producto == "terminar"):
            finalice = False
        else:
            precio = float(input("Ingresa el precio (Q):"))
            abarrotes.append(producto.strip())
            precios.append(precio)
    print(abarrotes)
    print(precios)
    print(total_compra(precios))
    facturacion(abarrotes, precios, total_compra(precios))

def total_compra(precios):
    sum = 0
    for i in range(0,len(precios)):
        sum = sum + precios[i]
    return sum

def facturacion(productos, precios, total):
    print("Ingresa los datos para la factura")
    nombre = input("Nombre: ")
    nit = input("Nit: ")
    print("*==================================*")
    print("*\t\t\t\t\t\t\tNo. {0}".format(randint(0, 999)) + "*")
    print("*\t\t\t\t\t\t\tSerie:{0}".format(random.choice(string.ascii_letters)) + "*")
    print("*__________________________________*")
    print(" \tNombre: {0}".format(nombre))
    print(" \tNit: {0}".format(nit))
    print("*__________________________________*")
    for i in range(len(productos)):
        print("\t{0}....................{1}".format(productos[i],str(precios[i])))
    print("*__________________________________*")
    print("*                        TOTAL {0}*".format(total))
    print("*==================================*")



cobro()
#total_compra({'aguacate': 8.0, 'pescado': 25.0})