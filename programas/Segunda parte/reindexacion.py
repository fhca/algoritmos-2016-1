__author__ = 'fhca'


class Arreglo:
    def __init__(self, datos="vacio"):
        if datos == "vacio":
            self.datos = []
        else:
            self.datos = list(datos)

    def __len__(self):
        return len(self.datos)

    def __getitem__(self, item):
        return self.datos[item - 1]

    def __setitem__(self, key, value):
        self.datos[key - 1] = value

    def __str__(self):
        return str(self.datos)

A = Arreglo(("a", "b", "c"))
print(A)
A[3]=6
print(A[1])
print(A[3])