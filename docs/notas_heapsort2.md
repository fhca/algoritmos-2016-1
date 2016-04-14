# Uso de la estructura de montículos para una implementación de *colas de prioridad*

Una *cola de prioridad* es una estructura para implementar un conjunto S, cuyos elementos tienen asociada una *llave*.
Como en los montículos, hay *colas de prioridad de máximos* y *de mínimos*.
Veamos la de máximos, ya que la de mínimos es análoga.
El uso más importante de las colas de prioridad es en el scheduler o programador de tareas de un sistema operativo.
Con él se agregan procesos a ser trabajados por el procesador, se eliminan si ya se ejecutaron, pero siempre se está
ejecutando el de máxima prioridad al momento.

Nota: aquí la llave es simplemente el valor del elemento en el arreglo, por supuesto que estos algoritmos se pueden
implementar para que incluyan otros campos en cada elemento del arreglo, siempre y cuando cada elemento incluya un campo
llave a revisar.

Una cola de prioridad de máximos debe implementar:

    inserta(S, x)
    máximo(S)
    extrae_max(S)
    incrementa_llave(S, x, k)

máximo(S), que muestra el elemento con llave máxima en tiempo O(1), se puede implementar de la siguiente manera:

    máximo(A):
        devuelve A[raiz]

extrae_max(S) elimina el elemento con máxima llave, es similar al heapsort visto. Nota que usamos mont_max() ya visto. 
Recuerde que tam(A) es el índice más grande del montículo. O(lg n).

    extrae_max(A):
        si tam(A) < 0
            error: "montículo vacío"
        max = A[raiz]
        A[raiz] = A[tam(A)]
        tam(A) --
        mont_max(A, raiz)
        regresa max

incrementa_llave(S, x, k) le cambia el valor de la llave del elemento x al valor k (que debe ser más grande que el valor actual de la llave de x).
Dado que la nueva llave se incrementa, no afecta a su descendencia, pero si podría ascender en la jerarquía, por lo que hay que arreglar desde i hasta la raiz.
O(lg n).

    incrementa_llave(A, i, llave):
        si llave < A[i]
            error: "la nueva llave no debe ser menor que la antigua"
        A[i] = llave
        mientras i > raiz y A[padre(i)] < A[i]
            intercambia A[i] con A[padre(i)]
            i = padre(i)

Ahora si podemos agregar el algoritmo para inserta(S, x), primero agregándolo como última hoja (de hecho como último 
elemento del arreglo) y con llave menos infinito, a fin de corregir esta a su valor correcto con el algoritmo anterior.
O(lg n)

    inserta(A, llave):
        tam(A) ++
        A[tam(A)] = -infinito
        incrementa_llave(A, tam(A), llave)

Así podemos implementar las operaciones de colas de prioridad con tiempo O(lg n).
 