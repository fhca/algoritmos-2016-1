__author__ = 'fhca'

""" Algoritmo:
    Si n = 1 (un sólo disco), pásalo a su destino (torre C)
    De lo contrario:
        Pasa n-1 discos de A a B utilizando C.
        Pasa el n-ésimo disco a C
        Pasa los n-1 discos en B a C utilizando A

    Pythonadas:
    Iniciar s como una lista vacía es práctica comun en muchos
    lenguajes. Aquí es donde acumularemos los movimientos.

    s.extend(X) agrega la "lista" de elementos X al final de la
    lista s. Aquí añadimos la lista (tupla en realidad) formada el
    entero n convertido a cadena y la cadena c. Es necesario
    convertir n a cadena para poder usar el "join" mas abajo.

    "".join(s) - toda cadena (en este caso, la cadena vacía) tiene
    un método llamado "join". Los elementos del parámetro s son
    concatenados o unidos entre si utilizando esta cadena. Por ejemplo
    si la cadena fuera "-".join(s) nos daría algo como:
    1-C-2-B-1-B-3-C-1-A-2... Este método de construir cadenas a partir
    de una lista es mucho más eficiente que el crear la cadena
    creciéndola con s = s + "C" (¿sabes por qué?).
"""

s = []


def hanoi(n, a, b, c):
    if n == 1:
        s.extend((str(n), c))
    else:
        hanoi(n - 1, a, c, b)
        s.extend((str(n), c))
        hanoi(n - 1, b, a, c)

hanoi(5, "A", "B", "C")
print("".join(s))
