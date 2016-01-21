__author__ = 'fhca'

from merge_sort import *


def buscar(elem, lista_ordenada):
    n = len(lista_ordenada)
    min_e = 0
    max_e = n - 1
    d = (min_e + max_e) // 2  # división entera
    while elem != lista_ordenada[d]:
        if elem < lista_ordenada[d]:
            max_e = d
        else:
            min_e = d
        d = (min_e + max_e) // 2
        if d == min_e or d == max_e:
            break
    if elem == lista_ordenada[d]:
        print("encontrado en la posición", d)
    else:
        print("no encontrado")

A = ordenar([5, 2, 4, 3, 5, 2, 1, 7, 6, 9, 9, 0])
print(A)

buscar(9, A)
