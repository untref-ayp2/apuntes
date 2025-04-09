---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Tablas de _Hashing_

Las tablas de _hashing_ son estructuras de datos que permiten almacenar y recuperar información de manera eficiente. Utilizan una función de _hash_ para mapear claves a posiciones en un arreglo, lo que permite acceder a los elementos en tiempo constante promedio $O(1)$. Son especialmente útiles para implementar diccionarios, conjuntos y otras estructuras de datos que requieren acceso rápido a los elementos.

Una tabla de _hashing_ generaliza el concepto de un arreglo, ya que permite acceder a cualquier posición de la tabla en tiempo constante. Podemos asi tener arreglos indexados con otros tipos de datos y no solo enteros. 

Para lograr esto, se utiliza una función de _hash_ que toma una clave y devuelve un índice en el arreglo. La función de _hash_ debe ser eficiente y distribuir uniformemente. 

En la siguiente figura se aprecia un esquema que nos permite analizar los distintos elementos involucrados en una tabla de _hashing_. 


```{figure} ../assets/images/TablaHash1.svg
---
name: tabla_hash
---
Esquema de una tabla de _hashing_.
```

Claves
: El universo de claves puede ser muy grande, o infinito. De ese conjunto solo un subconjunto se almacenará en la tabla de _hashing_. 

Valores
: El valor asociado a una clave. Puede ser cualquier tipo de dato, incluyendo estructuras de datos complejas.

Función de _hash_
: Una función que toma una clave y devuelve un índice en el arreglo. La función de _hash_ debe ser eficiente y distribuir uniformemente las claves en el arreglo.

Arreglo
: La estructura de datos subyacente que almacena los elementos, es un arreglo de _"valores"_. El tamaño del arreglo debe ser lo suficientemente grande para evitar colisiones, pero no tan grande como para desperdiciar espacio.

Colisiones
: Ocurren cuando dos claves diferentes se mapean al mismo índice en el arreglo. Las colisiones deben manejarse de manera eficiente para garantizar un rendimiento óptimo de la tabla de _hashing_.

## Claves

Las claves deben ser inmutables, es decir, no deben cambiar una vez que se han creado. Esto es importante porque la función de _hash_ se basa en el valor de la clave para calcular el índice en el arreglo. Si la clave cambia, el índice también cambiará, lo que puede provocar errores al intentar acceder a los elementos en la tabla de _hashing_.
Las claves pueden ser de cualquier tipo de dato, incluyendo enteros, cadenas de texto, estructuras de datos complejas, etc. Sin embargo, es importante que la función de _hash_ sea capaz de manejar todos los tipos de claves que se utilicen en la tabla de _hashing_.

## Colisiones

Las colisiones son un problema común en las tablas de _hashing_. Ocurren cuando dos claves diferentes se mapean al mismo índice en el arreglo. Esto puede suceder si la función de _hash_ no distribuye uniformemente las claves en el arreglo o si el tamaño del arreglo es demasiado pequeño.
Para manejar las colisiones, existen varias técnicas, entre las que se encuentran:

_Hashing_ abierto
: Con esta técnica, cuando se produce una colisión, se busca la siguiente posición libre en el arreglo para almacenar el nuevo elemento, simplemente incrementando el índice hasta encontrar una posición libre[1].

1: Otras versiones de esta técnica utilizan una función de _hash_ diferente para encontrar la siguiente posición libre, lo que se conoce como _hashing_ doble.

_Hashing_ cerrado
: Con esta técnica, el arreglo subyacente contiene una lista de elementos en cada posición. Cuando se produce una colisión, el nuevo elemento se agrega a la lista en la posición correspondiente. Esta técnica es más eficiente en términos de espacio, pero puede ser más lenta en términos de tiempo de acceso.

### _Hashing_ abierto

Cuando se produce una colisión se debe incrementar el índice en 1 hasta encontrar una posición libre. Esta técnica es simple de implementar y funciona bien en la mayoría de los casos. Sin embargo, puede ser ineficiente si hay muchas colisiones, ya que puede requerir un tiempo de búsqueda lineal en el peor de los casos. Es importante elegir una función de _hash_ que minimice las colisiones y un tamaño de arreglo que sea lo suficientemente grande para evitar colisiones.

Cuando se incrementa el índice, se debe tener en cuenta el tamaño del arreglo. Si el índice supera el tamaño del arreglo, se debe volver al principio del arreglo y continuar buscando una posición libre. Esto se conoce como _hashing_ circular.

### Inserción

En la siguiente figura se grafica la inserción de un elemento en una tabla de _hashing_ abierta.

```{figure} ../assets/images/TablaHashInsercion.svg
---
name: tabla_hash_insercion_abierta
---
Inserción en una tabla de _hash_ abierta.
```

Supongamos que vamos a insertar las claves $k_1$ y $k_2$, en ese orden, y que la posición 10 del arreglo ya se encontraba ocupada. En este caso, $f(k_1)$ devuelve el índice 9, como inicialmente la posición se encuentra vacía, se puede asociar la clave a ese índice. Luego $f(k_2)$ también devuelve 9, como la posición 9 se encuentra ocupada, intenta en la próxima, como la posición 10 ya está ocupada incrementa en forma circular el índice y finalmente puede asociar $k_2$ a la posición 0 del arreglo.

### Eliminación

La eliminación de un elemento en una tabla de _hashing_ abierta es un poco más complicada que la inserción. Cuando se elimina un elemento, se debe marcar la posición como eliminada, pero no se puede dejar la posición vacía, ya que esto podría causar problemas al buscar otros elementos en el futuro. En su lugar, se debe utilizar un marcador especial para indicar que la posición ha sido eliminada.
Esto se conoce como _marcador de eliminación_ y permite que la búsqueda continúe sin problemas. Sin embargo, esto puede aumentar el tiempo de búsqueda si hay muchos elementos eliminados en la tabla de _hashing_.

```{figure} ../assets/images/TablaHashEliminacion.svg
---
name: tabla_hash_eliminacion_abierta
---
Eliminación en una tabla de _hash_ abierta.
```
En la figura se observa que al eliminar el elemento en la posición 10, se marca la posición como eliminada, pero no se deja vacía. Esto permite que la búsqueda de otros elementos continúe sin problemas. Sin embargo, si hay muchos elementos eliminados en la tabla de _hashing_, esto puede aumentar el tiempo de búsqueda. En resumen una posición de la tabla podrá estar en algunos de los tres siguientes estados:
- Vacía
- Ocupada
- Eliminada

### Búsqueda

La búsqueda de un elemento en una tabla de _hashing_ abierta es similar a la inserción. Se utiliza la función de _hash_ para calcular el índice y luego se busca el elemento en esa posición. Si el elemento no se encuentra en la posición calculada, se incrementa el índice en 1 hasta encontrar el elemento o una posición vacía. Si se encuentra una posición eliminada, la búsqueda continua.

```{figure} ../assets/images/TablaHashBusquedaAbierta.svg
---
name: tabla_hash_busqueda_abierta
---
Búsqueda en una tabla de _hash_ abierta.
```
En la figura se observa que al buscar la clave $k_2$, se intenta con la posición 9, como la clave asociada a esa posición es $k_1$, la búsqueda continua, luego la posición 10 está eliminada, por lo que se avanza a la posición 0 donde finalmente se encuentra la clave buscada.

Supongamos que se busca una clave $k_3$ cuyo valor de _hash_ también es 9. En este caso, la búsqueda comenzaría en la posición 9, pero como la clave asociada a esa posición es $k_1$, la búsqueda continuaría hasta encontrar una posición vacía o eliminada. En este caso en la posición 1 se encuentra con una posición vacía, por lo que se concluye que la clave $k_3$ no está presente en la tabla de _hashing_.


