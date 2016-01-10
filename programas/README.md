# Programas de ejemplo para el curso

*IMPORTANTE: Como tarea para cada clase, debes traducir el programa visto en
clase de esta lista al lenguaje C o Java de tu elección.*

Orden en que deben verse:
1. insercion.py
1. pruebas_insercion.py
1. ordenamiento_constante.py


Rama de ejemplos hechos principalmente en Python, adaptados del Cormen 3ed.

Ejemplos de adaptaciones:

1. Las listas en Python (en C, en Java, etc.) comienzan en el elemento con
índice 0 y en el libro empiezan en índice 1, por lo que A[1] en el libro sería
A[0] en el programa. El chequeo de rango de índices sería i > 0 en el libro y
i >= 0 en el programa, etc.

2. En Python, para indicar un rango de elementos se usan ":", ejemplos:

  >A[:] = toda la lista A

  >A[1:] = los elementos de la lista A empezando con el de índice 1 "hasta el final"

  >A[:5] = los elementos de la lista A desde el principio hasta el de índice 4 ("uno antes que 5")
