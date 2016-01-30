a = 1
b = 1
print(a)
print(b)
c = a + b
while c < 1e9:  # detente antes de llegar a mil millones
    print(c)
    a = b
    b = c
    c = a + b