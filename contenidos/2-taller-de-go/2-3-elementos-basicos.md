---
label: elementos-basicos
---

# Elementos básicos

## Tipos de datos básicos

Go ofrece un conjunto de tipos de datos básicos (o primitivos) que cubren la mayoría de las necesidades.

| Categoría         | Tipos                                         | Descripción                                  |
| ----------------- | --------------------------------------------- | -------------------------------------------- |
| Booleanos         | `bool`                                        | `true` o `false`                             |
| Cadenas           | `string`                                      | Texto Unicode inmutable                      |
| Enteros con signo | `int`, `int8`, `int16`, `int32`, `int64`      | Tamaño fijo según el sufijo                  |
| Enteros sin signo | `uint`, `uint8`, `uint16`, `uint32`, `uint64` | Solo valores positivos                       |
| Punto flotante    | `float32`, `float64`                          | Números decimales                            |
| Complejos         | `complex64`, `complex128`                     | Números complejos                            |
| _Alias_           | `byte` (= `uint8`), `rune` (= `int32`)        | Para trabajar con bytes y caracteres Unicode |

Los tipos `int` y `uint` tienen un tamaño que depende de la arquitectura del sistema: 32 bits en sistemas de 32 bits y 64 bits en sistemas de 64 bits.

```{code-block} go
---
linenos:
---
var activo bool = true
var nombre string = "Algoritmos"
var edad int = 20
var altura float64 = 1.75
var letra byte = 'A'
var simbolo rune = '±'
```

Go es un lenguaje de **tipado estático**, lo que significa que el tipo de cada variable se conoce al momento de compilar y no puede cambiar durante la ejecución.

```{code-block} go
---
linenos:
---
var x int = 10
x = "hola" // ERROR de compilación
```

## Variables

### Declaración con `var`

La forma más explícita de declarar una variable es con la palabra clave `var`, seguida del nombre y el tipo:

```{code-block} go
---
linenos:
---
var edad int
var precio float64
var nombre string
var activo bool
```

Si no se asigna un valor inicial, la variable toma el **valor cero** de su tipo:

| Tipo                   | Valor cero          |
| ---------------------- | ------------------- |
| `int`, `float64`, etc. | `0`                 |
| `string`               | `""` (cadena vacía) |
| `bool`                 | `false`             |

```{code-block} go
---
linenos:
---
var edad int       // edad == 0
var nombre string  // nombre == ""
var activo bool    // activo == false
```

### Declaración con inicialización

Se puede declarar y asignar un valor inicial en la misma línea:

```{code-block} go
---
linenos:
---
var edad int = 25
var nombre string = "Martín"
```

Cuando el tipo se puede inferir del valor, se puede omitir:

```{code-block} go
---
linenos:
---
var edad = 25       // int
var nombre = "Martín" // string
var precio = 29.99  // float64
```

### Declaración corta `:=`

Dentro de una función, Go ofrece una sintaxis abreviada con `:=` que declara la variable e infiere el tipo automáticamente:

```{code-block} go
---
linenos:
---
func main() {
    edad := 25
    nombre := "Martín"
    precio := 29.99
}
```

`:=` no se puede usar fuera de funciones (a nivel de paquete no hay una instrucción que ejecutar).

### Declaración múltiple

Se pueden declarar varias variables en una misma línea:

```{code-block} go
---
linenos:
---
var x, y int = 10, 20
var nombre, apellido string = "Juana", "García"
a, b := 1, "dos"
```

O en un bloque:

```{code-block} go
---
linenos:
---
var (
    nombre   string = "Martín"
    edad     int    = 25
    activo   bool   = true
)
```

### Asignación vs. declaración

Una vez declarada, una variable se actualiza con `=` (sin `:`):

```{code-block} go
---
linenos:
---
edad := 25
edad = 26 // ok
edad := 27 // ERROR: ya fue declarada
```

Para asignar nuevos valores a múltiples variables se puede usar:

```{code-block} go
---
linenos:
---
x, y := 1, 2
x, y = y, x // intercambia los valores
```

## Constantes

Las constantes se declaran con `const` y, a diferencia de las variables, no se pueden modificar después de su declaración.

```{code-block} go
---
linenos:
---
const Pi = 3.1416
const Mensaje string = "Hola"
```

Al igual que con `var`, se pueden agrupar en bloques:

```{code-block} go
---
linenos:
---
const (
    StatusOK   = 200
    Status404  = 404
    Status500  = 500
)
```

Las constantes pueden ser **sin tipo** (sin especificar el tipo explícitamente) o **con tipo**:

```{code-block} go
---
linenos:
---
const n = 500          // sin tipo
const s string = "abc" // con tipo
```

Las constantes sin tipo tienen más flexibilidad: se pueden usar en contextos que esperan tipos compatibles. Por ejemplo, una constante numérica sin tipo se puede usar tanto con `int` como con `float64`:

```{code-block} go
---
linenos:
---
const n = 500
var entero int = n       // ok
var flotante float64 = n // ok
```

```{code-block} go
---
linenos:
---
func main() {
    const nombre = "Go"
    const anio = 2009

    fmt.Println(nombre, anio)

    // anio = 2010 // ERROR: las constantes no se pueden modificar
}
```

## Condicionales

### `if` / `else`

Go utiliza `if` y `else` de forma similar a C o Java, pero sin paréntesis alrededor de la condición:

```{code-block} go
---
linenos:
---
if edad >= 18 {
    fmt.Println("Mayor de edad")
} else {
    fmt.Println("Menor de edad")
}
```

Se pueden encadenar varios `else if`:

```{code-block} go
---
linenos:
---
if nota >= 8 {
    fmt.Println("Promocionado")
} else if nota >= 4 {
    fmt.Println("Regular")
} else {
    fmt.Println("Libre")
}
```

### `if` con inicialización

Go permite ejecutar una instrucción antes de la condición, separada por punto y coma. La variable declarada en esa inicialización solo existe dentro del bloque del `if`:

```{code-block} go
---
linenos:
---
if err := procesar(); err != nil {
    fmt.Println("Error:", err)
}
```

### Operadores de comparación y lógicos

Go tiene los operadores habituales: `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&` (y), `||` (o), `!` (no).

```{code-block} go
---
linenos:
---
if edad >= 18 && tienePermiso {
    fmt.Println("Acceso permitido")
}
```

### `switch`

El `switch` en Go tiene algunas diferencias importantes con Java:

1. No necesita `break` — cada `case` termina automáticamente al finalizar su bloque
2. Se pueden agrupar varios valores en un mismo `case`
3. Se puede usar sin expresión (como un `if` encadenado)

```{code-block} go
---
linenos:
---
switch dia := time.Now().Weekday(); dia {
case time.Saturday, time.Sunday:
    fmt.Println("Fin de semana")
default:
    fmt.Println("Día laborable")
}
```

```{code-block} go
---
linenos:
---
hora := 15
switch {
case hora < 12:
    fmt.Println("Buenos días")
case hora < 19:
    fmt.Println("Buenas tardes")
default:
    fmt.Println("Buenas noches")
}
```

### `fallthrough`

Si se quiere continuar al siguiente `case` (como en C), se usa la palabra clave `fallthrough`:

```{code-block} go
---
linenos:
---
switch n := 1; n {
case 1:
    fmt.Println("uno")
    fallthrough
case 2:
    fmt.Println("dos")
}
// Imprime "uno" y luego "dos"
```

## Ciclos

Go tiene una sola palabra clave para iterar: `for`. No tiene `while` ni `do-while`, pero el mismo `for` puede usarse de distintas formas para cubrir todos los casos.

### For clásico

Similar a C o Java: inicialización, condición, incremento.

```{code-block} go
---
linenos:
---
for i := 0; i < 10; i++ {
    fmt.Println(i)
}
```

Las variables declaradas en la inicialización (`i := 0`) solo existen dentro del bloque del `for`.

### For como `while`

Si se omite la inicialización y el incremento, queda solo la condición, comportándose como un `while`:

```{code-block} go
---
linenos:
---
i := 0
for i < 10 {
    fmt.Println(i)
    i++
}
```

### For infinito

Si se omite también la condición, el ciclo se ejecuta indefinidamente. Se sale con `break`:

```{code-block} go
---
linenos:
---
i := 0
for {
    if i >= 10 {
        break
    }
    fmt.Println(i)
    i++
}
```

### `range`

Go provee la palabra clave `range` para iterar sobre estructuras de datos como arreglos, *slices*, *strings*, mapas o canales. `range` devuelve dos valores: el índice y el elemento.

```{code-block} go
---
linenos:
---
numeros := []int{10, 20, 30, 40, 50}
for indice, valor := range numeros {
    fmt.Printf("posición %d = %d\n", indice, valor)
}
```

Si solo interesa el valor, se puede ignorar el índice con `_`:

```{code-block} go
---
linenos:
---
for _, valor := range numeros {
    fmt.Println(valor)
}
```

También se puede iterar sobre un `string`, en cuyo caso `range` itera por runas (caracteres Unicode), no por bytes:

```{code-block} go
---
linenos:
---
for posicion, letra := range "Algoritmos" {
    fmt.Printf("%c ", letra)
}
```

### `break` y `continue`

- `break`: sale del ciclo inmediatamente
- `continue`: salta a la siguiente iteración

```{code-block} go
---
linenos:
---
for i := 0; i < 10; i++ {
    if i%2 == 0 {
        continue // salta los pares
    }
    if i > 7 {
        break // termina al llegar a 7
    }
    fmt.Println(i)
}
// Imprime: 1 3 5 7
```

## Ejercicios

Los ejercicios de este capítulo están en `03-elementos-basicos/ejercicios/`
del repositorio taller-go.
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.
