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

def bb_recursiva(elem, lista_ordenada, inicio, fin):
    if inicio > fin:
        return -1
    else:
        medio = (inicio + fin) // 2
        if elem < lista_ordenada[medio]:
            return bb_recursiva(elem, lista_ordenada, inicio, medio)
        elif elem == lista_ordenada[medio]:
            return medio
        else:
            return bb_recursiva(elem, lista_ordenada, medio + 1, fin)

A = ordenar([5, 2, 4, 3, 5, 2, 1, 7, 6, 9, 9, 0])
print(A)

resultado = bb_recursiva(9, A, 0, len(A)-1)
if resultado == -1:
    print("no encontrado")
else:
    print("encontrado en la posición", resultado)
