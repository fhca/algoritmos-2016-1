# Programas de ejemplo para el curso

*IMPORTANTE: Como tarea para cada clase, debes traducir el programa visto en
clase de esta lista al lenguaje C o Java de tu elección.*

Orden en que deben verse:

1. [insercion.py](insercion.py) (visto el 2 de febrero)
1. [pruebas_insercion.py](pruebas_insercion.py) (para ver el 4 de febrero)
1. [pruebas_insercion0.py](pruebas_insercion0.py) (para ver el 4 de febrero)
1. [ordenamiento_constante.py](ordenamiento_constante.py) (para ver el 4 de febrero)
1. [merge_sort.py](merge_sort.py)
1. [pruebas_merge0.py](pruebas_merge0.py)

Programas del examen diagnóstico (2 de febrero):

1. [fibonacci.py](fibonacci.py)
1. [fibonacci.c](fibonacci.c)
1. [Fibonacci.java](Fibonacci.java)

Rama de ejemplos hechos principalmente en Python, adaptados del Cormen 3ed.

Ejemplos de adaptaciones:

1. Las listas en Python (en C, en Java, etc.) comienzan en el elemento con
índice 0 y en el libro empiezan en índice 1, por lo que A[1] en el libro sería
A[0] en el programa. El chequeo de rango de índices sería i > 0 en el libro y
i >= 0 en el programa, etc.
1. En Python, para indicar un rango de elementos se usan ":", ejemplos:

  >A[:] = toda la lista A

  >A[1:] = los elementos de la lista A empezando con el de índice 1 "hasta el final"

  >A[:5] = los elementos de la lista A desde el principio hasta el de índice 4 ("uno antes que 5")
