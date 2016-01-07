# algoritmos-2016-1

Rama de ejemplos hechos principalmente en Python, adaptados del Cormen 3ed.

Ejemplos de adaptaciones:

1. Las listas en Python (en C, en Java, etc.) comienzan en el elemento con
índice 0 y en el libro empiezan en índice 1, por lo que A[1] en el libro sería
A[0] en el programa. El chequeo de rango de índices sería i > 0 en el libro y
i >= 0 en el programa, etc.

2. En Python, para indicar un rango de elementos se usan ":", ejemplos:

A[:] = toda la lista A

A[1:] = los elementos de la lista A empezando con el de índice 1 "hasta el final"

A[:5] = los elementos de la lista A desde el principio hasta el de índice 4 ("uno
        antes que 5")

A[3:7] = los elementos desde el de índice 3 hasta el de índice 6 (3, 4, 5 y 6, o sea
        "de 3 a antes que 7")
