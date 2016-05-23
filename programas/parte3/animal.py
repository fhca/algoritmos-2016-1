__author__ = 'fhca'

import sys


def leeArchivo(arch):
    raiz = []
    try:
        f = open(arch)
        raiz = eval(f.readline())
        f.close()
    except:
        print("Algo salió mal!")
    return raiz


respuestaNO = ["n", "N", "no", "No", "NO"]


def articula(animal):
    "Antepone 'un' o 'una' según corresponda."
    artículo = "una" if animal[-1] == "a" else "un"
    if animal in ["serpiente", "liebre", "perdiz"]:
        artículo = "una"  #excepciones femeninas
    if animal in ["koala", "panda", "águila"]:
        artículo = "un"  #excepciones femeninas
    return artículo + " " + animal


def proponeRespuesta(hoja):
    if hoja:
        animalViejo = hoja[0]
        resp = input("El animal es %s?: " % articula(animalViejo))
        if resp in respuestaNO:
            print("Lo siento, no he vivido lo suficiente.")
            animalNuevo = input("Cuál animal era?: ")
            print("Qué pregunta harías cuya respuesta sea afirmativa")
            print("para %s y negativa para %s?" % (articula(animalNuevo), articula(animalViejo)))
            pregunta = input("El animal ... ")
            print("Gracias, aprendí la lección.")
            hoja[0] = pregunta
            hoja.extend([[animalNuevo], [animalViejo]])
        else:
            print("Ah!, lo sabía!")
    else:
        print("Hubo un error en el programa!")


def pregunta(cuestion):
    if cuestion:
        if len(cuestion) == 1:  # hoja
            proponeRespuesta(cuestion)
        else:
            resp = input("El animal %s?: " % cuestion[0])
            if resp in respuestaNO:
                pregunta(cuestion[2])
            else:
                pregunta(cuestion[1])


def main():
    arch = sys.argv[1] if len(sys.argv) > 1 else "animal.db"
    raiz = leeArchivo(arch)
    if not raiz:
        raiz = ["oso"]
    print("Piensa en un animal...")
    de_nuevo = True
    while de_nuevo:
        pregunta(raiz)
        resp = input("Juegas de nuevo?:")
        de_nuevo = not (resp in respuestaNO)
    f = open(arch, "w")
    f.write(str(raiz))
    f.close()


if __name__ == '__main__':
    main()
