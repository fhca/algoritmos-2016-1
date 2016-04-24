__author__ = 'Profe'

negacion_binaria = ["A01DA", "A10DA", "AbbNH"]

castor_ocupado = ["A01DB", "A11IC", "B01IA", "B11DB", "C01IB", "C11DH"]

reglas = castor_ocupado

estado_actual = "A"

cabeza = 10

cinta = ['b']*30

#cinta[10:20]=["1", "1", "0", "0", "1", "0", "1", "1", "1", "0"]
cinta[10]="0"

def muestra_cinta():
    print(" " * cabeza + estado_actual)
    print("".join(cinta))

def compara_light_old(c1, c2):
    if c1 == c2:
        return True
    elif c1 == 'b' and c2 == '0':
        return True
    elif c2 == 'b' and c1 == '0':
        return True
    return False

def compara_light(c1, c2):
    return (c1 == c2) or (c1 == 'b' and c2 == '0') or (c2 == 'b' and c1 == '0')

def compara_estricto(c1, c2):
    return c1 == c2

muestra_cinta()

pasos = 0
while estado_actual != "H":
    pasos +=1
    if pasos >= 1000:
        print("CICLO INFINITO!!!")
        break
    for cadena in reglas:
        (estado, leido, escribir, direccion, proximo) = tuple(cadena)
        if estado == estado_actual and compara_light(cinta[cabeza],leido):
            print(cadena)
            cinta[cabeza] = escribir
            if direccion == "D":
                cabeza += 1
            elif direccion == "I":
                cabeza -= 1
            estado_actual = proximo
            muestra_cinta()

