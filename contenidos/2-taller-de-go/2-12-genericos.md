---
label: genericos
---

# Tipos parametrizables (genéricos)

En capítulos anteriores trabajamos con funciones y tipos concretos: una función que suma enteros suma solo enteros, una que ordena _strings_ ordena solo _strings_. Si queríamos la misma lógica para otro tipo, teníamos que reescribir la función. En este capítulo vamos a ver cómo escribir código que funcione para cualquier tipo usando **tipos parametrizables** (genéricos).

## El problema: lógica repetida para cada tipo

Supongamos que queremos una función que busque un elemento en un slice. Para enteros haríamos:

```{code-block} go
---
linenos:
---
func ContieneInt(arr []int, elem int) bool {
    for _, v := range arr {
        if v == elem {
            return true
        }
    }
    return false
}
```

Si después necesitamos lo mismo para _strings_, escribimos otra función casi idéntica:

```{code-block} go
---
linenos:
---
func ContieneString(arr []string, elem string) bool {
    for _, v := range arr {
        if v == elem {
            return true
        }
    }
    return false
}
```

La única diferencia es el tipo de los parámetros. El resto del código es exactamente igual. Esto viola el principio de no repetirse (DRY, por su sigla en inglés *Don't Repeat Yourself*; [Wikipedia](https://es.wikipedia.org/wiki/No_te_repitas)) y hace que el código sea más difícil de mantener.

```{admonition} Nota
---
class: note
---
Este problema de código repetido es el mismo que motiva el uso de plantillas (_templates_) en C++ o _generics_ en Java.
```

### Solución clásica: `interface{}`

Antes de que Go tuviera genéricos, la solución era usar el tipo vacío `interface{}` (que también puede escribirse como `any`). Como `interface{}` no impone ningún método, cualquier valor lo satisface:

```{code-block} go
---
linenos:
---
func ContieneAny(arr []interface{}, elem interface{}) bool {
    for _, v := range arr {
        if v == elem {
            return true
        }
    }
    return false
}
```

Pero esta solución tiene problemas:

- **Sin verificación en compilación**: si se intentan hacer operaciones como sumar dos valores de tipo `any`, el código compila pero falla en ejecución. El compilador no ayuda a encontrar el error.
- **Código verboso**: para usar el valor hay que preguntar por su tipo concreto con `valor.(Tipo)`, y si el tipo no coincide, el programa explota con un *panic*.
- **Pérdida de información**: adentro del `interface{}` el compilador no sabe si hay un `int`, un `string` o lo que sea.

```{code-block} go
---
linenos:
---
func main() {
    nums := []interface{}{10, 20, 30}
    fmt.Println(ContieneAny(nums, 20))    // true, funciona bien
    fmt.Println(ContieneAny(nums, "hola")) // false, compila pero no tiene sentido
}
```

```output
true
false
```

El problema es que el compilador no nos protege: pasar un `string` donde debería ir un `int` no genera ningún error en compilación. Si la función hiciera operaciones aritméticas, el error aparecería recién en ejecución.

## Tipos parametrizables (_type parameters_)

Desde Go 1.18, podemos escribir funciones que acepten cualquier tipo usando tipos parametrizables. La sintaxis usa corchetes `[]`:

```{code-block} go
---
linenos:
---
func Contiene[T comparable](arr []T, elem T) bool {
    for _, v := range arr {
        if v == elem {
            return true
        }
    }
    return false
}
```

Analicemos la sintaxis:

- `[T comparable]` declara un tipo parametrizable `T` con la *restricción* (_constraint_) `comparable`.
- `T` se usa como tipo de los parámetros `arr` (slice de `T`) y `elem` (`T`).
- Dentro de la función, los valores son del tipo concreto `T`, no `interface{}`..

La restricción `comparable` indica que `T` debe soportar los operadores `==` y `!=`, que son los que usamos dentro de la función.

Al llamar a la función, Go infiere el tipo automáticamente:

```{code-block} go
---
linenos:
---
func main() {
    numeros := []int{10, 20, 30, 40, 50}
    fmt.Println(Contiene(numeros, 30))   // true
    fmt.Println(Contiene(numeros, 99))   // false

    nombres := []string{"Ana", "Luis", "Pepe"}
    fmt.Println(Contiene(nombres, "Luis")) // true
}
```

```output
true
false
true
```

La misma función `Contiene` funciona con `int`, `string`, y cualquier otro tipo que sea comparable. Go genera el código necesario para cada tipo concreto en tiempo de compilación, sin penalidad en ejecución.

A diferencia de la solución con `interface{}`, acá el compilador no permite mezclar tipos:
si declaramos un slice de enteros, solo podemos buscar enteros dentro de él:

```{code-block} go
---
linenos:
---
func main() {
    numeros := []int{10, 20, 30}
    fmt.Println(Contiene(numeros, 20))    // bien: int con int

    // Esto NO compila:
    // fmt.Println(Contiene(numeros, "hola")) // error: string no es int
}
```

El error en compilación nos protege de equivocarnos antes de ejecutar el programa.

### Inferencia de tipos

Al llamar a una función genérica, el compilador deduce los tipos parametrizables a partir de los argumentos:

```{code-block} go
---
linenos:
---
Contiene(numeros, 30)   // T se infiere como int
Contiene(nombres, "Luis") // T se infiere como string
```

También podemos especificar el tipo explícitamente si hace falta:

```{code-block} go
---
linenos:
---
Contiene[int](numeros, 30)
```

```{figure} ../_static/figures/2-taller-de-go/2-12-genericos/generics_light.svg
---
class: only-light-mode
width: 80%
---
Los tipos parametrizables permiten que una misma función trabaje con diferentes tipos concretos.
```

```{figure} ../_static/figures/2-taller-de-go/2-12-genericos/generics_dark.svg
---
class: only-dark-mode
width: 80%
---
Los tipos parametrizables permiten que una misma función trabaje con diferentes tipos concretos.
```

## Restricciones (_constraints_)

Los _constraints_ definen qué operaciones puede hacer `T` dentro de la función. Go provee algunos _constraints_ predefinidos y permite crear los nuestros.

### `any`

`any` es un alias para `interface{}`. Acepta cualquier tipo, pero no permite ninguna operación específica sobre los valores (no se puede usar `==`, `<`, `+`, etc.):

```{code-block} go
---
linenos:
---
func Imprimir[T any](arr []T) {
    for _, v := range arr {
        fmt.Println(v)
    }
}
```

Esta función solo puede usar operaciones válidas para cualquier tipo: asignar, pasar como parámetro, imprimir con `fmt.Println` (que usa `interface{}` internamente).

### `comparable`

`comparable` restringe `T` a tipos que soporten `==` y `!=`. Todos los tipos básicos (enteros, _strings_, booleanos) son comparables, así como punteros, _structs_ con campos comparables y arreglos.

```{code-block} go
---
linenos:
---
func BuscarLineal[T comparable](arr []T, elem T) int {
    for i, v := range arr {
        if v == elem {
            return i
        }
    }
    return -1
}
```

### Restricciones personalizadas (_custom constraints_)

Para operaciones como `<`, `>`, `<=`, `>=`, no existe un _constraint_ predefinido en la biblioteca estándar (hasta Go 1.21). Podemos definir el nuestro propio:

```{code-block} go
---
linenos:
---
type Ordenable interface {
    ~int | ~float64 | ~string
}
```

El operador `~` indica que el tipo subyacente debe ser `int`, `float64` o `string`. Esto permite usar tanto los tipos literales (`int`, `string`) como tipos definidos a partir de ellos (por ejemplo, `type Edad int`).

Ahora podemos escribir funciones que usen operadores de comparación:

```{code-block} go
---
linenos:
---
func Maximo[T Ordenable](arr []T) T {
    max := arr[0]
    for _, v := range arr[1:] {
        if v > max {
            max = v
        }
    }
    return max
}

func main() {
    enteros := []int{10, 5, 8, 3, 12}
    fmt.Println(Maximo(enteros)) // 12

    alturas := []float64{1.75, 1.80, 1.65, 1.90}
    fmt.Println(Maximo(alturas)) // 1.9

    nombres := []string{"Ana", "Luis", "Pepe", "Beatriz"}
    fmt.Println(Maximo(nombres)) // Pepe (orden lexicográfico)
}
```

```output
12
1.9
Pepe
```

```{admonition} Importante
---
class: important
---
Los _constraints_ con uniones de tipos (`~int | ~float64 | ~string`) solo pueden definirse como interfaces en el contexto de un tipo parametrizable. No pueden usarse como tipos de variables regulares.
```

## Alternativa: función comparadora

En lugar de definir un _constraint_ personalizado, podemos pasar una función que compare elementos. Acá el tipo es `[T any]` porque no hacemos operaciones directamente sobre `T`: toda la lógica de comparación está dentro de la función `menor`, que recibe los `T` y decide el orden.

```{code-block} go
---
linenos:
---
func OrdenarSeleccion[T any](arr []T, menor func(T, T) bool) {
    n := len(arr)
    for i := 0; i < n-1; i++ {
        minIdx := i
        for j := i + 1; j < n; j++ {
            if menor(arr[j], arr[minIdx]) {
                minIdx = j
            }
        }
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    }
}

func main() {
    numeros := []int{4, 2, 7, 1, 9}
    OrdenarSeleccion(numeros, func(a, b int) bool { return a < b })
    fmt.Println(numeros) // [1 2 4 7 9]

    nombres := []string{"Pepe", "Ana", "Luis"}
    OrdenarSeleccion(nombres, func(a, b string) bool { return a < b })
    fmt.Println(nombres) // [Ana Luis Pepe]
}
```

```output
[1 2 4 7 9]
[Ana Luis Pepe]
```

La función `menor` recibe dos elementos `T` y devuelve `true` si el primero debe ir antes que el segundo. Esto nos permite ordenar cualquier tipo, incluso _structs_ sin un orden natural:

```{code-block} go
---
linenos:
---
type Persona struct {
    Nombre string
    Edad   int
}

func main() {
    personas := []Persona{
        {"Ana", 30},
        {"Luis", 25},
        {"Pepe", 35},
    }

    OrdenarSeleccion(personas, func(a, b Persona) bool {
        return a.Edad < b.Edad
    })

    fmt.Println(personas) // [{Luis 25} {Ana 30} {Pepe 35}]
}
```

```output
[{Luis 25} {Ana 30} {Pepe 35}]
```

## Tipos genéricos

Los tipos parametrizables también funcionan con _structs_. Esto permite definir contenedores que almacenen valores de cualquier tipo:

```{code-block} go
---
linenos:
---
type Caja[T any] struct {
    valor T
}

func (c *Caja[T]) Set(valor T) {
    c.valor = valor
}

func (c *Caja[T]) Get() T {
    return c.valor
}

func main() {
    cajaInt := Caja[int]{}
    cajaInt.Set(42)
    fmt.Println(cajaInt.Get()) // 42

    cajaStr := Caja[string]{valor: "hola"}
    fmt.Println(cajaStr.Get()) // hola
}
```

```output
42
hola
```

Un tipo genérico también puede tener múltiples parámetros:

```{code-block} go
---
linenos:
---
type Dicc[K comparable, V any] struct {
    datos map[K]V
}

func NuevoDicc[K comparable, V any]() *Dicc[K, V] {
    return &Dicc[K, V]{datos: make(map[K]V)}
}

func (d *Dicc[K, V]) Set(clave K, valor V) {
    d.datos[clave] = valor
}

func (d *Dicc[K, V]) Get(clave K) (V, bool) {
    v, ok := d.datos[clave]
    return v, ok
}
```

## Resumen

| Concepto                 | Sintaxis                               | Ejemplo                                               |
| ------------------------ | -------------------------------------- | ----------------------------------------------------- |
| Parámetro de tipo        | `[T any]`                              | `func Imprimir[T any](arr []T)`                       |
| Constraint `comparable`  | `[T comparable]`                       | `func Contiene[T comparable](arr []T, elem T) bool`   |
| Constraint personalizado | `type X interface { ~int \| ~string }` | `func Maximo[T Ordenable](arr []T) T`                 |
| Función comparadora      | Parámetro `func(T, T) bool`            | `func Ordenar[T any](arr []T, menor func(T, T) bool)` |
| Struct genérico          | `type Nombre[T any] struct { ... }`    | `type Caja[T any] struct { valor T }`                 |
| Múltiples parámetros     | `[K comparable, V any]`                | `type Dicc[K comparable, V any] struct { ... }`       |

## Ejercicios

Los ejercicios de este capítulo están en `12-genericos/ejercicios/`
del repositorio taller-go.
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.
