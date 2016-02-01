__author__ = 'fhca'

import insercion
from random import randrange

fp = open("insercion.txt", "w")
for n in range(1, 1001):
    A = [randrange(1000) for _ in range(n)]
    insercion.pasos = 0
    insercion.ordenar2(A)
    fp.write("{} {}\n".format(n, insercion.pasos))
fp.close()

