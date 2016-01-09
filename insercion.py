__author__ = 'fhca'

""" Ordenamiento por inserción. Adaptado del Cormen 3ed, Pag.18"""

def ordenamiento_por_inserción(A):
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

if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print("A:", A)
    Aord = ordenamiento_por_inserción(A)
    print("Aord:", Aord)

""" Ordenamiento por inserción. Incluye conteo de número de pasos """

pasos = 0
def ordenamiento_por_inserción2(A):
    """Algoritmo chafa, sólo utilizar como ejemplo en clase.
    A : una lista de enteros o elementos comparables con '>'. """
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

if __name__ == '__main__':
    A = [5, 2, 4, 6, 1, 3]
    print("A:", A)
    Aord = ordenamiento_por_inserción2(A)
    print("Aord:", Aord)
    print("Número de pasos:", pasos)

