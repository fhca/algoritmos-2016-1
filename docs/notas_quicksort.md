# Quicksort

Usa el paradigma de "divide y vencerás"

Ordenaremos el subarreglo A[p ... r] de la siguiente manera:

Divide (reacomoda) A[p ... r] en dos subarreglos, posiblemente vacíos A[p ... q-1] y A[q+1 ... r] con pivote q, de 
manera que los del primer subarreglo sean menores o iguales que A[q] y los del segundo subarreglo sean mayores o iguales.

Vence ordenando recursivamente los subarreglos A[p ... q-1] y A[q+1 ... r]

Para combinar, no hay que hacer nada, puesto que los elementos ya estarán en su lugar.

    quicksort(A, p, r):
        si p < r
            q = particiona(A, p, r)
            quicksort(A, p, q - 1)
            quicksort(A, q + 1, r)
 
La llamada inicial es porsupuesto quicksort(A, 0, len(A)-1).

La función que particiona es así:

    particiona(A, p, r):
        x = A[r]
        i = p - 1
        para j = p hasta r - 1
            si A[j] <= x
                i ++
                intercambia A[i] con A[j]
        intercambia(A[i + 1], A[r])
        devuelve i + 1

