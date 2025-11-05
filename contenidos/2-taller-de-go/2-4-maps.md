---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Mapas

Podemos pensar a los mapas como una generalización de los arreglos, donde en lugar de usar sólo enteros como índices, podemos usar otros tipos. Por ejemplo podemos acceder a un elemento de un mapa usando una cadena como índice `edades["alice"]`{l=go} en lugar de un entero como `edades[0]`{l=go}.

Los mapas son una forma de asociar claves a valores, y son útiles para almacenar datos que se pueden identificar mediante una clave. Por ejemplo, en el caso de `edades`{l=go}, la clave es el nombre de una persona y el valor es su edad.

En Go, un `map`{l=go} es una referencia a una tabla hash[^1], y el tipo de `map`{l=go} se escribe como `map[K]V`{l=go}, donde `K`{l=go} y `V`{l=go} son los tipos de sus claves y valores. Todas las claves en un mapa dado son del mismo tipo, y todos los valores son del mismo tipo, pero las claves no necesitan ser del mismo tipo que los valores.

```{important}
**El tipo de clave `K`{l=go} se debe poder comparar usando `==`{l=go}**, para que el mapa pueda verificar si una clave ya está presente o no.
```

No hay restricciones sobre el tipo de valor `V`{l=go}.

Los mapas son dinámicos es decir que pueden crecer o disminuir su tamaño a medida que se agregan o eliminan elementos.

La función _built-in_ `make`{l=go} se puede usar para reservar la memoria que usará un mapa:

```go
edades := make(map[string]int)
```

También podemos crear un _mapa literal_ para crear un nuevo mapa con algunos pares clave/valor iniciales:

```go
edades := map[string]int{
    "alice": 31,
    "charlie": 34,
}
```

Esto es equivalente a

```go
edades := make(map[string]int)
edades["alice"] = 31
edades["charlie"] = 34
```

Una expresión alternativa para un nuevo mapa vacío es `map[string]int{}`{l=go}.

Los elementos de un mapa se acceden mediante la notación habitual de subíndice:

```go
edades["alice"] = 32
edad := edades["alice"]
fmt.Println(edad)
```

```output
32
```

y se pueden eliminar con la función _built-in_ `delete`{l=go}:

```go
delete(edades, "alice")
```

Todas estas operaciones son seguras incluso si el elemento no está en el mapa; una búsqueda en un mapa utilizando una clave que no está presente devuelve el _valor cero_ para su tipo. Por ejemplo, lo siguiente funciona incluso cuando `"bob"`{l=go} aún no es una clave en el mapa porque el valor de `edades["bob"]`{l=go} será `0`{l=go}.

```go
edades["bob"] = edades["bob"] + 1
```

Las formas abreviadas de asignación `x += y`{l=go} y `x++`{l=go} también funcionan para los elementos de un mapa, por lo que podemos reescribir la declaración anterior como

```go
edades["bob"] += 1
```

o incluso de forma más concisa como

```go
edades["bob"]++
```

Para enumerar todos los pares clave/valor en el mapa, usamos un bucle `for`{l=go} basado en `range`{l=go}, similar a los que vimos para _slices_. Las iteraciones sucesivas del bucle hacen que las variables `name`{l=go} y `age`{l=go} se configuren con el siguiente par clave/valor:

```go
for name, age := range edades {
    fmt.Printf("%s\t%d\n", name, age)
}
```

```output
charlie  34
bob      3
```

Los mapas en Go no están ordenados y si mostramos todos los pares claves/valor almacenados es posible que el orden se modifique de una ejecución a la siguiente. Esto es intencional; hacer que la secuencia varíe ayuda a forzar que los programas sean robustos entre implementaciones.

Para enumerar los pares clave/valor en orden, debemos ordenar las claves explícitamente, por ejemplo, usando la función `sort`{l=go} del paquete `String`{l=go}:

```go
import "sort"

var names []string

for name := range edades {
    names = append(names, name)
}

sort.Strings(names)

for _, name := range names {
    fmt.Printf("%s\t%d\n", name, edades[name])
}
```

```output
bob      3
charlie  34
```

Dado que conocemos el tamaño final de `names`{l=go} desde el principio, es más eficiente asignar un array con el tamaño requerido de antemano. La siguiente declaración crea un _slice_ que inicialmente está vacío pero tiene la capacidad suficiente para contener todas las claves del mapa `edades`{l=go}:

```go
names := make([]string, 0, len(edades))
```

En el primer bucle `range`{l=go} mencionado anteriormente, solo necesitamos las claves del mapa `edades`{l=go}, por lo que omitimos la segunda variable del bucle. En el segundo bucle, solo necesitamos los elementos del _slice_ `names`{l=go}, por lo que usamos el identificador en blanco `_`{l=go} para ignorar la primera variable, el índice.

El _valor cero_ para un tipo mapa es `nil`{l=go}, es decir nulo. En otras palabras el mapa no tiene memoria asignada y no se puede usar. Un mapa `nil`{l=go} es diferente de un mapa vacío, que es un mapa que tiene memoria asignada pero no tiene claves.

```go
var edades map[string]int
fmt.Println(edades == nil)
fmt.Println(len(edades) == 0)
```

```output
true
true
```

La mayoría de las operaciones sobre mapas, incluyendo la recuperación, `delete`{l=go}, `len`{l=go} y los bucles `range`{l=go}, son seguras de realizar en un mapa `nil`{l=go}, ya que se comporta como un mapa vacío. Sin embargo, almacenar en un mapa `nil`{l=go} provoca un error:

```go
edades["carol"] = 21
```

```output
panic: assignment to entry in nil map
```

Antes de poder almacenar valores, se debe asignar memoria al mapa.

**Acceder a un elemento de un mapa mediante subíndices siempre devuelve un valor**. Si la clave está presente en el mapa, obtendrás el valor correspondiente; si no, obtendrás el _valor cero_ para el tipo del elemento, como vimos con `edades["bob"]`{l=go}.

Para muchos propósitos, eso está bien, pero a veces necesitas saber si el elemento realmente estaba allí o no. Por ejemplo, si el tipo del elemento es numérico, podrías necesitar distinguir entre un elemento inexistente y un elemento que casualmente tiene el _valor cero_, utilizando una prueba como esta:

```go
age, ok := edades["bob"]
if !ok { /* "bob" no es una clave en este mapa; age == 0. */ }
```

Es muy común el siguiente patrón que combina las dos sentencias anteriores dentro de la condición del `if`{l=go}, asignación y comparación en una sola línea:

```go
if age, ok := edades["bob"]; !ok { /* ... */ }
```

Utilizar un subíndice en un mapa en este contexto produce dos valores; el segundo es un booleano que indica si el elemento está presente. La variable booleana a menudo se llama `ok`{l=go}, especialmente si se usa inmediatamente en una condición `if`{l=go}.

Al igual que con los _slices_, **los mapas no se pueden comparar entre sí**; la única comparación legal es con `nil`{l=go}. Para verificar si dos mapas contienen las mismas claves y los mismos valores asociados, debemos escribir un bucle.

```go
x := map[string]int{"a": 1}
y := map[string]int{"a": 1}
fmt.Println(x == y)
```

```output
invalid operation: x == y (map can only be compared to nil)
```

## Ejercicios

1. Escribir una función `ContarPalabras`{l=go} que cuente las palabras en un string y devuelva un mapa que mapee las palabras a su número de ocurrencias. La función `Split`{l=go} del paquete `strings`{l=go} puede ser útil.
2. Escribir una función que compare dos mapas de cadenas y devuelva `true`{l=go} si los mapas contienen las mismas claves y los mismos valores. Usa el siguiente prototipo: `func Igual(x, y map[string]int) bool`{l=go}.
3. Los anagramas son palabras que tienen las mismas letras pero en un orden diferente. Escribir una función `Anagramas`{l=go} que tome dos strings y devuelva `true` si son anagramas. Usa el siguiente prototipo: `func Anagramas(s1, s2 string) bool`{l=go}. La complejidad del algoritmo debe ser $O(n)$, donde n es la longitud de los strings.

## Links recomendados

- [Effective Go](https://golang.org/doc/effective_go.html#maps){target="\_blank"}
- [Go by Example: Maps](https://gobyexample.com/maps){target="\_blank"}
- [The Go Programming Language Specification: Map types](https://golang.org/ref/spec#Map_types){target="\_blank"}

[^1]: Durante el curso veremos qué es y como funciona una tabla de hash.
