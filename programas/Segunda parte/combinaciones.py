__author__ = 'fhca'

"Combinaciones de n elementos tomados de m en m. Versión recursiva."
def comb(n, m):
    if n == 1 or m == 0 or n == m:
        v = 1
    else:
        v = comb(n - 1, m) + comb(n - 1, m - 1)
    return v

n=5
for i in range(n + 1):
    print(comb(n, i), "* x ^", n - i, end=" + ")

K=5
print()
for n in range(K + 1):
    print(" "* (K - n), end="")
    for i in range(n + 1):
        print(comb(n, i), end=" ")
    print()