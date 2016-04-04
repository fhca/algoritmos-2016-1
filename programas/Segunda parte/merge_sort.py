__author__ = 'fhca'


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []  # 1 .. n1+1
    R = []  # 1 .. n2+1
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    # En Python, las lineas anteriores se pueden escribir como:
    #   L = A[p : q+1]
    #   R = A[q+1 : r+1]
    infinito = 1e30  # un número muy grande
    L.append(infinito)
    R.append(infinito)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def ordenar(A):
    B = A[:]  # hace una copia, para no modificar A
    merge_sort(B, 0, len(B) - 1)
    return B


if __name__ == "__main__":
    A = [2, 4, 5, 7, 1, 2, 3, 6]
    print(ordenar(A))
    print(A)  # A sin modificar


pasos = 0

def merge2(A, p, q, r):
    global pasos
    n1 = q - p + 1 ; pasos += 1
    n2 = r - q ; pasos += 1
    L = [] ; pasos += 1  # 1 .. n1+1
    R = [] ; pasos += 1  # 1 .. n2+1
    for i in range(n1):
        L.append(A[p + i]) ; pasos += 1
    for j in range(n2):
        R.append(A[q + j + 1]) ; pasos += 1
    # En Python, las lineas anteriores se pueden escribir como:
    #   L = A[p : q+1]
    #   R = A[q+1 : r+1]
    infinito = 1e30 ; pasos += 1  # un número muy grande
    L.append(infinito) ; pasos += 1
    R.append(infinito) ; pasos += 1
    i = 0 ; pasos += 1
    j = 0 ; pasos += 1
    for k in range(p, r+1):
        if L[i] <= R[j]:
            pasos += 1  # comparación
            A[k] = L[i] ; pasos += 1
            i += 1 ; pasos += 1
        else:
            pasos += 1  # comparación
            A[k] = R[j] ; pasos += 1
            j += 1 ; pasos += 1


def merge_sort2(A, p, r):
    global pasos
    if p < r:
        pasos += 1  # comparación
        q = (p + r) // 2 ; pasos += 1
        merge_sort2(A, p, q) ; pasos += 1
        merge_sort2(A, q+1, r) ; pasos += 1
        merge2(A, p, q, r) ; pasos += 1


def ordenar2(A):
    global pasos
    B = A[:] ; pasos += 1  # hace una copia, para no modificar A
    merge_sort2(B, 0, len(B) - 1) ; pasos += 1
    return B


if __name__ == "__main__":
    A = [2, 4, 5, 7, 1, 2, 3, 6]
    print(ordenar2(A))
    print(A)  # A sin modificar
