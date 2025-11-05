---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Errores

Si bien Go no implementa excepciones como una construcción propia del lenguaje, es posible hacer un control de errores por medio del módulo `errors`{l=go}.

Por eso, en Go es común que los errores sean devueltos "normalmente" desde una función y quien invocó dicha función es responsable de manejar un posible error.

## Crear errores simples

```go
package main

import (
    "errors"
    "fmt"
)

func test(input int) error {
    if input < 0 {
        // Creamos un error con un mensaje estático
        return errors.New("input must be greater or equal to zero")
    }
    return nil
}

func main() {
    err := test(-1)
    if err != nil {
        fmt.Print(err)
    }
}
```

## Crear errores con formateo dinámico

Además, Go incluye en el paquete `fmt`{l=go} la función `fmt.Errorf`{l=go}, que permite crear errores con mensajes formateados, similar a `fmt.Sprintf`{l=go}. Esto es muy útil para **agregar información dinámica** al mensaje de error.

```go
package main

import "fmt"

func test(input int) error {
    if input < 0 {
        // Se agrega información dinámica al mensaje
        return fmt.Errorf("input must be greater or equal to zero, instead it was: %d", input)
    }
    return nil
}

func main() {
    err := test(-1)
    if err != nil {
        fmt.Print(err)
    }
}
```

En este ejemplo, la función retorna un error más informativo que incluye el valor de entrada que causó el problema. Este tipo de mensajes con contexto son de gran ayuda para depuración y logging.

______________________________________________________________________

En los dos ejemplos anteriores, podemos observar la forma típica en la que se maneja un error en Go. Van a encontrar `if err != nil`{l=go} en multiples lugares de un programa de Go.

Go tiene una forma de "lanzar" errores por medio de la función `panic`{l=go}, pero esta debería ser reservada para casos muy extremos, ya que no es posible recuperar el programa luego de esa invocación.
