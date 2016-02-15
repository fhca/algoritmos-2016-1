__author__ = 'fhca'

import random

class Inversiones:
    def __init__(self, ary):
        self.ary = ary # arreglo de entrada
        self.reporta = [] # lista de parejas de indices
        self.pasos = 0  # contador de pasos
        for i in range(len(ary)):
            for j in range(i + 1, len(ary)):
                if self.ary[i] > self.ary[j]:
                    self.reporta.append((i, j))
                self.pasos += 1

    def inversiones(self):
        return self.reporta

    def tiempo(self):
        return self.pasos

for n in range(1, 1001):
    inv = Inversiones([random.randrange(10000) for i in range(n)])
    #print(inv.inversiones())
    print(n, inv.tiempo())
