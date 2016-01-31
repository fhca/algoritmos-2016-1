__author__ = 'fhca'

s = []


def hanoi(n, a, b, c):
    if n == 1:
        s.extend((str(n), c))
    else:
        hanoi(n - 1, a, c, b)
        s.extend((str(n), c))
        hanoi(n - 1, b, a, c)

hanoi(5, "A", "B", "C")
print("".join(s))
