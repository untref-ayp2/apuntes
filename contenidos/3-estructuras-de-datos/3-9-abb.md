---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Árboles Binarios de Búsqueda

:::{Admonition} Definición de Árbol Binario de Búsqueda
Un árbol binario de búsqueda es un árbol binario que cumple con las siguientes propiedades para cada nodo N:

- Todos los nodos en el subárbol izquierdo de N tienen valores menores que el valor de N.
- Todos los nodos en el subárbol derecho de N tienen valores mayores que el valor de N.
- Ambos subárboles (izquierdo y derecho) deben ser también árboles binarios de búsqueda.
:::

En la siguiente figura se muestran dos árboles binarios, el de la izquierda cumple con la propiedad de ABB y por lo tanto es un árbol binario de búsqueda, mientras que el de la derecha no cumple con la propiedad ya que el nodo 8 es mayor que el 7 que se encuentra en la raíz del árbol y por lo tanto no se cumple que los todos los nodos del subárbol izquierdo son menores que la raíz. 

El subárbol de la izquierda cuya raíz es 2 si es ABB y el de la derecha cuya raiz es 9 también es ABB, sin embargo el árbol completo no es un ABB.

```{figure} ../assets/images/ABB.svg
---
name: abb
---
```
El recorrido inorden de un árbol binario de búsqueda produce una secuencia ordenada de los valores almacenados en el árbol. Esto se debe a que al visitar el subárbol izquierdo, el nodo raíz y luego el subárbol derecho, se garantiza que los nodos se procesen en orden ascendente. 

Por ejemplo en la siguiente figura se muestran dos árboles binarios de búsqueda que tienen el mismo recorrido inorden: 1, 2, 3, 5, 7, 9. Los árboles son diferentes porque los elementos se insertaron en diferente orden, sin embargo al ser un ABB el recorrido inorden es el mismo.

```{figure} ../assets/images/ABBInorden.svg
---
name: abbinorden
---
Dos árboles binarios de búsqueda con el mismo recorrido inorden
```

## Operaciones en un árbol binario de búsqueda

Las operaciones más comunes en un árbol binario de búsqueda son:
- **Inserción**: Agregar un nuevo nodo al árbol manteniendo la propiedad de ABB.
- **Búsqueda**: Encontrar un nodo en el árbol.
- **Eliminación**: Quitar un nodo del árbol manteniendo la propiedad de ABB.

### Inserción

La inserción en un árbol binario de búsqueda se realiza de manera recursiva. Se compara el valor a insertar con el valor del nodo actual y se decide si ir al subárbol izquierdo o derecho. Si el subárbol correspondiente está vacío, se inserta el nuevo nodo.

Para insertar un nuevo nodo en un árbol binario de búsqueda, se sigue el siguiente algoritmo:
```{code-block} 
---
caption: Algoritmo de inserción en un árbol binario de búsqueda
linenos:
---
FUNCION InsertarABB(raiz, valor)
  SI raiz ES nula ENTONCES
    raiz ← CrearNodo(valor)
  SINO SI valor < raiz.valor ENTONCES
    raiz.izquierdo ← InsertarABB(raiz.izquierdo, valor)
  SINO SI valor > raiz.valor ENTONCES
    raiz.derecho ← InsertarABB(raiz.derecho, valor)
  FIN SI
  RETORNAR raiz
FIN FUNCION
```
En la siguiente animación se observa la inserción del valor 6 en un árbol binario de búsqueda.

```{figure} ../assets/videos/insercionABB.mp4
---
name: insercionABB
---
Inserción de un nodo en un árbol binario de búsqueda (botón derecho del mouse- Mostrar todos los controles)
```

1. Se compara el valor 6 con la raíz (7) y como 6 es menor se va al subárbol izquierdo.
2. Se compara el valor 6 con la raíz (2) del subárbol izquierdo y como 6 es mayor se va al subárbol derecho.
3. Se compara el valor 6 con la raíz (5) del subárbol derecho y como 6 es mayor se va al subárbol derecho.
4. Como el subárbol derecho de (5) es nulo se inserta el nodo 6 como hijo derecho de (5).
   
## Búsqueda

La búsqueda en un árbol binario de búsqueda también se realiza de manera recursiva. Se compara el valor buscado con el valor del nodo actual y se decide si ir al subárbol izquierdo o derecho. Si el valor es igual al del nodo actual, se ha encontrado el nodo, si en cambio se llega a un nodo nulo, el valor no está en el árbol.

```{code-block}
---
caption: Algoritmo de búsqueda en un árbol binario de búsqueda
linenos:
---
FUNCION BuscarABB(raiz, valor)
  SI raiz ES nula ENTONCES
    RETORNAR nula
  SINO SI raiz.valor = valor ENTONCES
    RETORNAR raiz
  SINO SI valor < raiz.valor ENTONCES
    RETORNAR BuscarABB(raiz.izquierdo, valor)
  SINO
    RETORNAR BuscarABB(raiz.derecho, valor)
  FIN SI
FIN FUNCION
```

En la siguiente animación se observa la búsqueda del valor 4 que no se encuentra.

```{figure} ../assets/videos/busquedaABB.mp4
---
name: busquedaABB
---
Búsqueda de un nodo en un árbol binario de búsqueda (botón derecho del mouse- Mostrar todos los controles)
```

## Eliminación

La eliminación de un nodo en un árbol binario de búsqueda es un poco más compleja que la inserción y la búsqueda. Existen tres casos a considerar:

El nodo a eliminar es una hoja (no tiene hijos)
: En este caso, simplemente se elimina el nodo. En el ejemplo se elimina la hoja (6).)

```{figure} ../assets/images/ABBEliminacion-1.svg
---
name: eliminacion1
---
Eliminación de un nodo hoja
```

El nodo a eliminar tiene un solo hijo
: En este caso, se reemplaza reemplaza el nodo a eliminar por su hijo. Esto se hace actualizando el puntero del padre del nodo a eliminar para que apunte al hijo del nodo a eliminar. En el ejemplo se elimina el nodo (5) que tiene sólo un hijo izquierdo (3) y se reemplaza por su hijo.

```{figure} ../assets/images/ABBEliminacion-2.svg
---
name: eliminacion2
---
Eliminación de un nodo con un solo hijo
```

El nodo a eliminar tiene dos hijos
: En este caso, se busca el nodo más pequeño en el subárbol derecho del nodo a eliminar (sucesor) o el nodo más grande en el subárbol izquierdo (predecesor). Luego, se reemplaza el valor del nodo a eliminar por el valor del sucesor o predecesor y se elimina el sucesor o predecesor (que siempre va a ser una hoja o a lo sumo va tener un sólo hijo).

En la siguiente figura se observa la eliminación de la raíz del árbol, el nodo 7.

```{figure} ../assets/images/ABBEliminacion-3.svg
---
name: eliminacion3
---
Eliminación de un nodo con dos hijos
```

Para ubicar al predecesor (es decir el mayor elemento del subárbol izquierdo), se debe bajar al subárbol izquierdo y luego seguir bajando por las ramas derechas hasta llegar a un nodo que no tenga hijo derecho. En este caso el predecesor es (6). 

En cambio para ubicar al sucesor (es decir el menor elemento del subárbol derecho), se debe bajar al subárbol derecho y luego seguir bajando por las ramas izquierdas hasta llegar a un nodo que no tenga hijo izquierdo. En este caso el sucesor es (9). 

En el ejemplo se eligió reemplazar la raíz con el predecesor y eliminar el nodo (6).

```{important}
Cuando se elimina un nodo con dos hijos, el nodo no se elimina directamente, sino que se reemplaza por su predecesor o sucesor. Esto asegura mantener la estructura del ABB
```

A continuación se presenta el algoritmo de eliminación de un nodo en un árbol binario de búsqueda:

```{code-block}
---
caption: Algoritmo de eliminación en un árbol binario de búsqueda
linenos: 
---
FUNCION EliminarABB(raiz, valor)
  SI raiz ES nula ENTONCES
    RETORNAR nula
  // Buscar el nodo a eliminar
  SINO SI valor < raiz.valor ENTONCES
    raiz.izquierdo ← EliminarABB(raiz.izquierdo, valor)
  SINO SI valor > raiz.valor ENTONCES
    raiz.derecho ← EliminarABB(raiz.derecho, valor)
  SINO // Nodo encontrado
    // Caso 1: Nodo a eliminar es una hoja
    SI raiz.izquierdo ES nula Y raiz.derecho ES nula ENTONCES
      RETORNAR nula
    // Caso 2: Nodo a eliminar tiene un solo hijo
    SINO SI raiz.izquierdo ES nula ENTONCES
      RETORNAR raiz.derecho
    SINO SI raiz.derecho ES nula ENTONCES
      RETORNAR raiz.izquierdo
    // Caso 3: Nodo a eliminar tiene dos hijos
    SINO
      predecesor ← BuscarMaximo(raiz.izquierdo) // busca el mayor del subárbol izquierdo
      raiz.valor ← predecesor.valor
      raiz.izquierdo ← EliminarABB(raiz.izquierdo, predecesor.valor) // elimina el predecesor
    FIN SI
  FIN SI
  RETORNAR raiz
FIN FUNCION
```

```{code-block}
---
caption: Algoritmo de búsqueda del nodo máximo en un árbol binario de búsqueda
linenos:
---
FUNCION BuscarMaximo(raiz)
  SI raiz.derecho ES nula ENTONCES
    RETORNAR raiz
  SINO
    RETORNAR BuscarMaximo(raiz.derecho)
  FIN SI
FIN FUNCION
```

## Orden de las operaciones

En un árbol binario de búsqueda, las operaciones de inserción, búsqueda y eliminación tienen un tiempo de ejecución que depende de la altura del árbol. Por lo tanto es importante tratar de mantener el árbol equilibrado para que la altura no crezca demasiado.

Un árbol binario de búsqueda equilibrado tiene una altura aproximada de $O(log n)$, donde $n$ es el número de nodos en el árbol. En este caso, las operaciones de inserción, búsqueda y eliminación tienen un tiempo de ejecución promedio de $O(log n)$.

En la siguiente figura se observa un árbol binario de búsqueda equilibrado y completamente balanceado, donde cada nodo tiene dos hijos y la altura del árbol es mínima. En este caso, el árbol tiene una altura de 3 y contiene 15 nodos.

```{figure} ../assets/images/ABBBalanceado.svg
---
name: arbolbalanceado
---
Árbol binario de búsqueda equilibrado
```

Sin embargo, en el peor de los casos, un árbol binario de búsqueda puede degenerar en una lista enlazada, lo que resulta en una altura de $O(n)$ y un tiempo de ejecución de $O(n)$ para las operaciones. Esto ocurre cuando los nodos se insertan en orden ascendente o descendente, lo que provoca que el árbol se convierta en una estructura lineal. En la siguiente figura se observa un árbol binario de búsqueda degenerado, donde cada nodo tiene solo un hijo. En este caso, el árbol tiene una altura de 6 y contiene 7 nodos.

```{figure} ../assets/images/ABBDegenerado.svg
---
name: ABBDegenerado
---
Árbol binario de búsqueda degenerado
```

