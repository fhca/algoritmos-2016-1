__author__ = 'fhca'

import merge_sort
import insercion
from random import randrange
import time

maxn = 1000
def caso_promedio(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = [randrange(1000) for _ in range(n)]
        merge_sort.pasos = 0
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, merge_sort.pasos))
    fp.close()

def caso_mejor(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = list(range(n))
        merge_sort.pasos = 0
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, merge_sort.pasos))
    fp.close()


def caso_peor(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = list(range(n, 0, -1))
        merge_sort.pasos = 0
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, merge_sort.pasos))
    fp.close()

caso_promedio("merge_sort_promedio.txt")
caso_mejor("merge_sort_mejor.txt")
caso_peor("merge_sort_peor.txt")

def caso_promedio(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = [randrange(1000) for _ in range(n)]
        t0 = time.time()
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, time.time()-t0))
    fp.close()

def caso_mejor(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = list(range(n))
        t0 = time.time()
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, time.time()-t0))
    fp.close()


def caso_peor(arch):
    fp = open(arch, "w")
    for n in range(1, maxn + 1):
        A = list(range(n, 0, -1))
        t0 = time.time()
        merge_sort.ordenar2(A)
        fp.write("{} {}\n".format(n, time.time()-t0))
    fp.close()

caso_promedio("merge_sort_promedio_t.txt")
caso_mejor("merge_sort_mejor_t.txt")
caso_peor("merge_sort_peor_t.txt")