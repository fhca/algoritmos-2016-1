Notas sobre Heapsort

(Notación: LxL = piso de x )

Un montículo se puede ver como un arreglo A de longitud len(A) en el que se cumple la propiedad de "montículo de máximos" o la de "montículo de mínimos", que se verán enseguida. El arreglo se puede pensar como un árbol binario casi completo (en su último nivel sólo le faltan, si acaso, los elementos de más a su derecha). Cómo árbol sus índices cumplen:
padre(i) = L(i-1)/2L
izq(i) = 2i+1
der(i) = 2i+2

(Nota: en el Cormen se consideran arreglos que comienzan en índice uno. Aquí utilizo índice cero, aunque podrías también desperdiciar el elemento cero y utilizar los algoritmos del libro, que son un poco más sencillos, en fin, esta es otra forma, para que tengas dos versiones y compares).

Llamaremos tam(A) a una variable que consideraremos como el último índice del montículo, es decir, en ocasiones no utilizaremos todo el arreglo.

raiz = 0 (índice del elemento raiz del árbol binario)

*Propiedad de montículo de máximos*
A[padre(i)] >= A[i]   (el padre el mayor que sus hijos, esta utilizaremos en esta explicación)

*Propiedad de montículo de mínimos*
A[padre(i)] <= A[i]  (el padre es menor que sus hijos)

altura(i) = número de aristas del camino más largo de i a una hoja descendiente
altura(A) = altura(raiz)

imax(A, i, j, k):   # devuelve el índice en el que A se hace máxima
  i,j,k <= tam(A)  # los índices están en el montículo
  devuelve el índice m tal que A[m] = max{A[i], A[j], A[k]}
  (desempates: si A[m]=A[i], devuelve i, si A[i] < A[j] = A[k], devuelve j)

mont_max(A, i): # hace cumplir la propiedad de montículo de máximos para una cadena desde i hasta una hoja descendiente
  m = imax(A, i, izq(i), der(i))
  si m != i:
    intercambia(A[i], A[m])
    mont_max(A, m)  # recursividad de cola, facil de convertir a iteración

const_mont_max(A):   #construye un montículo con el arreglo A
  tam(A) = len(A) - 1
  para i = padre(tam(A)) ... raiz
    mont_max(A, i)

heapsort(A):  # acomoda "in situ" los elementos en orden ascendiente
  const_mont_max(A)
  tam(A) = len(A) - 1
  para i = tam(A) ... 1
    intercambia(A[raiz], A[i])
    tam(A) --
    mont_max(A, raiz)
