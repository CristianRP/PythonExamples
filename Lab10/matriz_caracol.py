#!/usr/bin/env python3
# -*- coding:utf8 -*-
import random


def dibujarMatrizCaracol():
    n = int(input("Ingresa la dimensión de la matriz:"))
    matriz = [None] * n
    count = 0
    for i in range(0, n):
        matriz[i] = [None] * n
        count += 1

    for i in range(0, n):
        for j in range(0, n):
            matriz[i][j] = (int)(count)
            count += 1

    print("\nOriginal\n")
    print(matriz)
    print("\nEspiral horizontal ascendente\n")
    for i in range(0, n):
        if (i % 2) == 0:
            for j in range(0, n):
                print(str(matriz[i][j]) + "\n")
        else:
            for j in range(n - 1, -1, -1):
                print(str(matriz[i][j]) + "\n")

dibujarMatrizCaracol()


