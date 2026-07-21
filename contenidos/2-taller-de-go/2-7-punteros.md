---
label: punteros
---

# Punteros

## ¿Qué es un puntero?

Un puntero es una variable que almacena una **dirección de memoria** de otra variable. En vez de contener un valor directamente, contiene la ubicación donde ese valor está guardado.

En Go, cada tipo `T` tiene un tipo puntero asociado `*T`, que es un puntero a un valor de tipo `T`. Por ejemplo, `*int` es un puntero a un entero, `*float64` es un puntero a un número de punto flotante, y `*Persona` es un puntero a una variable de tipo `Persona`.

El tipo del puntero no es solo una formalidad: el compilador necesita saber a qué tipo apunta para poder leer e interpretar correctamente los bytes en esa dirección. Un `*int` sabe que debe leer 8 bytes (en una arquitectura de 64 bits) e interpretarlos como un entero con signo, mientras que un `*float64` también lee 8 bytes pero los interpreta como un número de punto flotante. Un `*byte` lee un solo byte. Si el puntero no tuviera esta información, el compilador no podría generar el código correcto para acceder al valor.

Cuando asignamos una variable a otra en Go, se copia el contenido. Esto vale para `int`, `float64`, `string`, `struct`, arreglos, etc. Para lograr el mismo efecto que las referencias en Java (compartir el acceso a un mismo valor sin copiarlo), Go usa punteros de forma explícita.

## Operadores `&` y `*`

Trabajar con punteros implica dos operadores fundamentales:

`&` (dirección de)
: Devuelve la dirección de memoria de una variable.

`*` (desreferencia)
: Accede al valor almacenado en la dirección que contiene el puntero. Si se usa en una declaración de tipo, indica que es un tipo puntero (ej: `*int`).

Veamos un ejemplo concreto:

```{code-block} go
---
linenos:
---
import "fmt"

var a int = 7          // a es una variable int con valor 7
var pa *int = &a       // pa es un puntero a int que guarda la dirección de a

fmt.Printf("La variable a se encuentra en la dirección %p y su valor es %d\n", &a, a)
fmt.Printf("pa contiene la dirección %p\n", pa)
fmt.Printf("Si desreferenciamos pa con *pa obtenemos %d\n", *pa)
```

```output
La variable a se encuentra en la dirección 0xc00052a000 y su valor es 7
pa contiene la dirección 0xc00052a000
Si desreferenciamos pa con *pa obtenemos 7
```

Acá ocurre lo siguiente:

1. Declaramos una variable `a` de tipo `int` con valor `7`.
2. Declaramos `pa` de tipo `*int` (puntero a `int`) y le asignamos `&a`, es decir, la dirección de memoria donde vive `a`.
3. Al imprimir `pa` vemos la dirección hexadecimal `0xc00052a000`.
4. Al imprimir `*pa` **desreferenciamos** el puntero: seguimos la flecha hasta la dirección y obtenemos el valor que hay allí, que es `7`.

El operador `*` también permite **modificar** el valor apuntado:

```{code-block} go
---
linenos:
---
*pa = 99                      // Cambiamos el valor en la dirección apuntada
fmt.Printf("a ahora vale %d (se modificó a través de *pa)\n", a)
```

```output
a ahora vale 99 (se modificó a través de *pa)
```

Al hacer `*pa = 99` estamos yendo a la dirección que contiene `pa` y escribiendo `99` ahí. Como esa dirección es la de `a`, la variable `a` también cambió.

```{admonition} No confundir el operador * con el tipo *T
---
class: warning
---
En la declaración `var pa *int`, el asterisco forma parte del tipo (`*int` significa "puntero a int"). En cambio, en `*pa` el asterisco es el operador de desreferencia que accede al valor apuntado. El contexto determina el significado.
```

## Diagrama en memoria

La siguiente figura muestra cómo se relacionan las variables `pa` y `a` en memoria:

```{figure} ../_static/figures/2-taller-de-go/2-7-punteros/puntero-direccion_light.svg
---
class: only-light-mode
width: 90%
---
Variables `pa` y `a` en memoria.
```

```{figure} ../_static/figures/2-taller-de-go/2-7-punteros/puntero-direccion_dark.svg
---
class: only-dark-mode
width: 90%
---
Variables `pa` y `a` en memoria.
```

`pa` contiene la dirección `0xc00052a000`. Al desreferenciar con `*pa` obtenemos el valor `7`. Toda modificación a través de `*pa` impacta directamente en `a`.

## Pasar parámetros por referencia

En el capítulo de funciones vimos que los argumentos en Go siempre se pasan por valor: la función recibe una copia. Esto hace que el siguiente código no funcione como cabría esperar:

```{code-block} go
---
linenos:
---
func duplicar(x int) {
    x = x * 2
}

a := 5
duplicar(a)
fmt.Println(a)
```

```output
5
```

`duplicar` recibe una **copia** de `a`, por más que la variable se llame igual. Modificar `x` dentro de la función no afecta a la variable original.

Para modificar el original, necesitamos un puntero:

```{code-block} go
---
linenos:
---
func duplicar(x *int) {
    *x = *x * 2
}

a := 5
duplicar(&a)
fmt.Println(a)
```

```output
10
```

Ahora:

1. `duplicar` recibe `&a`, la dirección de `a`.
2. Dentro de la función, `x` es un `*int` que apunta a `a`.
3. `*x = *x * 2` desreferencia `x`, multiplica el valor por 2 y lo guarda en la misma dirección.
4. Al volver, `a` vale `10`.

```{admonition} ¿Por qué no pasar siempre punteros?
---
class: note
---
Los punteros son útiles cuando necesitamos cambiar un valor desde otra función. Sin embargo, si solo necesitamos leer el valor, pasar una copia suele ser más seguro (evita efectos secundarios) y no necesariamente más lento. Go puede optimizar ciertos casos.
```

## Puntero `nil`

El valor cero de un puntero es `nil`. Un puntero `nil` es aquel que no tiene una dirección de memoria válida a la cual apuntar; no está inicializado o se le asignó `nil` explícitamente. Si intentamos desreferenciar un puntero `nil` con `*p`, el programa entra en pánico porque no hay una dirección de memoria válida de la cual leer:

```{code-block} go
---
linenos:
---
var p *int
fmt.Println(p)
```

```output
<nil>
```

```{code-block} go
---
linenos:
---
p = nil
fmt.Println(*p) // panic!
```

```output
panic: runtime error: invalid memory address or nil pointer dereference
```

Siempre debemos verificar que un puntero no sea `nil` antes de desreferenciarlo:

```{code-block} go
---
linenos:
---
if p != nil {
    fmt.Println(*p)
} else {
    fmt.Println("puntero nulo, no se puede desreferenciar")
}
```

```output
puntero nulo, no se puede desreferenciar
```

## Manipular arreglos con punteros

Un arreglo en Go se pasa por valor: pasarlo a una función copia todos sus elementos. Para evitarlo, podemos pasar un puntero al arreglo:

```{code-block} go
---
linenos:
---
func duplicarElementos(arr *[4]int) {
    for i := range arr {
        arr[i] *= 2
    }
}

nums := [4]int{1, 2, 3, 4}
duplicarElementos(&nums)
fmt.Println(nums)
```

```output
[2 4 6 8]
```

Dentro del cuerpo de la función, Go nos permite escribir `arr[i]` directamente sobre un puntero a arreglo, sin necesidad de `(*arr)[i]`. Se trata de **azúcar sintáctico**[^syntactic-sugar] (o *syntactic sugar* en inglés): una forma más cómoda de escribir lo mismo.

````{admonition} Relación con slices
---
class: tip
---
En la práctica, en lugar de pasar `*[N]T` se suele usar `[]T` (un slice). El slice ya contiene internamente un puntero al arreglo subyacente, como vimos en el capítulo de arreglos y slices. De hecho, lo siguiente es equivalente al ejemplo anterior pero usando slices:

```{code-block} go
:linenos:
func duplicarElementos(arr []int) {
    for i := range arr {
        arr[i] *= 2
    }
}

nums := []int{1, 2, 3, 4}
duplicarElementos(nums)
fmt.Println(nums)
```

```output
[2 4 6 8]
```

La diferencia es que cuando usamos `[]int`, el slice ya maneja internamente la contigüidad en memoria del arreglo subyacente, la longitud y la capacidad. Al pasar un slice no necesitamos usar `&` para obtener la dirección; el puntero al arreglo subyacente viaja dentro del slice.

````

## Funciones que devuelven punteros

En Go es perfectamente válido que una función devuelva la dirección de una variable local:

```{code-block} go
---
linenos:
---
func nuevoContador(valorInicial int) *int {
    c := valorInicial
    return &c
}

contador := nuevoContador(42)
fmt.Println(*contador)

*contador++
fmt.Println(*contador)
```

```output
42
43
```

A simple vista parece peligroso: `c` es una variable local de `nuevoContador`, ¿no se destruye al salir de la función? Go resuelve esto mediante el *escape analysis* (análisis de escape). El compilador detecta que la dirección de `c` escapa del ámbito de la función, y automáticamente asigna `c` en el *heap* en vez del *stack*. Esto se cubrió en el capítulo de gestión de memoria.

## Ejercicios

Los ejercicios de este capítulo están en `07-punteros/ejercicios/`
del repositorio taller-go.
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.

[^syntactic-sugar]: **Azúcar sintáctico** es una construcción de un lenguaje de programación que no agrega poder expresivo (es decir, se puede expresar de otra forma), pero hace que el código sea más legible y fácil de escribir. En este caso, `arr[i]` sobre un puntero es azúcar sintáctico porque internamente el compilador lo traduce a `(*arr)[i]`.
