
"Versión iterativa de Fibonacci."
def fib_iterativo(n):
    if n <= 2:
        b = 1
    else:
        a = b = 1
        for i in range(3, n + 1):
            a, b = b, a + b      # c = a + b; a=b; b=c
    return b

print(list(fib_iterativo(x) for x in range(1, 20)))

"Versión recursiva de Fibonacci."
def fib_recursivo(n):
    if n <= 2:
        return 1
    else:
        return fib_recursivo(n - 1) + fib_recursivo(n - 2)  # recursividad de cola

print(list(fib_recursivo(x) for x in range(1, 20)))