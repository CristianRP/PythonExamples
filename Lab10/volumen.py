#!/usr/bin/env python3
# -*- coding:utf8 -*-
def calcular_ml():
    CONVER = 1000000
    salir = ""
    while salir != "no":
        volumen = float(input(("Ingresa el volumen(m3):\n")))
        ml = volumen * CONVER
        print("Hay {0}ml en {1}m3".format(round(ml), round(volumen)))
        salir = str(input("Quieres realizar otra conversion? si/no \t" ))

calcular_ml()