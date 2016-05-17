__author__ = 'fhca'

class Gráfica:
	def __init__(self, n):
        self.n = n  # número de nodos
        self.m = 0  # número de aristas no dirigidas
		self.estructura = [ [] for i in range(n) ]
        self.llave = [-1e30] * n # llaves de nodos
        self.peso = []  #pesos de aristas

	def aristad(self, origen, destino):
		self.estructura[origen].append(destino)

	def arista(self, origen, destino, peso = -1e30):
        self.m += 1
		self.aristad(origen, destino)
		self.aristad(destino, origen)
        self.peso[hash(origen,destino)] = peso

	def __str__(self):
		return str(self.estructura)

	def cadenad(self, cad):
        self.m += len(cad) - 1
		for a in zip(cad, cad[1:]):
			self.aristad(a[0], a[1])

	def cadena(self, cad):
        self.m += len(cad) - 1
		for a in zip(cad, cad[1:]):
			self.arista(a[0], a[1])

    def cuenta_aristas(self):
        if self.m == 0:  # sólo si no se ha inicializado self.m
            self.m = sum(len(vecinos) for vecinos in self.estructura)

    "función hash para pesos de aristas, asume que hay self.m aristas"
    def hash(a,b):
        self.cuenta_aristas()
        return ((a + b) * self.n + (a + b)) % self.m

class ColaP:
    def __init__(self):
        self.estructura = []

casita = Gráfica(5)
print(casita)

casita.arista(0,1)
casita.arista(1,2)
casita.arista(2,3)
casita.arista(3,4)
casita.arista(4,0)
casita.arista(0,3)
casita.arista(1,4)
casita.arista(1,3)

print(casita)

casita2 = Gráfica(5)
casita2.cadena([0,4,1,3,2,1,0,3,4])
print("casita2:", casita2)

k5 = Gráfica(5)
k5.cadena([0,1,2,3,4,0,2,4,1,3,0])
print(k5)

k33 = Gráfica(6)
k33.cadena([3,0,4,1,5,2,3,1])
k33.arista(4,2)
k33.arista(0,5)
print(k33)