from random import randint
import string
import random

def cobro():
    print("Bienviendo al sistema de cobro PythonStore")
    print("Ingresa los articulos por cobrar y escribe 'terminar'\npara finalizar la lista.")
    abarrotes = []
    precios = []
    cantidades = []
    finalice = True
    while finalice:
        producto = input("Ingresa los abarrotes: ")
        if (producto == "terminar"):
            finalice = False
        else:
            precio = float(input("Ingresa el precio (Q):"))
            cantidad = int(input("Ingresa la cantidad: "))
            abarrotes.append(producto.strip())
            precios.append(precio)
            cantidades.append(cantidad)
    facturacion(abarrotes, precios, total_productos(precios, cantidades), cantidades)

def total_productos(precios, cantidad):
    multi = 0
    for i in range(len(precios)):
        total = precios[i] * cantidad[i]
        multi += total
    return multi

def total_compra(precios):
    sum = 0
    for i in range(0,len(precios)):
        sum = sum + precios[i]
    return sum

def facturacion(productos, precios, total, cantidades):
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
    print("*Producto......Cantidad......Precio*")
    for i in range(len(productos)):
        print("\t{0}............{1}........{2}".format(productos[i],str(cantidades[i]),str(precios[i])))
    print("*__________________________________*")
    print("*                        TOTAL {0}*".format(total))
    print("*==================================*")



cobro()
#total_compra({'aguacate': 8.0, 'pescado': 25.0})