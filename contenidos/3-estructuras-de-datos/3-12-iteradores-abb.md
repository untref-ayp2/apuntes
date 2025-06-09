---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Iteradores en Árboles Binarios de Busqueda (ABB)

En este anexo, vamos a implementar iteradores para un Árbol Binario de Búsqueda (ABB) en Go. Los iteradores nos permiten recorrer los nodos del árbol de manera ordenada, facilitando la obtención de los valores almacenados. Elegimos implementarlos sobre un ABB para aprovechar su estructura ordenada.

## Interfaz del Iterador

En el siguiente fragmento de código definimos la interfaz `Iterator` que contendrá los métodos necesarios para iterar cualquier colección de elementos y en particular los nodos de un ABB.

```{literalinclude} ../_static/code/types/types.go
:lineno-match:
:linenos:
```
Los métodos que debe implementar un iterador son los siguientes

_HasNext_
: Indica si hay un siguiente elemento en la colección. Devuelve `true` si hay más elementos por recorrer, o `false` si se ha llegado al final de la colección.

_Next_
: Devuelve el siguiente elemento de la colección. El comportamiento de Next consiste en avanzar al próximo elemento y devolverlo. Si no hay más elementos para iterar devuelve un elemento nulo y un error.

## Árbol Binario de Búsqueda (ABB)

En esta implementación de ABB la funcionalidad del árbol se encuentra en el árbol propiamente dicho y no en los nodos, con el propósito de simplificar el código y mejorar la legibilidad.

Los métodos incluidos son los mínimos y necesarios para crear un árbol, insertar elementos y obtener los distintos iteradores.

El árbol es genérico del tipo `constraints.Ordered`, lo que significa que los valores deben ser comparables y ordenables, es decir deben soportar las operaciones de comparación como `<`, `<=`, `>`, `>=`, `==` y `!=`.

A continuación se muestra la estructura del nodo del ABB.

```{literalinclude} ../_static/code/binarytree/binarynode.go
:start-at: type BinaryNode
:end-at: }
:lineno-match:
:linenos:
```

El tipo `BinaryNode` solo tiene los métodos necesarios para crear un nodo y obtener su valor. No contiene métodos para insertar o eliminar nodos, ya que toda la funcionalidad del árbol está implementada en `BinarySearchTree` directamente. 

En la implementación del ABB tenemos los métodos para obtener los iteradores: 

```{literalinclude} ../_static/code/binarytree/binarysearchtree.go
:lineno-match:
:linenos:
:emphasize-lines: 95, 101, 107
```


## Implementación de los iteradores. El Desafío de Mantener el Estado: ¿Por qué no solo recursión?

Cuando estudiamos los recorridos de árboles (inorder, preorder, postorder), la forma más intuitiva y elegante de implementarlos es usando recursión, ya que el código queda conciso, limpio y fácil de entender.

Sin embargo, cuando hablamos de un iterador, la situación cambia. Un iterador, por definición (según el patrón Iterador), debe permitirnos obtener el "siguiente" elemento de la colección a demanda, sin tener que procesar el resto de la colección de antemano. Es decir, queremos que nuestro método Next() devuelva un único valor y luego HasNext() nos diga si hay más, esperando una nueva llamada a Next().

Aquí es donde la recursión directa presenta un desafío:

Manejo del estado: 
Una función recursiva completa su ejecución y devuelve un resultado. No "pausa" su estado para ser reanudada en el mismo punto más tarde. Cada llamada recursiva crea un nuevo stack frame (marco de pila) que se destruye al finalizar.

Devolución de un solo elemento
: Si intentáramos adaptar la recursión para devolver un solo elemento en cada llamada a Next(), nos encontraríamos con que la función recursiva ya ha avanzado en el recorrido, y sería muy difícil mantener el "punto exacto" en el que nos quedamos para la siguiente llamada.

Espacio en memoria (stack overflow)
: Para árboles muy grandes o muy desbalanceados (degenerados), una implementación recursiva podría consumir una gran cantidad de memoria de la pila de llamadas, llevando a un error de stack overflow.

Para superar estos desafíos y crear un iterador que sea _lazy_ (bajo demanda) y eficiente en memoria, necesitamos una forma de simular la pila de llamadas recursiva de forma explícita. Y la estructura de datos perfecta para esto es, precisamente, una pila (stack).

```{Note}
Que sea _lazy_ significa que el iterador no calcula todos los elementos de antemano, sino que los obtiene a medida que se le solicita un nuevo elemento. Esto es fundamental para manejar colecciones grandes o infinitas sin consumir demasiada memoria.
```

### La Pila como Sustituto de la Recursión Explícita

Al usar una pila en nuestros iteradores, nosotros somos los que gestionamos el "estado" de la recursión. En lugar de que el sistema operativo maneje la pila de llamadas por nosotros, nosotros empujamos (_Push_) y sacamos (_Pop_) nodos de nuestra propia estructura de pila para recordar qué camino hemos tomado y qué nodos nos quedan por visitar.

Esta técnica nos permite:

Pausar y Reanudar
: Cuando Next() es llamado, podemos extraer el siguiente nodo a visitar de la pila, devolverlo, y luego dejar la pila en un estado que representa el "resto" del recorrido. La próxima vez que se llame Next(), la pila nos recordará dónde estábamos.

Eficiencia en Memoria
: La profundidad de la pila que necesitamos es proporcional a la altura del árbol (O(h)), no al número total de nodos (O(N)), lo que es mucho más eficiente para árboles grandes y balanceados (O(logN)).

Control Explícito
: Tenemos un control total sobre el orden en que los nodos se agregan y se eliminan de la pila, lo que es fundamental para implementar correctamente los diferentes tipos de recorridos.

## Iterador Inorder

La estrategia para el iterador inorder es la siguiente:

1. Comenzamos desde la raíz del árbol.
2. Vamos hacia la izquierda hasta llegar al nodo más a la izquierda apilando los nodos en la pila.
3. El menor elemento del árbol será el nodo más a la izquierda es el que se encuentra en el tope de la pila.
4. Cuando llamamos a Next(), sacamos el nodo del tope de la pila, chequeamos si tiene un hijo derecho. Si lo tiene, vamos a ese hijo derecho y repetimos el proceso de ir hacia la izquierda, apilando los nodos.
5. Una vez que no hay más nodos a la izquierda, el tope de la pila contendrá el siguiente nodo en orden.
6. Devolvemos el elemento del nodo que acabamos de sacar de la pila.

En el siguiente fragmento de código se puede observar la implementación del iterador Inorder

```{literalinclude} ../_static/code/binarytree/inorderIterator.go
:lineno-match:
:linenos:
```

