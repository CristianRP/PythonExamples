#!/usr/bin/env python3
# -*- coding:utf8 -*-
""" Proyecto de SUMA
El proyecto consiste en crear una programa
que sume "manualmente" los numeros
"""
from itertools import zip_longest

def sumar(sumando1, sumando2):

    try:
        unidades_sumando1 = sumando1.find('.')
    except ValueError:
        unidades_sumando1 = len(sumando1)

    try:
        unidades_sumando2 = sumando2.find('.')
    except ValueError:
        unidades_sumando2 = len(sumando2)

    if unidades_sumando1 > unidades_sumando2:
        sumando2 = '0' * (unidades_sumando1 - unidades_sumando2) + sumando2

    if unidades_sumando2 > unidades_sumando1:
        sumando1 = '0' * (unidades_sumando2 - unidades_sumando1) + sumando1

    array1 = []
    for i in sumando1:
        array1.append(int(i))
        'print(i)'

    array2 = []
    for i in sumando2:
        array2.append(int(i))
        'print(i)'

    array3 = []
    for x in zip(array1, array2):
        array3.append(list_sum(x))

    # array3 = [list_sum([1,2]), list_sum([2,3])]
    print(sumando1)
    print(sumando2)
    print(array3[0],array3[1],array3[2])


def list_sum(array1):
    if len(array1) == 1:
        return array1[0]
    else:
        return array1[0] + list_sum(array1[1:])

sumar('123.123', '456.456')