__author__ = 'fhca'

class Turing:
    def __init__(self, reglas="vacias", cinta="0"):
        self.tam = 100
        mitad = self.tam // 2
        "agregando las reglas"
        if reglas == "vacias":
            self.reglas = []
        else:
            self.reglas = reglas
        "definición de la cinta"
        self.cinta = ['b'] * self.tam
        if cinta == "0":
            self.cinta[mitad] = '0'
        else:
            self.cinta[mitad:len(cinta)] = list(cinta)
        "comparación estricta ssi una regla lee 'b'. comparación ligera === '0'=='b'."
        self.compara = self.compara_ligera
        for r in self.reglas:
            if "b" == r[1]:
                self.compara = self.compara_estricta
                break
        self.cabeza = mitad
        self.estado_actual = "A"

    def añade_regla(self, r):
        self.reglas.append(r)
        self.compara = self.compara_ligera
        for r in self.reglas:
            if "b" == r[1]:
                self.compara = self.compara_estricta
                break

    def compara_ligera(self, c1, c2):
        return (c1 == c2) or (c1 == 'b' and c2 == '0') or (c2 == 'b' and c1 == '0')

    def compara_estricta(self, c1, c2):
        return c1 == c2

    def muestra_cinta(self):
        print(" " * self.cabeza + self.estado_actual)
        print("".join(self.cinta))

    def lee(self):
        return self.cinta[self.cabeza]

    def escribe(self, e):
        self.cinta[self.cabeza] = e

    def mueve(self, dir):
        if dir == "D":
            self.cabeza += 1
        elif dir == "I":
            self.cabeza -= 1

    def cambia_estado(self, e):
        self.estado_actual = e

    def anima(self):
        pasos = 0
        infinito = 1000
        self.muestra_cinta()
        while self.estado_actual != "H":
            pasos += 1
            if pasos >= infinito:
                print("CICLO INFINITO!!!")
                break
            for cadena in self.reglas:
                (estado, leido, escribir, direccion, proximo) = tuple(cadena)
                if estado == self.estado_actual and self.compara(self.lee(), leido):
                    print(cadena)
                    self.escribe(escribir)
                    self.mueve(direccion)
                    self.cambia_estado(proximo)
                    self.muestra_cinta()

"Castor ocupado"
#Turing(["A01DB", "A11IC", "B01IA", "B11DB", "C01IB", "C11DH"]).anima()
"Negación binaria"
#Turing(["A01DA", "A10DA", "AbbNH"], "1101101110101").anima()
"Repite n"
#Turing(["A00N1", "A11N1", "10NNH", "11ED2", "20ED3", "211D2", "301I4", "311D3", "40EI5", "411I4", "501D1", "511I5"], "111").anima()
"rebota dos posiciones"
#Turing(["A00IA", "A11DA"], "1").anima()
"recorre unos"
#Turing(["A00IB", "A11DA", "B00DA", "B11IB"], "1111111").anima()
"101010..."
#Turing(["A01DB", "B00DA"]).anima()
"110110110..."
#Turing(["A01DB", "B01DC", "C00DA"]).anima()
"unifica:   1000010001 -> 111111111"
Turing(["A00DA", "A11IB", "B01IB", "BbbDC", "C11DC", "C01DA", "CbbNH", "B11DC", "AbbIB"], "10000010000100100000011").anima()