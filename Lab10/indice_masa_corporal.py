#!/usr/bin/env python3
# -*- coding:utf8 -*-
#(IMC = peso[kg] / estatura[m2]).

def calcular_imc():
    print("Bienvenido al sistema para calcular tu IMC")
    LBS = 2.2046
    salir = ""
    while (salir.lower() != "salir"):
        peso = float(input("Ingresa tu peso: \n"))
        libras = str(input("Ingresaste kg o lbs?"))
        if (libras == "lbs" or libras == "libras"):
            new_peso = peso / LBS
        else:
            new_peso = peso
        estatura = float(input("Ingresa tu estatura(m): \n"))
        imc = new_peso / (estatura**2)
        print("Tu IMC es de {0}".format(round(imc,2)))
        if (round(imc) < 18.5):
            print("Estas en un peso inferior al normal")
        elif (round(imc) in range(19, 25)):
            print("Estas en un peso normal")
        elif (round(imc) in range(25, 30)):
            print("Estas en un peso superior al normal")
        else:
            print("Estas obeso!")
        draw_table()
        salir = str(input("Quieres calcular otro IMC o salir? calcular/salir \n"))

def draw_table():
    print("*******************************************")
    print("|Composición Corporal    \t           IMC|")
    print("|Peso Inferior al normal \t Menos de 18.5|")
    print("|Normal                  \t   18.5 - 24.9|")
    print("|Peso superior al normal \t     25 - 29.9|")
    print("|Obesidad                \t     Más de 30|")
    print("*******************************************")

calcular_imc()