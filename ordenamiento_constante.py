__author__ = 'fhca'

import random

"""La complejidad de un algoritmo se mide en términos de 'n', el número de elementos
de la entrada. Así que si nuestro algoritmo nunca considera 'n' dentro de sus
procedimientos, la teoría nos dice que funcionará en tiempo CONSTANTE, lo cual es lo
menos que un algoritmo podría tardar, asintóticamente hablando. Aunque aquí hay por
lo menos un problema. ¿Puedes identificar cuál es?. Nota: B es la lista A ordenada."""

def algoritmo1():
    "super-chafa, pero por que funciona?"
    A = list(range(100))
    random.shuffle(A)
    print("A:", A)
    B = [0] * 100
    for a in A:
        B[a] = a
    print("B:", B)

def algoritmo2():
    A = []
    for i in range(100):
        A.append(random.randrange(100))
    print(A)
    import insercion
    print(insercion.ordenar(A)) #sólo para verificar, A sigue desordenada


algoritmo2()
