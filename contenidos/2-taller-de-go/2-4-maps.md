---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Mapas

<!--
Esta celda oculta nos permite usar `fmt.Println` sin necesidad de importar
"fmt", el objetivo es que no se imprima la salida que tiene `fmt.Println` ya
que devuelve la cantidad de caracteres impresos y un error.
-->

```{code-cell} go
:tags: [remove-cell]
import f "fmt"

type FmtWrapper struct{}

func (fw FmtWrapper) Println(a ...interface{}) {
    _, _ = f.Println(a...)
}

func (fw FmtWrapper) Printf(format string, a ...interface{}) {
    _, _ = f.Printf(format, a...)
}

var fmt FmtWrapper = FmtWrapper{}
```

En Go, un `map`{l=go} es una referencia a una tabla hash, y el tipo de `map`{l=go} se escribe como `map[K]V`{l=go}, donde `K`{l=go} y `V`{l=go} son los tipos de sus claves y valores. Todas las claves en un mapa dado son del mismo tipo, y todos los valores son del mismo tipo, pero las claves no necesitan ser del mismo tipo que los valores. **El tipo de clave `K`{l=go} debe ser comparable usando `==`{l=go}**, para que el mapa pueda verificar si una clave dada es igual a una ya existente. No hay restricciones sobre el tipo de valor `V`{l=go}.

La función _built-in_ `make`{l=go} se puede usar para reservar la memoria que usará un mapa:

```{code-cell} go
edades := make(map[string]int)
```

También podemos crear un _mapa literal_ para crear un nuevo mapa con algunos pares clave/valor iniciales:

```{code-cell} go
edades := map[string]int{
    "alice": 31,
    "charlie": 34,
}
```

Esto es equivalente a

```{code-cell} go
edades := make(map[string]int)
edades["alice"] = 31
edades["charlie"] = 34
```

Una expresión alternativa para un nuevo mapa vacío es `map[string]int{}`{l=go}.

Los elementos de un mapa se acceden mediante la notación habitual de subíndice:

```{code-cell} go
edades["alice"] = 32
fmt.Println(edades["alice"])
```

y se pueden eliminar con la función _built-in_ `delete`{l=go}:

```{code-cell} go
delete(edades, "alice")
```

Todas estas operaciones son seguras incluso si el elemento no está en el mapa; una búsqueda en un mapa utilizando una clave que no está presente devuelve el _valor cero_ para su tipo. Por ejemplo, lo siguiente funciona incluso cuando `"bob"`{l=go} aún no es una clave en el mapa porque el valor de `edades["bob"]`{l=go} será `0`{l=go}.

```{code-cell} go
edades["bob"] = edades["bob"] + 1
```

Las formas abreviadas de asignación `x += y`{l=go} y `x++`{l=go} también funcionan para los elementos de un mapa, por lo que podemos reescribir la declaración anterior como

```{code-cell} go
edades["bob"] += 1
```

o incluso de forma más concisa como

```{code-cell} go
edades["bob"]++
```

Pero un elemento de un mapa no es una variable, y no podemos tomar su dirección:

```{code-cell} go
:tags: [remove-output]
_ = &edades["bob"]
```

```output
invalid operation: cannot take address of edades["bob"] (map index expression of type int)
```

Una razón por la cual no podemos tomar la dirección de un elemento de un mapa es que, al crecer un mapa, podría ocurrir un rehashing de los elementos existentes hacia nuevas ubicaciones de almacenamiento, lo que potencialmente invalidaría la dirección.

Para enumerar todos los pares clave/valor en el mapa, usamos un bucle `for`{l=go} basado en `range`{l=go}, similar a los que vimos para _slices_. Las iteraciones sucesivas del bucle hacen que las variables `name`{l=go} y `age`{l=go} se configuren con el siguiente par clave/valor:

```{code-cell} go
:tags: [remove-output]
for name, age := range edades {
    fmt.Printf("%s\t%d\n", name, age)
}
```

```output
charlie  34
bob      3
```

El orden de iteración de un mapa no está especificado, y diferentes implementaciones podrían usar una función hash distinta, lo que lleva a un orden diferente. En la práctica, el orden es aleatorio y varía de una ejecución a la siguiente. Esto es intencional; hacer que la secuencia varíe ayuda a forzar que los programas sean robustos entre implementaciones. Para enumerar los pares clave/valor en orden, debemos ordenar las claves explícitamente, por ejemplo, usando la función `Strings`{l=go} del paquete `sort`{l=go} si las claves son cadenas. Este es un patrón común:

```{code-cell} go
:tags: [remove-output]
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

```{code-cell} go
names := make([]string, 0, len(edades))
```

En el primer bucle `range`{l=go} mencionado anteriormente, solo necesitamos las claves del mapa `edades`{l=go}, por lo que omitimos la segunda variable del bucle. En el segundo bucle, solo necesitamos los elementos del _slice_ `names`{l=go}, por lo que usamos el identificador en blanco `_`{l=go} para ignorar la primera variable, el índice.

El _valor cero_ para un tipo de mapa es `nil`{l=go}, es decir, una referencia a ninguna tabla hash en absoluto.

```{code-cell} go
:tags: [remove-output]
var edades map[string]int
fmt.Println(edades == nil)
fmt.Println(len(edades) == 0)
```

```output
true
true
```

La mayoría de las operaciones sobre mapas, incluyendo la recuperación, `delete`{l=go}, `len`{l=go} y los bucles `range`{l=go}, son seguras de realizar en una referencia de mapa `nil`{l=go}, ya que se comporta como un mapa vacío. Sin embargo, almacenar en un mapa `nil`{l=go} provoca un error:

```{code-cell} go
:tags: [remove-output]
edades["carol"] = 21
```

```output
panic: assignment to entry in nil map
```

Antes de poder almacenar valores, se debe asignar memoria al mapa.

**Acceder a un elemento de un mapa mediante subíndices siempre devuelve un valor**. Si la clave está presente en el mapa, obtendrás el valor correspondiente; si no, obtendrás el _valor cero_ para el tipo del elemento, como vimos con `edades["bob"]`{l=go}. Para muchos propósitos, eso está bien, pero a veces necesitas saber si el elemento realmente estaba allí o no. Por ejemplo, si el tipo del elemento es numérico, podrías necesitar distinguir entre un elemento inexistente y un elemento que casualmente tiene el _valor cero_, utilizando una prueba como esta:

```{code-cell} go
age, ok := edades["bob"]
if !ok { /* "bob" no es una clave en este mapa; age == 0. */ }
```

Es muy común este patrón que combina dos sentencias dentro de la condición del `if`{l=go}:

```{code-cell} go
if age, ok := edades["bob"]; !ok { /* ... */ }
```

Utilizar un subíndice en un mapa en este contexto produce dos valores; el segundo es un booleano que indica si el elemento está presente. La variable booleana a menudo se llama `ok`{l=go}, especialmente si se usa inmediatamente en una condición `if`{l=go}.

Al igual que con los _slices_, **los mapas no se pueden comparar entre sí**; la única comparación legal es con `nil`{l=go}. Para verificar si dos mapas contienen las mismas claves y los mismos valores asociados, debemos escribir un bucle.

## Ejercicios

1. Escribir una función `ContarPalabras`{l=go} que cuente las palabras en un string y devuelva un mapa que mapee las palabras a su número de ocurrencias. La función `Split`{l=go} del paquete `strings`{l=go} puede ser útil.
2. Escribir una función que compare dos mapas de cadenas y devuelva `true`{l=go} si los mapas contienen las mismas claves y los mismos valores. Usa el siguiente prototipo: `func Igual(x, y map[string]int) bool`{l=go}.
3. Los anagramas son palabras que tienen las mismas letras pero en un orden diferente. Escribir una función `Anagramas`{l=go} que tome dos strings y devuelva `true` si son anagramas. Usa el siguiente prototipo: `func Anagramas(s1, s2 string) bool`{l=go}. La complejidad del algoritmo debe ser $O(n)$, donde n es la longitud de los strings.

## Links recomendados

- [Effective Go](https://golang.org/doc/effective_go.html#maps)
- [Go by Example: Maps](https://gobyexample.com/maps)
- [The Go Programming Language Specification: Map types](https://golang.org/ref/spec#Map_types)
