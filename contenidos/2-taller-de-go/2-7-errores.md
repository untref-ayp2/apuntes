---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Errores

Si bien Go no implementa excepciones como una construcción propia del lenguaje,
es posible hacer un control de errores por medio del módulo `errors`.

Por eso, en Go es común que los errores sean devueltos "normalmente" desde una
función y quien invocó dicha función es responsable de manejar un posible error.

## Crear errores simples

```{code-cell} go
import {
    "errors"
    "fmt"
}

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

## Crear errores con contexto dinámico

Además, Go incluye en el paquete `fmt` la función `fmt.Errorf`, que permite
crear errores con mensajes formateados, similar a `fmt.Sprintf`.
Esto es muy útil para **agregar información dinámica** al mensaje de error.

```{code-cell} go
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

En este ejemplo, la función retorna un error más informativo que incluye
el valor de entrada que causó el problema. Este tipo de mensajes con contexto
son de gran ayuda para depuración y logging.

---

En los dos ejemplos anteriores, podemos observar la forma típica en la que se maneja un error
en Go. Van a encontrar `if err != nil` en multiples lugares de un programa de Go.

Go tiene una forma de "lanzar" errores por medio de la función `panic`, pero
esta debería ser reservada para casos muy extremos, ya que no es posible
recuperar el programa luego de esa invocación.
