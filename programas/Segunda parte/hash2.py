__author__ = 'fhca'

def hash(palabra):
    k=0
    for p in palabra[:-1]:
        k = (ord(p) + k) * 256
    return (k + ord(palabra[-1])) % 35

def inserta(T, palabra):
    h = hash(palabra)
    if T[h] == None:
        T[h] = [palabra]
    else:
        T[h].append(palabra)

def esta(T, palabra):
    h = hash(palabra)
    if T[h] == None:
        return False
    else:
        for p in T[h]:
            if hash(p) == hash(palabra):
                return True
        return False

T = [None] * 35
inserta(T, "Sergio")
inserta(T, "América")
inserta(T, "Jucaoma")
inserta(T, "Hugo")
inserta(T, "Erki")
inserta(T, "Angélica")

print(T)
print(esta(T, "Armando"))
