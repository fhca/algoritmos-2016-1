__author__ = 'fhca'

import insercion
from random import shuffle


print("Caso promedio (permutación aleatoria)...")
A = list(range(100)) # lista del 0 al 99
shuffle(A) # les aplica una permutación al azar
print("A:", A)
insercion.pasos = 0  # inicializa número de pasos
print("Aord:", insercion.ordenar2(A))  # ordena
print("pasos:", insercion.pasos)  # imprime numero de pasos

print("\nMejor caso (datos ya ordenados)...")
A = list(range(100)) # lista del 0 al 99
print("A:", A)
insercion.pasos = 0  # inicializa número de pasos
print("Aord:", insercion.ordenar2(A))  # ordena
print("pasos:", insercion.pasos)  # imprime numero de pasos

print("\nPeor caso (datos ordenados de mayor a menor)...")
A = list(range(99, -1, -1))
print("A:", A)
insercion.pasos = 0  # inicializa número de pasos
print("Aord:", insercion.ordenar2(A))  # ordena
print("pasos:", insercion.pasos)  # imprime numero de pasos

