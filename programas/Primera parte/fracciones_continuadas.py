__author__ = 'fhca'

"repite los últimos rep coeficientes, las ai en 1/(a1 + 1/(a2 + 1/(a3 +...)))"
def frac(coef, rep=1):
    val = 0
    last = 2000001
    n = len(coef)
    if rep < 1:
        rep = 1

    if rep > n:
        rep = n
    for i in range(last-1, -1, -1):
        if i < n:
            ai = coef[i]
        else:
            ai = coef[n - rep + (i - n) % rep]
        if val == 0:
            val = ai
        else:
            val = ai + 1/val
    return 1 / val


print(frac([6], 2))
