---
label: funciones
---

# Funciones

A diferencia de Java, donde las funciones siempre pertenecen a una clase, en Go las funciones pueden ser independientes y no es necesario definirlas como métodos estáticos. Las funciones en Go son "ciudadanos de primera clase": una función es un valor que se puede almacenar en una variable, pasar como argumento o devolver como resultado de otra función.

Una función puede tomar cero o más parámetros, y puede devolver cero o más valores.

## Parámetros

### Sintaxis básica

Los parámetros se declaran con nombre y tipo, separados por coma:

```go
func sumar(x int, y int) int {
    return x + y
}
```

En este ejemplo, la función `sumar` toma dos parámetros de tipo `int` y devuelve un `int`. Cabe destacar que, a diferencia de Java, el tipo de retorno se escribe después de los paréntesis.

Si quisiéramos generar algo similar en Java deberíamos declarar una clase con métodos estáticos:

```java
public class Matemática {
    public static int sumar(int a, int b) {
        return a + b;
    }
}
```

### Parámetros del mismo tipo

Cuando dos o más parámetros consecutivos comparten el mismo tipo, podemos declarar el tipo una sola vez al final:

```go
func sumar(x, y int) int {
    return x + y
}
```

### Parámetros variádicos

Go permite definir funciones que aceptan una cantidad variable de argumentos con `...` antes del tipo. Estos se conocen como parámetros variádicos y se reciben como un _slice_ dentro de la función:

```go
func sumar(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
```

```go
import "fmt"

func main() {
    fmt.Println(sumar(1, 2, 3))
    fmt.Println(sumar(5, 10, 15, 20))
}
```

```output
6
50
```

## Pasaje por valor

En Go los argumentos siempre se pasan por valor. Esto significa que la función recibe una copia del valor original y cualquier modificación dentro de la función no afecta a la variable que se pasó como argumento:

```go
func duplicar(x int) {
    x = x * 2
}
```

```go
a := 5
duplicar(a)
fmt.Println(a)
```

```output
5
```

El valor de `a` sigue siendo `5` porque `duplicar` recibió una copia. Esto aplica a todos los tipos: `int`, `float64`, `string`, `struct`, arreglos, etc.

Los *slices* y los *maps* son casos especiales: la estructura que los representa (puntero, longitud, capacidad) se copia, pero tanto el original como la copia comparten el mismo arreglo subyacente. Esto se cubre en detalle en el próximo capítulo.

## Valores de retorno

### Retorno múltiple

Go permite devolver múltiples valores desde una función. Esto se usa frecuentemente para reportar errores junto con el resultado esperado:

```go
import "errors"

func divisionSegura(dividendo, divisor float32) (float32, error) {
    if divisor == 0.0 {
        return 0.0, errors.New("división por cero")
    }

    return dividendo / divisor, nil
}
```

Cuando se devuelven múltiples valores, los tipos se encierran entre paréntesis en el orden correspondiente.

### Valores de retorno nombrados

Go permite asignar nombres a los valores de retorno. Estos nombres actúan como variables declaradas dentro de la función, inicializadas con su valor cero. Al usar `return` sin argumentos se devuelven automáticamente los valores actuales de esas variables:

```go
func division(dividendo, divisor float32) (resultado float32, err error) {
    if divisor == 0.0 {
        err = errors.New("división por cero")
        return
    }

    resultado = dividendo / divisor
    return
}
```

El retorno desnudo (`return` sin valores) es útil cuando los nombres de retorno mejoran la legibilidad, pero su uso excesivo puede tener el efecto contrario.

### Ignorar valores de retorno

Cuando una función devuelve múltiples valores y no necesitamos alguno de ellos, podemos ignorarlo con el identificador en blanco `_`:

```go
resultado, _ := divisionSegura(10, 2)
```

Esto evita tener que declarar variables que no se van a usar, lo que Go no permite.

## Funciones como valores

Al ser "ciudadanos de primera clase", las funciones se pueden asignar a variables:

```go
f := sumar
fmt.Println(f(3, 4))
```

```output
7
```

La variable `f` tiene tipo `func(int, int) int`. También podemos declarar el tipo explícitamente:

```go
var operacion func(int, int) int
operacion = sumar
fmt.Println(operacion(10, 5))
```

Esto permite pasar funciones como argumentos a otras funciones, lo que es la base de patrones como *callbacks* y funciones de orden superior.

## Funciones anónimas

Go soporta funciones sin nombre que se pueden definir en el lugar donde se necesitan:

```go
func() {
    fmt.Println("función anónima")
}()
```

Los paréntesis al final invocan la función inmediatamente (IIFE). También se pueden asignar a una variable:

```go
saludar := func(nombre string) {
    fmt.Printf("Hola, %s\n", nombre)
}

saludar("Martín")
```

```output
Hola, Martín
```

## Ejercicios

1. Escriba una función variádica `promedio` que reciba `nums ...float64` y devuelva el promedio. Si no recibe argumentos, debe devolver `0.0`.

2. Escriba una función `aplicar` que reciba un slice de enteros y una función `f func(int) int`, y devuelva un nuevo slice con `f` aplicada a cada elemento.
