__author__ = 'fhca'


def odd(n):
    if n <= 1:
        return 1
    elif (n % 2) == 1:
        return n + odd(n - 2)
    else:
        return odd(n - 1)

print(odd(10))  # --> 25

def even(n):
    if n<= 2:
        return 2
    elif (n % 2) == 0:
        return n + even(n - 2)
    else:
        return even(n - 1)

print(even(10))  # --> 30

def oddi(n):
    suma = 0
    for i in range(1, n + 1, 2):
        suma += i
    return suma

def oddi2(n):
    return sum(range(1, n + 1, 2))

print("oddi", oddi(9))
print("oddi2", oddi2(9))

def evencito(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma

print("evencito", evencito(10))

def evencito1(n):
    return sum(range(2, n + 1, 2))

print("evencito1", evencito1(11))