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

```{figure} ../assets/images/ABB.svg
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

Los recorridos de un árbol binario son técnicas utilizadas para visitar y procesar todos los nodos de un árbol en un orden específico. Existen tres tipos principales de recorridos

Preorden
: En este recorrido, se visita primero el nodo raíz, luego el subárbol izquierdo y finalmente el subárbol derecho. El orden de visita es: raíz, izquierda, derecha.

Inorden
: En este recorrido, se visita primero el subárbol izquierdo, luego el nodo raíz y finalmente el subárbol derecho. El orden de visita es: izquierda, raíz, derecha.

Postorden
: En este recorrido, se visita primero el subárbol izquierdo, luego el subárbol derecho y finalmente el nodo raíz. El orden de visita es: izquierda, derecha, raíz.

Los subárboles se visitan de forma recursiva, es decir, se aplica el mismo recorrido a cada subárbol. Esto significa que cada subárbol se trata como un árbol binario independiente y se recorren sus nodos siguiendo el mismo patrón de recorrido.

Los recorridos de un árbol binario son útiles para diversas aplicaciones, como la búsqueda, la ordenación y la evaluación de expresiones. Cada tipo de recorrido tiene sus propias características y se utiliza en diferentes contextos.

Por ejemplo, para el árbol binario de la figura anterior, los recorridos serían:
- Preorden: $+ \, a \, * \, - \, b \, c \, d$
- Inorden: $a + b - c * d$
- Postorden: $a \, b \, c \, - \, d \, * \, +$