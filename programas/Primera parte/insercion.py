__author__ = 'fhca'

""" Ordenamiento por inserción. Adaptado del Cormen 3ed, Pag.18"""

def ordenar(A):
    """Algoritmo chafa, sólo utilizar como ejemplo en clase.
    A : una lista de enteros o elementos comparables con '>'. """
    for j in range(1, len(A)): # en Python, como en C, las listas empiezan con índice 0
        key = A[j]
        # insertar A[j] en la lista ordenada A[0:j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

""" Pythonadas:
        if __name__ == '__main__':   Construcción que significa que el bloque que
        sigue se ejecutará sólo si el programa (este programa) se ejecuta por si
        sólo, es decir, no se ejecutará si este programa se llama desde otro
        mediante un 'include' (es, decir, si se llama como módulo).
"""
if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print("A:", A)
    Aord = ordenar(A)
    print("Aord:", Aord)

""" Ordenamiento por inserción. Incluye conteo de número de pasos """

pasos = 0
def ordenar2(A):
    """Algoritmo chafa, sólo utilizar como ejemplo en clase.
    A : una lista de enteros o elementos comparables con '>'. """
    """Pythonadas:
            En Python se puede usar ';' para agregar instrucciones a una misma línea
            creando con ello código espaghetti como en C y similares. En general
            NO SE RECOMIENDA HACER ESTO.
    """
    global pasos
    for j in range(1, len(A)): # en Python, como en C, las listas empiezan con índice 0
        key = A[j] ; pasos += 1
        # insertar A[j] en la lista ordenada A[0:j]
        i = j - 1 ; pasos += 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i] ; pasos += 1
            i -= 1 ; pasos += 1
        A[i + 1] = key ; pasos += 1
    return A

""" Pythonadas:
        if __name__ == '__main__':   Construcción que significa que el bloque que
        sigue se ejecutará sólo si el programa (este programa) se ejecuta por si
        sólo, es decir, no se ejecutará si este programa se llama desde otro
        mediante un 'include' (es, decir, si se llama como módulo).
"""
if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print("A:", A)
    Aord = ordenar(A)
    print("Aord:", Aord)
    print("Número de pasos:", pasos)

