__author__ = 'fhca'

"Combinaciones de n elementos tomados de m en m. Versión recursiva."
def comb(n, m):
    if n == 1 or m == 0 or n == m:
        v = 1
    else:
        v = comb(n - 1, m) + comb(n - 1, m - 1)
    return v

def comb_it(n, m):
    pila = []
    suma = 0
    pila.append(("comb", n, m))
    while len(pila)>0:
        accion, n, m = pila.pop()
        if accion == "comb":
            if n == 1 or m == 0 or n == m:
                pila.append(("agrega", n, m))
            else:
                pila.append(("comb", n-1, m))
                pila.append(("comb", n-1, m-1))
        else:
            suma += 1
    return suma

n=5
for i in range(n + 1):
    print(comb(n, i), "* x ^", n - i, end=" + ")

print()
n=5
for i in range(n + 1):
    print(comb_it(n, i), "* x ^", n - i, end=" + ")

K=8
print()
for n in range(K + 1):
    print(" "* (K - n), end="")
    for i in range(n + 1):
        print(comb(n, i), end=" ")
    print()

K=8
print()
for n in range(K + 1):
    print(" "* (K - n), end="")
    for i in range(n + 1):
        print(comb_it(n, i), end=" ")
    print()

