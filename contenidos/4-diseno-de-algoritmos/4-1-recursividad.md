---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Recursividad

La recursividad es una técnica que permite subdividir el problema original en subproblemas más pequeños, luego resuelve los subproblemas y finalmente combina las soluciones parciales de cada unos de los subrpoblemas para obtener la solución del problema original. Cada subproblema a su vez se vuelve a subdividir en subproblemas aún más pequeños, y así sucesivamente, hasta llegar a un caso base cuya solución es trivial o fácil de obtener.

No todos los problemas se pueden resolver de manera recursiva, pero aquellos que sí, suelen ser más fáciles de entender y de implementar. La recursividad o recursión también permite buscar la solución de problemas complejos resolviendo subproblemas más simples.

La siguiente figura es sólo a modo de graficar la recursión


```{figure} ../assets/images/Recursion.svg
---
width: 300px
name: recursion
---
Imagen Recursiva
```

En la práctica podemos identificar una función recursiva porque dentro del cuerpo de la misma se llama a sí misma.

Para que la recursión funcione es necesario estructurar el código en:

Caso base
: Es el caso más simple y trivial que se puede resolver directamente sin necesidad de subdividir el problema en subproblemas más pequeños. La recursión debe llegar a este caso para poder terminar. Si no hay un caso base que corte la recursión, la función se llamará a sí misma indefinidamente y se producirá un error de desbordamiento de pila.

Caso recursivo
: Es el caso en el que se resuelve un subproblema más pequeño y se combina la solución parcial con la solución de los subproblemas más pequeños. Las llamadas recursivas deben acercarse al caso base en cada iteración para que la recursión termine, en caso contrario, si el tamaño de los datos no disminuye en cada iteración, la recursión no terminará.

Como ejemplo podemos reescribir el algoritmo de la búsqueda binaria que ya vimos para hacerlo recursivo

:::{code-block} GO
:linenos:
:emphasize-lines: 16, 17, 18, 23, 27

/**
 * Búsqueda binaria en un arreglo ordenado para encontrar un elemento específico.
 * La búsqueda se realiza entre las posiciones ini y fin del arreglo
 *
 * @param array Un arreglo de enteros ordenado de forma ascendente.
 * @param inicio El índice inicial del rango en el que se realizará la búsqueda.
 * @param fin El índice final del rango en el que se realizará la búsqueda.
 * @param x El valor que se desea buscar en el arreglo.
 * @return El índice del elemento encontrado en el arreglo,
 * o -1 si el elemento no está presente.
 *
 * La función utiliza un enfoque recursivo para dividir el rango de búsqueda en mitades,
 * comparando el valor buscado con el elemento en el índice medio del rango actual.
 */
func busquedaBinaria(array []int, inicio int, fin int, x int) int {
  if inicio > fin {
	  return -1
	}

	medio := (inicio + fin) / 2

	if array[medio] > x {
		return busquedaBinaria(array, inicio, medio-1, x) 
	}

	if array[medio] < x {
		return busquedaBinaria(array, medio+1, fin, x)
	}

	return medio
}
:::

En este caso, la función `busquedaBinaria` se llama a sí misma dos veces, una vez para buscar en la mitad izquierda del rango y otra vez para buscar en la mitad derecha del rango. La función se llama recursivamente hasta que el elemento buscado se encuentra en el arreglo o hasta que el rango de búsqueda se reduce a cero (es decir se ejecuta el caso base). De las dos llamadas recursivas, solo una de ellas se ejecutará en cada iteración, dependiendo de si el elemento buscado es menor o mayor que el elemento en el índice medio del rango actual.

Se pueden identificar claramente el caso base y los casos recursivos en la función. El caso base es cuando `inicio` es mayor que `fin` (línea 16, 17 y 18). Casos recursivos (líneas 23 y 27) donde la función se llama nuevamente con un rango más pequeño.

## Tipos de recursividad

La recursividad, de acuerdo a como las funciones se llaman a sí misma, se puede ser clasificar en dos tipos:

Recursión directa
: Es la forma más común de recursión, donde una función se llama a sí misma directamente.

Recursión indirecta
: En este caso, dos o más funciones se llaman entre sí de forma cíclica. Es decir, la función A llama a la función B, que a su vez llama a la función A. Este tipo de recursión es menos común y puede ser difícil de entender y depurar y así sucesivamente. Incluso puede haber más de dos funciones que se llaman mutuamente.

El ejemplo de la búsqueda binaria es un ejemplo de recursión directa, ya que la función `busquedaBinaria` se llama a sí misma directamente.

A continuación se muestra un ejemplo de recursión indirecta, donde dos funciones se llaman entre sí de forma cíclica. Las funciones son capaces de determinar si el entero dado es par o impar, sin usar divisiones, resto de la división o multiplicaciones. Simplemente llegan hasta el caso base cuando `n == 0` y retornan el valor correspondiente. (Es un ejemplo didáctico, no es la forma más eficiente de determinar si un número es par o impar)

:::{code-block} GO
:linenos:
:emphasize-lines: 1, 5, 9, 12

func esPar(n int) bool {
	if n == 0 { // El 0 es par
		return true
	}
	return esImpar(n - 1)
}

func esImpar(n int) bool {
	if n == 0 { // El 0 no es impar
		return false
	}
	return esPar(n - 1)
}
:::

En este caso en la línea 5 se llama a la función `esImpar` y en la línea 12 a la función `esPar`. Cada llamada recursiva se realiza siempre con un número menor, de forma tal de acercarse al caso base cuano `n == 0`. De acuerdo si llego al caso base por la primera o la segunda función el valor de retorno será Verdadero o Falso.

## Teorema del Maestro

El cálculo del orden de las funciones recursvias puede ser complicado de realizar, ya que se trata de ecuaciones de recurrencia. Por suerte el **Teorema del Maestro** permite agilizar el cálculo a partir de la siguiente observación:

La ecuación de recurrencia de una función recursiva será:


