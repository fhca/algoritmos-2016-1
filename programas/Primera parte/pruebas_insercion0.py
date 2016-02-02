__author__ = 'fhca'

import insercion
from random import randrange

def caso_promedio(arch):
    fp = open(arch, "w")
    for n in range(1, 1001):
        A = [randrange(1000) for _ in range(n)]
        insercion.pasos = 0
        insercion.ordenar2(A)
        fp.write("{} {}\n".format(n, insercion.pasos))
    fp.close()

def caso_mejor(arch):
    fp = open(arch, "w")
    for n in range(1, 1001):
        A = list(range(n))
        insercion.pasos = 0
        insercion.ordenar2(A)
        fp.write("{} {}\n".format(n, insercion.pasos))
    fp.close()


def caso_peor(arch):
    fp = open(arch, "w")
    for n in range(1, 1001):
        A = list(range(n, 0, -1))
        insercion.pasos = 0
        insercion.ordenar2(A)
        fp.write("{} {}\n".format(n, insercion.pasos))
    fp.close()

caso_promedio("insercion_promedio.txt")
caso_mejor("insercion_mejor.txt")
caso_peor("insercion_peor.txt")
