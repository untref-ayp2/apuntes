---
label: errores
---

# Errores

Si bien Go no implementa excepciones como una construcción propia del lenguaje, es posible hacer un control de errores por medio del módulo `errors`.

Por eso, en Go es común que los errores sean devueltos "normalmente" desde una función y quien invoca dicha función es responsable de manejar un posible error.

## Crear errores simples

```{code-block} go
---
linenos:
---
package main

import (
    "errors"
    "fmt"
)

func test(input int) error {
    if input < 0 {
        // Creamos un error con un mensaje estático
        return errors.New("el nro. ingresado debe ser mayor o igual a cero")
    }
    return nil
}

func main() {
    err := test(-1)
    if err != nil {
        fmt.Println(err)
    }
}
```

```output
el nro. ingresado debe ser mayor o igual a cero
```

## Crear errores con formateo dinámico

Además, Go incluye en el paquete `fmt` la función `fmt.Errorf`, que permite crear errores con mensajes formateados, similar a `fmt.Sprintf`. Esto es muy útil para **agregar información dinámica** al mensaje de error.

```{code-block} go
---
linenos:
---
package main

import "fmt"

func test(input int) error {
    if input < 0 {
        // Se agrega información dinámica al mensaje
        return fmt.Errorf("el nro. ingresado debe ser mayor o igual a cero, "+
            "en su lugar se recibió: %d", input)
    }
    return nil
}

func main() {
    err := test(-1)
    if err != nil {
        fmt.Println(err)
    }
}
```

```output
el nro. ingresado debe ser mayor o igual a cero, en su lugar se recibió: -1
```

En este ejemplo, la función retorna un error más informativo que incluye el valor de entrada que causó el problema. Este tipo de mensajes con contexto es de gran ayuda para depuración y *logging*.

En los dos ejemplos anteriores, podemos observar la forma típica en la que se maneja un error en Go. Van a encontrar `if err != nil` en múltiples lugares de un programa de Go.

## La interfaz `error`

Internamente, `error` es una **interfaz** incorporada en el lenguaje:

```{code-block} go
---
linenos:
---
type error interface {
    Error() string
}
```

Cualquier tipo que implemente `Error() string` cumple automáticamente la interfaz `error` y puede usarse como valor de error. Tanto `errors.New` como `fmt.Errorf` devuelven tipos que implementan esta interfaz, por eso funcionan donde se espera un `error`.

Si definís tu propio tipo con un método `Error() string`, también podés usarlo como error. Esto permite crear errores con más información:

```{code-block} go
---
linenos:
---
package main

import "fmt"

type ErrEdad struct {
    Valor int
}

func (e *ErrEdad) Error() string {
    return fmt.Sprintf("edad inválida: %d", e.Valor)
}

func validarEdad(edad int) error {
    if edad < 0 || edad > 150 {
        return &ErrEdad{Valor: edad}
    }
    return nil
}

func main() {
    err := validarEdad(-5)
    if err != nil {
        fmt.Println(err)
    }
}
```

```output
edad inválida: -5
```

Acá `ErrEdad` implementa la interfaz `error` porque tiene `Error() string`. La función `validarEdad` devuelve un `*ErrEdad` (que es un `error`) cuando la edad es inválida.

## Errores centinela

Un patrón muy común en Go es definir errores como **variables globales** (llamados errores centinela). Sirven para comparar con `==` y saber exactamente qué error ocurrió:

```{code-block} go
---
linenos:
---
package main

import (
    "errors"
    "fmt"
)

var ErrNotFound = errors.New("elemento no encontrado")

func buscar(numeros []int, target int) (int, error) {
    for _, n := range numeros {
        if n == target {
            return n, nil
        }
    }
    return 0, ErrNotFound
}

func main() {
    nums := []int{10, 20, 30}
    _, err := buscar(nums, 25)
    if err == ErrNotFound {
        fmt.Println("elemento no encontrado")
    }
}
```

```output
elemento no encontrado
```

Fijate que `ErrNotFound` se declara afuera de cualquier función, como variable del paquete. Por convención, estos errores se nombran con el prefijo `Err` (son exportados) o `err` (si son internos al paquete).

## Tipos de error personalizados

Cuando necesitás que un error lleve **más información** que solo un mensaje, podés definir un struct que implemente la interfaz `error`:

```{code-block} go
---
linenos:
---
package main

import "fmt"

type ValidationError struct {
    Campo string
    Valor int
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("error en %s: %d no es válido",
        e.Campo, e.Valor)
}

func validarEdad(edad int) error {
    if edad < 0 {
        return &ValidationError{
            Campo: "edad",
            Valor: edad,
        }
    }
    return nil
}

func main() {
    err := validarEdad(-1)
    if err != nil {
        fmt.Println(err)
    }
}
```

```output
error en edad: -1 no es válido
```

Esto es útil porque quien recibe el error puede **consultar los campos** del `ValidationError` haciendo una conversión de tipo (*type assertion*) para obtener más detalles.

## Wrapping de errores con `%w`

Muchas veces una función llama a otra que puede fallar, y queremos **agregar contexto** al error original sin perderlo. Go permite esto con `fmt.Errorf` y el verbo `%w`:

```{code-block} go
---
linenos:
---
package main

import (
    "errors"
    "fmt"
    "os"
)

func cargarUsuario(id int) (string, error) {
    ruta := fmt.Sprintf("usuarios/%d.txt", id)
    datos, err := os.ReadFile(ruta)
    if err != nil {
        return "", fmt.Errorf("cargando usuario %d: %w", id, err)
    }
    return string(datos), nil
}

func main() {
    _, err := cargarUsuario(42)
    if err != nil {
        if errors.Is(err, os.ErrNotExist) {
            fmt.Println("el archivo del usuario no existe")
        } else {
            fmt.Println("error inesperado:", err)
        }
        return
    }
}
```

```output
el archivo del usuario no existe
```

Fijate que el mensaje del error original (`os.ErrNotExist`) queda preservado
dentro del error que creamos con `%w`. Por eso `errors.Is` puede
detectarlo aunque esté envuelto en una capa con más contexto. Así podemos
reaccionar distinto según el tipo de error que ocurrió, sin importar cuánto
contexto se haya agregado en el camino.

## Convenciones en el manejo de errores

Para cerrar, algunas convenciones que se ven en todo código Go:

1. **El error es siempre el último valor de retorno.** Si una función devuelve un resultado y puede fallar, la firma es `(resultado, error)`.
2. **Revisar `err != nil` inmediatamente.** Apenas recibís un error, lo *checkeás*. No lo guardás para después.
3. **No ignorar errores.** Si una función devuelve `error` y estás seguro de que no va a fallar, usá `_ = llamada()` como señal explícita de que decidiste ignorarlo.
4. **Preferir `errors.New` y `fmt.Errorf` a `panic`.** Salvo excepciones muy contadas, los errores se manejan con valores, no con `panic`.

## Manejo de errores con archivos

Como viste en el capítulo 2-8, las funciones del paquete `os` devuelven un
`error` que tenés que revisar. Combinado con lo que vimos antes, podés
**agregar contexto** al error con `%w` para saber en qué operación falló:

```{code-block} go
---
linenos:
---
package main

import (
    "fmt"
    "os"
)

func leerArchivo(ruta string) (string, error) {
    datos, err := os.ReadFile(ruta)
    if err != nil {
        return "", fmt.Errorf("error al leer %s: %w", ruta, err)
    }
    return string(datos), nil
}

func main() {
    contenido, err := leerArchivo("mensaje.txt")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Print(contenido)
}
```

```output
error al leer mensaje.txt: open mensaje.txt: no such file or directory
```

Lo mismo al escribir:

```{code-block} go
---
linenos:
---
package main

import (
    "fmt"
    "os"
)

func escribirArchivo(ruta, texto string) error {
    err := os.WriteFile(ruta, []byte(texto), 0644)
    if err != nil {
        return fmt.Errorf("error al escribir %s: %w", ruta, err)
    }
    return nil
}

func main() {
    err := escribirArchivo("salida.txt", "Hola, archivo!\n")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println("archivo escrito correctamente")
}
```

```output
archivo escrito correctamente
```

Este patrón — función que delega en `os.ReadFile`/`os.WriteFile` y envuelve
el error con `fmt.Errorf` + `%w` — es muy común en programas Go que trabajan
con archivos.

## Ejercicios

Los ejercicios de este capítulo están en `10-errores/ejercicios/`
del repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git).
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.
