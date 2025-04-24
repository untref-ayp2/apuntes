---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Árboles

Un árbol de datos es una estructura jerárquica compuesta por nodos interconectados mediante aristas. Se caracteriza por tener un único nodo **raíz**, en la cima de la jerarquía, del cual pueden descender cero o más nodos hijos. Los árboles son herramientas fundamentales para modelar relaciones jerárquicas, como la organización de sistemas de archivos, la estructura de directorios o las dependencias entre objetos.

En todo árbol, la **raíz** se distingue por carecer de nodo padre. El resto de los nodos poseen un único padre y pueden tener múltiples (o ningún) hijo. Aquellos nodos sin descendientes se denominan **hojas**. Los nodos que no son hojas ni la raíz se conocen como **nodos internos**. 


Una propiedad esencial de los árboles es la existencia de un único camino que conecta la raíz con cada una de las hojas.

Consideremos el árbol genérico ilustrado: el nodo $A$ representa la **raíz**, mientras que $D$, $C$, $N$ y $K$ son las **hojas** y los nodos $R$ y $Z$ son **nodos internos**.

```{figure} ../assets/images/Arbol.svg
---
name: arbol
---
Árbol de datos
```

## Propiedades de los árboles

Altura
: La altura de un árbol es la longitud del camino más largo desde la raíz hasta una hoja. En el caso de un árbol vacío, la altura se define como $-1$.

Profundidad
: La profundidad de un nodo es la longitud del camino desde la raíz hasta ese nodo. La profundidad de la raíz es $0$.

Nivel
: El nivel de un nodo es la profundidad del nodo más uno. La raíz se encuentra en el nivel $1$, sus hijos en el nivel $2$, y así sucesivamente.

Grado
: El grado de un nodo es el número de hijos que tiene. Un nodo hoja tiene un grado de $0$, mientras que la raíz puede tener un grado mayor o igual a $0$.

En la figura anterior, el árbol tiene una altura de 2, ya que el camino más largo desde la raíz hasta las hojas $C$, $D$ o $K$, que son las más profundas del árbol, tiene una longitud de 2. La raíz $A$ tiene un grado de 3, ya que tiene tres hijos: $R$, $N$ y $Z$, estos nodos son hermanos ya que tienen el mismo padre. El nodo $R$ tiene un grado de 2, ya que tiene dos hijos: $D$ y $C$. El nodo $C$ es una hoja, por lo que su grado es 0. La profundidad de los nodos $R$, $N$ y $Z$ es 1, ya que está a un nivel de la raíz, a su vez $N$ también es una hoja.

# Árboles binarios

Los árboles binarios son árboles donde cada nodo tiene como máximo dos hijos. Estos hijos se denominan hijo izquierdo e hijo derecho. Los árboles binarios son ampliamente utilizados en informática debido a su simplicidad y eficiencia en diversas operaciones.

```{figure} ../assets/images/ArbolBinario.svg
---
name: ArbolBinario
---
Árbol Binario
```
:::{card} Definición de Árbol Binario
Un árbol binario es por definición:

- Un árbol vacío, o
- Un nodo raíz con un hijo izquierdo y un hijo derecho, donde cada uno de estos hijos es a su vez un árbol binario.
+++
La definición recursiva de un árbol binario implica que cada subárbol también es un árbol binario. Esto permite construir árboles binarios de manera jerárquica y recursiva, lo que facilita su manipulación y análisis.
:::

## Recorridos de un árbol binario

Los **recorridos de un árbol binario** son algoritmos fundamentales para visitar y procesar cada uno de los nodos que componen la estructura, siguiendo un orden específico. Existen tres tipos principales de recorridos en profundidad: preorden, inorden y postorden.

La característica distintiva de estos recorridos radica en su naturaleza recursiva. Al aplicar un recorrido a un árbol, el mismo proceso se aplica de manera independiente a sus subárboles izquierdo y derecho. Esto asegura que cada nodo dentro de la estructura sea visitado siguiendo el patrón definido por el tipo de recorrido.

Estos métodos son esenciales en diversas aplicaciones informáticas, incluyendo la búsqueda eficiente de información, la ordenación de datos y la evaluación de expresiones aritméticas o lógicas representadas en forma de árbol. Cada tipo de recorrido ofrece una secuencia de visita única, lo que los hace adecuados para diferentes contextos y tareas.

### Preorden (Raíz - Izquierda - Derecha)

El recorrido preorden comienza visitando la raíz del árbol, seguido por la exploración recursiva del subárbol izquierdo y, finalmente, el subárbol derecho. El orden de procesamiento es, por lo tanto: nodo raíz, subárbol izquierdo, subárbol derecho.

El siguiente seudocódigo ilustra la implementación del recorrido preorden como un método dentro de un nodo de un árbol binario, delegando la lógica del recorrido a cada nodo:

```{code-block} 
---
caption: Preorden
linenos:
---
FUNCION Preorden(raiz)
  SI raiz ES nulo ENTONCES
    retornar
  FIN SI
  Procesar(raiz)  // Visitar el nodo actual
  Preorden(raiz.izquierdo)  // Recorrer el subárbol izquierdo
  Preorden(raiz.derecho)  // Recorrer el subárbol derecho
FIN FUNCION
```

`Procesar(raiz)`
: Representa una operación genérica que se aplica al nodo actual. Esta operación puede variar según la necesidad, como imprimir el valor del nodo o añadirlo a una lista.

llamadas recursivas
: Las líneas 6 y 7 realizan las llamadas recursivas para aplicar el recorrido preorden a los subárboles izquierdo y derecho del nodo actual, respectivamente.

Por ejemplo en el siguiente video se observa el recorrido preorden. Cuando el nodo se pinta de amarillo significa que se llamó a la función `preorden` con ese nodo y cuando el nodo se pinta de verde significa que el nodo fue visitado (línea 4 del seudocódigo).

```{figure} ../assets/videos/preorden.mp4
---
name: preorden
---
Recorrido en Preorden (botón derecho del mouse- Mostrar todos los controles)
```

```{math}

+ \, a \, * \, - \, b \, c \, d

```

### Inorden (Iquierda - Raíz - Derecha)

El recorrido inorden visita primero de forma recursiva todos los nodos del subárbol izquierdo, luego procesa el nodo raíz, y finalmente recorre recursivamente el subárbol derecho. La secuencia de visita es: subárbol izquierdo, nodo raíz, subárbol derecho.

El siguiente seudocódigo muestra la implementación del recorrido inorden:

```{code-block} 
---
caption: Inorden
linenos:
---
FUNCION Inorden (raiz)
  SI raiz ES nulo ENTONCES
    retornar
  FIN SI
  Inorden(raiz.izquierdo)  // Visitar el subárbol izquierdo
  Procesar(raiz)  // Visitar el nodo actual
  Inorder(raiz.derecho)  // Visitar el subárbol derecho
FIN FUNCION
```

Ejemplo de recorrido inorden:

```{figure} ../assets/videos/inorden.mp4
---
name: inorden
---
Recorrido en Inorden (botón derecho del mouse- Mostrar todos los controles)
```

```{math}

a + b - c * d

```

### Postorden (Izquierda - Derecha - Raíz)

En el recorrido postorden, se exploran recursivamente el subárbol izquierdo, seguido del subárbol derecho, y finalmente se procesa el nodo raíz. El orden de visita es: subárbol izquierdo, subárbol derecho, nodo raíz.

El seudocódigo para el recorrido postorden se presenta a continuación:

```{code-block} 
---
caption: Postorden
linenos:
---
FUNCION Postorden (raiz)
  SI raiz ES nulo ENTONCES
    retornar
  FIN SI
  Postorden(raiz.izquierdo)  // Visitar el subárbol izquierdo
  Postorden(raiz.derecho)  // Visitar el subárbol derecho
  Procesar(raiz)  // Visitar el nodo actual
FIN FUNCION
```
Ejemplo de recorrido postorden:

```{figure} ../assets/videos/postorden.mp4
---
name: postorden
---
Recorrido en Postorden (botón derecho del mouse- Mostrar todos los controles)
```

```{math}

a \, b \, c \, - \, d \, * \, +

```

