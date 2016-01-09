__author__ = 'fhca'

import random

"""La complejidad de un algoritmo se mide en términos de 'n', el número de elementos
de la entrada. Así que si nuestro algoritmo nunca considera 'n' dentro de sus
procedimientos, la teoría nos dice que funcionará en tiempo CONSTANTE, lo cual es lo
menos que un algoritmo podría tardar, asintóticamente hablando. Aunque aquí hay por
lo menos un problema. ¿Puedes identificar cuál es?. Nota: B es la lista A ordenada."""

def algoritmo1():
    "Super-chafa, pero ¿por qué funciona?."
    """ Pythonadas:
            [0] * 100 : genera una lista de 100 valores, todos iguales a '0'
    """
    A = list(range(100))
    random.shuffle(A)
    print("A:", A)
    B = [0] * 100
    for a in A:
        B[a] = a
    print("B:", B)

def algoritmo2():
    "Este mejora un poco, pero aún chafea, ¿por qué?, ¿cuánto se tarda?."
    """ Pythonadas:
            randrange(n) : es como el range(n), pero aleatorio, es decir, genera
            números enteros al azar en el rango de 0 a n-1.

            print( ... , end=", ") : cambia el caracter que usa normalmente print al
            final de una linea ('\n'=cambio de línea) por la cadena que se le ponga
            al 'end', en este caso, una coma y un espacio SIN CAMBIO DE LINEA.
    """
    A = []
    for i in range(100):
        A.append(random.randrange(100))
    print("A:", A)
    import insercion  #para verificar el resultado, no contarlo en el tiempo de este
    print("Aord:", insercion.ordenar(A))  #A sigue desordenada
    B = [-1] * 1000  # arreglo "vacio", -1 = espacio vacío
    for a in A:
        desp = 0
        "busca un espacio vacío..."
        while B[10 * a + desp] != -1:
            desp += 1
        B[10 * a + desp] = a  # pone 'a' en el primer espacio vacío encontrado
    print("B:    ", end=" ")
    for b in B:
        if b != -1:  # elimina el -1, sentinela de espacio no ocupado en B
            print(b, end=", ")
    print()



algoritmo2()
