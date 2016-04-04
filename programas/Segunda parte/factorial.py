__author__ = 'fhca'

def factorial_iterativo(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s

print(factorial_iterativo(5))

def factorial_recursivo(n):
    if n <= 1:
        return n
    else:
        return n * factorial_recursivo(n - 1) # recursividad de cola

print(factorial_recursivo(5))