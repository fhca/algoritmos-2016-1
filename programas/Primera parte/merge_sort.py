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
