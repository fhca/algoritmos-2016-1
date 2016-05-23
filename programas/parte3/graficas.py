__author__ = 'fhca'


class Gráfica:
    def __init__(self, param="nada"):
        if isinstance(param, int):
            self.n = param  # número de nodos
            self.etiqueta_nodo = [i for i in range(param)]
        elif isinstance(param, list):
            self.n = len(param)
            self.etiqueta_nodo = param
        self.estructura = list([] for _ in range(self.n))
        self.m = 0  # número de aristas no dirigidas

    def indice(self, et):
        return self.etiqueta_nodo.index(et)

    def arista(self, origen, destino):
        """Crea una arista no dirigida o -> d si o <= d ó de lo contrario d -> o,
        origen y destino son etiquetas."""
        self.m += 1
        i = self.indice
        self.estructura[i(origen)].append(i(destino))
        self.estructura[i(destino)].append(i(origen))

    def __str__(self):
        et = self.etiqueta_nodo
        s = ', '.join(et[i] + ':[' + ', '.join(et[t] for t in l) + ']' for i, l in enumerate(self.estructura))
        return '[' + s + ']'

    def cadena(self, cad):
        "Agrega una cadena de nodos con las etiquetas enlistadas en cad."
        for a in zip(cad, cad[1:]):
            self.arista(*a)

    def lista_de_adyacentes(self, et):
        return [self.etiqueta_nodo[i] for i in self.estructura[self.indice(et)]]


class Gráfica_con_pesos(Gráfica):
    "Gráfica con valores asignados a aristas y nodos."

    def __init__(self, n, pesos_nodos="infinito", pesos_aristas="nada"):
        super().__init__(n)
        if pesos_nodos == "infinito":
            self._peso_nodo = [1e30] * self.n  # pesos de nodos
        else:
            if isinstance(pesos_nodos, list):
                self._peso_nodo = pesos_nodos
        if pesos_aristas == "nada":
            self._peso_arista = [1e30] * (self.n * (self.n - 1))  # pesos de aristas
        else:
            if isinstance(pesos_aristas, list):
                self._peso_arista = pesos_aristas

    def hash(self, origen, destino):
        "función hash para pesos de aristas, basado en etiquetas."
        i = self.indice
        if i(origen) > i(destino):
            origen, destino = destino, origen
        if i(destino) in self.estructura[i(origen)]:
            return i(origen) * self.n + i(destino)  # n^2/2 TODO: usar diccionarios
        else:
            return -1

    def pesos_nodos(self, ary):
        "Inserta lista de pesos de nodos."
        if len(ary) >= self.n:
            self._peso_nodo = ary[:self.n]  # recorta a la cantidad necesaria
        else:
            print("Error: no se definió la cantidad de pesos correcta.")

    def pesos_aristas(self, ary):
        "Inserta lista de pesos de aristas."
        if len(ary) >= self.m:
            self._peso_arista = ary[:self.m]  # recorta a la cantidad necesaria
        else:
            print("Error: no se definió la cantidad de pesos correcta.")

    def arista(self, origen, destino, peso_arista=0, peso_origen=1e30, peso_destino=1e30):
        "Inserta una arista con peso."
        super().arista(origen, destino)
        self._peso_arista[self.hash(origen, destino)] = peso_arista
        self._peso_nodo[self.indice(origen)] = peso_origen
        self._peso_nodo[self.indice(destino)] = peso_destino

    def set_peso_nodo(self, et, peso):
        "Ajusta el peso de un nodo"
        i = self.indice(et)
        if i < self.n:
            self._peso_nodo[i] = peso
        else:
            print("Error: índice fuera de rango")

    def get_peso_nodo(self, et):
        "Obtiene el peso de un nodo."
        i = self.indice(et)
        if i < self.n:
            return self._peso_nodo[i]
        else:
            print("Error: índice fuera de rango")

    def set_peso_arista(self, origen, destino, peso):
        "Ajusta el peso de una arista."
        if 0 <= self.hash(origen, destino):
            self._peso_arista[self.hash(origen, destino)] = peso
        else:
            print("Error: índice fuera de rango o arista inexistente")

    def get_peso_arista(self, origen, destino):
        "Obtiene el peso de una arista."
        if 0 <= self.hash(origen, destino):
            # print("hash", origen, destino, self.hash(origen, destino))
            return self._peso_arista[self.hash(origen, destino)]
        else:
            return 1e30

    def muestra_pesos_nodos(self):
        "Muestra la lista de pesos de los nodos. debug."
        s = ", ".join(str(self.etiqueta_nodo[t]) + ":" + str(self._peso_nodo[t]) for t in range(len(self.estructura)))
        return "[" + s + "]"

    def cadena(self, cad, pesos_nodos="infinito", pesos_aristas="ceros"):
        "Agrega una cadena de nodos con las etiquetas enlistadas en cad."
        if pesos_nodos == "infinito":
            pesos_nodos = [1e30] * self.n
        if pesos_aristas == "ceros":
            pesos_aristas = [0] * self.m
        i = 0
        for a in zip(cad, cad[1:]):
            self.arista(*a, pesos_aristas[i], *pesos_nodos[i:i + 2])
            i += 1


class Gráfica_para_Prim(Gráfica_con_pesos):
    def __init__(self, n):
        super().__init__(n)
        self.predecesores = [None] * self.n
        self.etiquetas = self.etiqueta_nodo
        self.llaves = self._peso_nodo
        self.llave = self.set_peso_nodo

    def predecesor(self, et, nodo):
        "Predecesor en el MST del nodo dado."
        self.predecesores[self.indice(et)] = nodo


class ColaP:
    """Cola de prioridad. El valor almacenado (ej. i), es el índice del
    nodo y self.llave[i] es la llave con la cual se acomoda este índice
    en la cola. La estructura de datos es un montículo de mínimos."""

    def __init__(self, gráfica):
        self.tam = -1
        self.llaves = gráfica.llaves
        self.etiquetas = gráfica.etiquetas
        self.A = list(range(gráfica.n))  # ín
        self.const_mont_min()

    @staticmethod
    def padre(i):
        return (i - 1) // 2

    @staticmethod
    def izq(i):
        return 2 * i + 1

    @staticmethod
    def der(i):
        return 2 * i + 2

    def imin(self, i, j, k):
        "Calcula el mínimo valor de la llave de 3 valores en las posiciones i,j,k."
        tam = self.tam
        if k <= tam and self.llave(k) < self.llave(i):
            _min = k
        else:
            _min = i
        if j <= tam and self.llave(j) < self.llave(_min):
            _min = j
        return _min

    def llave(self, x):
        return self.llaves[self.A[x]]

    def mont_min(self, i):
        "'Arregla' la cadena de nodos desde i hasta una hoja."
        m = self.imin(i, self.izq(i), self.der(i))
        if m != i:
            self.A[i], self.A[m] = self.A[m], self.A[i]
            self.mont_min(m)

    def const_mont_min(self):
        "Construye un montículo."
        self.tam = len(self.A) - 1
        for i in range(self.padre(self.tam), -1, -1):
            self.mont_min(i)

    def extrae(self):
        "Extrae un elemento de la cola de prioridad."
        try:
            res = self.A[0]
            self.A[0] = self.A[self.tam]
            self.A = self.A[:self.tam]  # ajusta estructura a tam
            self.tam -= 1
            self.mont_min(0)
            return self.etiquetas[res]
        except IndexError:
            print("Error: cola vacía!")

    def añade(self, et):
        "Agrega un elemento a la cola de prioridad."
        try:
            i = self.indice(et)
            self.A = self.A[:self.tam]  # ajusta estructura a tam
            self.A.append(i)
            self.const_mont_min()
        except Exception:
            print("Error: índice fuera de rango")

    def indice(self, et):
        "Dice el índice del nodo dado por su etiqueta."
        return self.etiquetas.index(et)

    def cambia_llave(self, et, valor):
        "Modifica la llave de un nodo dado por su etiqueta."
        if et in self:
            j = self.indice(et)  # índice del nodo
            i = self.A.index(j)  # índice de j en el montículo
            self.llaves[j] = valor
            while i > 0 and self.llave(self.padre(i)) > self.llave(i):
                pi = self.padre(i)
                self.A[i], self.A[pi] = self.A[pi], self.A[i]
                i = pi  ## Ejemplo de gráfica con 5 nodos

    def __str__(self):
        "Convierte a cadena."
        return str(self.A)

    def __len__(self):
        "Número de elementos en la cola"
        return len(self.A)

    def __contains__(self, et):
        "et está guardado en la cola?. Para usar con 'in'."
        return self.indice(et) in self.A


G = Gráfica_para_Prim(list('abcdefghi'))
G.cadena("abcdefghicfd", pesos_aristas=[4, 8, 7, 9, 10, 2, 1, 7, 2, 4, 14])
G.arista('h', 'b', 11)
G.arista('i', 'g', 6)
G.arista('a', 'h', 8)
G.llave("a", 0)
Q = ColaP(G)
while len(Q) > 0:  # cola no vacía
    print("Q", Q)
    u = Q.extrae()
    print("extrae", u, "llave", G.get_peso_nodo(u))
    for v in G.lista_de_adyacentes(u):
        print("ady", v)
        if v in Q and G.get_peso_arista(u, v) < G.get_peso_nodo(v):
            G.predecesor(v, u)
            Q.cambia_llave(v, G.get_peso_arista(u, v))
            print("pred", u, "llave", G.get_peso_arista(u, v))

print("predecesores\n", ", ".join(G.etiqueta_nodo[i] + " -> " + str(p) for i, p in enumerate(G.predecesores)))
