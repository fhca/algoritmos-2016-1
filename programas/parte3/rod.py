__author__ = 'fhca'

# lista de precios p_1, p_2,..., p_10
p=[1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def memoized_cut_rod(p, n):
    r=[0] * (n + 1)
    for i in range(n + 1):
        r[i] = -1
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

print("ganancia n=10:", memoized_cut_rod(p, 10))

def bottom_up_cut_rod(p, n):
    r=[0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j- i])
        r[j] = q
    return r
print("ganancias:", bottom_up_cut_rod(p, 10))

def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * n # restar uno de indices del libro
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j - 1] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    print("r:", r)
    print("s:", s)
    while n > 0:
        n -= s[n - 1]
        print(s[n - 1])

print_cut_rod_solution(p, 10)
print_cut_rod_solution(p, 7)