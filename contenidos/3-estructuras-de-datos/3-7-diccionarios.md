---
file_format: mystnb
kernelspec:
    name: gophernotes
---

# Diccionarios

Los diccionarios son una estructura de datos que permiten almacenar pares de elementos `(clave, valor)`. La clave es un valor único que nos permite identificar al valor asociado. Los diccionarios se pueden implementar sobre distintas estructuras de datos como tablas de hash y árboles, entre otros.

Podemos pensar a los diccionarios como una guía telefónica, donde el nombre de la persona es la clave y el número de teléfono es el valor asociado y podemos buscar rapidamente un número utilizando un índice para no tener que recorrer toda la guía telefónica.

```{figure} ../assets/images/Diccionario.svg
---
width: 300px
name: diccionario
---
Guía telefónica
```

Cada implementación tiene sus propias características y ventajas, sin embargo, en general, los diccionarios son estructuras de datos eficientes para la búsqueda y recuperación de valores asociados a una clave.

Otra forma de pensar a los diccionarios es como una generalización de los arreglos, donde en lugar de utilizar índices enteros para acceder a los elementos, utilizamos claves de cualquier tipo.

Los diccionarios tienen muchísimas aplicaciones en la vida cotidiana y en la programación, por ejemplo, en la implementación de bases de datos, en la implementación de sistemas de cache, en la implementación de sistemas de búsqueda, entre otros.

## Conjunto de claves

Las claves de un diccionario tienen que ser únicas, es decir, no puede haber dos elementos con la misma clave. Si se intenta agregar un elemento con una clave que ya existe, se reemplaza el valor asociado a la clave existente por el nuevo valor, por lo tanto las claves se deben poder comparar para determinar si son iguales o no. Si además se desea que las claves estén ordenadas las claves deben soportar orden total.

## Operaciones

Los diccionarios deben soportar las siguientes operaciones:

`Put`
: Agrega el par (clave, valor) al diccionario. Si la clave ya existe, se reemplaza el valor asociado a la clave existente por el nuevo valor.

`Get`
: Devuelve el valor asociado a la clave.

`Size`
: Devuelve la cantidad de elementos en el diccionario.

`Exist`
: Determina si una clave existe en el diccionario.

`Remove`
: Elimina el par (clave, valor) del diccionario.

`Keys`
: Devuelve una lista con todas las claves del diccionario.

`Values`
: Devuelve una lista con todos los valores del diccionario.

Cómo se mencionó anteriormente, el orden de las operaciones puede variar dependiendo de la implementación del diccionario.

A continuación el orden esperado en una implementación de diccionario sobre tabla de hash:

:::{table} Orden de las Operaciones
:width: 40%
:align: center

| Operación | Orden  |
| :-------: | :----: |
|   `Put`   | $O(1)$ |
|   `Get`   | $O(1)$ |
|  `Size`   | $O(1)$ |
|  `Exits`  | $O(1)$ |
| `Remove`  | $O(1)$ |
|  `Keys`   | $O(n)$ |
| `Values`  | $O(n)$ |

:::

## Implementación en Go

En Go, los diccionarios se pueden implementar usando el tipo de dato `map`. Un `map` es una colección de pares clave-valor, donde las claves son únicas y los valores pueden ser de cualquier tipo. La sintaxis para declarar un `map` es la siguiente:

```go
var m map[TipoClave]TipoValor
```

Donde `TipoClave` es el tipo de dato de la clave y `TipoValor` es el tipo de dato del valor. Por ejemplo, para declarar un `map` que asocie nombres de personas con sus edades, podemos hacer lo siguiente:

```go
var edades map[string]int
```

En este caso, la clave es de tipo `string` y el valor es de tipo `int`. Para inicializar un `map` se puede utilizar la función `make`:

```go
edades = make(map[string]int)
```

Para agregar un par clave-valor al `map` se puede hacer de la siguiente manera:

```go
edades["Juan"] = 25
```

Para obtener el valor asociado a una clave se puede hacer de la siguiente manera:

```go
fmt.Println(edades["Juan"])
```

Para eliminar un par clave-valor se puede hacer de la siguiente manera:

```go
delete(edades, "Juan")
```

Para verificar si una clave existe en el `map` se puede hacer de la siguiente manera:

```go
if _, ok := edades["Juan"]; ok {
    fmt.Println("La clave existe")
} else {
    fmt.Println("La clave no existe")
}
```

Para recorrer un `map` se puede hacer de la siguiente manera:

```go
for clave, valor := range edades {
    fmt.Println(clave, valor)
}
```

## Ejercicios

1. Implementar un diccionario sobre una tabla de _hashing_ genérica, como la vista en la clase anterior

2. Analizar el orden de todas las operaciones
