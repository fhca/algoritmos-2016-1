# Notas de computabilidad.


En un congreso internacional de matemáticas el matemático _Hilbert_ enunció 23 famosos problemas no resueltos hasta ese entonces.

Entre ellos se contaba con la pregunta que hasta ese momento sólo había sido formulada de manera filosófica de la completez de las matemáticas.

Esto es, dado un conjunto de axiomas, con este y las técnicas de toda la matemática conocida hasta entonces, era posible demostrar cualquier nuevo resultado?

Algún tiempo después _Goedel_ respondió a la pregunta de manera negativa, demostrando formalmente que un sistema axiomático si es consistente no puede ser completo y su consistencia no puede ser demostrada dentro del sistema.

Esto vino a revolucionar la forma de pensar a las matemáticas, base de todas las así llamadas "ciencias puras", ya que implicaba que habrían resultados ciertos pero que no se podrían demostrar.

Siguiendo estos resultados, _Alan Turing_ trabajó en la idea de la *máquina automática*, actualmente llamada __máquina de Turing__.

Esta consiste en una _cinta_ que se extiende de manera infinita hacia la izquierda y hacia la derecha, dividida transversalmente en _celdas_ o _cuadros_, en cada celda se puede escribir un solo _símbolo_ dentro de un _alfabeto_ finito de símbolos `S`.

La cinta es recorrida por una cabeza que _lee_ y puede _modificar_ el símbolo en cada celda, basándose en una _tabla finita de reglas o tuplas_ divididas en una serie de _estados_ en los que la máquina puede _caer_. 

La cabeza puede recibir las instrucciones `I` o `D`, para _moverse_ exactamente una casilla a la izquierda o a la derecha respectivamente. Una variación es usar `N`, para _no moverse_.

Cada estado describe las posibles _acciones_ a realizar por la cabeza, de encontrarse en la celda actual con alguno de los símbolos del alfabeto.

Dentro del alfabeto se encuentra el símbolo `b`, llamado _blanco_ que es con el que inicialmente se encuentran pobladas todas las celdas de la cinta (a veces en vez de `b` usaremos `0`).

Dentro de los estados, hay uno que es el _primero_ y otro especial llamado `H` (del inglés *halt* = *detenerse*)

El símbolo blanco es el único que se permite repetirlo de manera infinita en la cinta.

La cinta puede comenzar vacía (sólo blancos), o con cierta _información inicial_ y la cabeza se sitúa por lo general en el elemento no blanco de más a la izquierda, de existir.

Las tuplas se dividen en cinco campos que originalmente representan en orden: _Estado actual_, _Valor leído_, _Valor a escribir_, _Movimiento_ y _Estado siguiente_.

Un ejemplo (_el castor ocupado_) es el siguiente: la cinta empieza vacía (todas las celdas en blanco), el alfabeto es `{0,1} ; (b=0)` y las tuplas son `(A,0,1,D,B); (A,1,1,I,C); (B,0,1,I,A); (B,1,1,D,B); (C,0,1,I,B); (C,1,1,D,H)`. Esta construye un conjunto (finito) de números uno, y luego de detiene.

_Ejercicios, deducir que hacen las tuplas anteriores; escribir máquinas de Turing que escriban `n` números `1` consecutivos, para `n=1,2,…,10`._

_Pregunta: puede una máquina de Turing almacenar información?_

Algo que observó Turing es que en la cinta de su máquina podía representar las reglas mismas, codificando en dicha cinta una máquina de Turing completa, con lo cual inventó el concepto de programa almacenado. (esto sería lo que ahora llamamos _programa_ o _app_)

Con esto, ideó el concepto de __máquina universal de Turing__, las cuales son máquinas normales de Turing pero cuya entrada (programa almacenado) es otra máquina de Turing. Este es el principio de las computadoras actuales.

Alan Turing inventó su máquina para demostrar que existen problemas que *no son computables*, es decir, que no tienen una solución _sistemática_ o _algorítmica_ diríamos actualmente.

Esto lo logró con ayuda de las máquinas universales, probando que el problema de demostrar que __siempre se puede detectar que una máquina de Turing se detiene__, es no computable. (problema __HALT__)

Para ello definió `H(M,I)` como la máquina de Turing universal que tenía las entradas `M` e `I`, que devolvía `si`, si la máquina de Turing `M` ejecutada con la entrada `I` terminaba, y devolvía `no`, si `M` no terminaba.

Luego definió otra máquina universal de Turing `H'(M)` cuya única entrada era la máquina `M` y su resultado era `si` en caso de que `H(M,M)` devolviera `no`, y devolvía un ciclo infinito (no terminaba) en caso de que `H(M,M)` devolviera `si`.

Tomó entonces `H'(H')`, que es también una máquina de Turing, pero su misma existencia es una contradicción,  pues no puede dar ningún valor. Esto demuestra que la hipótesis de que existía una máquina de Turing `H`, no es cierta.

A continuación veremos algunos ejemplos de "programas" que se pueden generar para la máquina de Turing.

En los siguientes ejemplos la cabeza empieza en el `1` más a la izquierda, y el alfabeto es `{0,1}`...

    Ej. Rebota entre dos posiciones (ciclo infinito): 
    Entrada=(1)
    Tuplas: A00IA, A11DA

    Ej. Recorre la serie de unos de la entrada de izq a der y de der a izq
    Entrada=(1111111)
    Tuplas: A00IB, A11DA, B00DA, B11IB

    Ej. Escribir 10101010101…
    Entrada=(0)  "cinta vacía"
    Tuplas: A01DB, B00DA

    Ej. Escribir 110110110…
    Entrada=(0)
    Tuplas: 
