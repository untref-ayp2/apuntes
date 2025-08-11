---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Errores

Si bien Go no implementa excepciones como una construcción propia del lenguaje,
es posible hacer un control de errores por medio del módulo `errors` y el paquete `fmt`.

Por eso, en Go es común que los errores sean devueltos "normalmente" desde una
función y quien invocó dicha función es responsable de manejar un posible error.

Además del paquete `errors`, Go incluye en el paquete `fmt` la función `fmt.Errorf`,
que permite crear errores con mensajes formateados, similar a `fmt.Sprintf`. Esto
es muy útil para agregar información dinámica en el mensaje de error.

```{code-cell} go
import "fmt"

func test(input int) error {
    if input < 0 {
      // Usamos fmt.Errorf para crear un error con un mensaje dinámico.
      // Se puede dejar solo un mensaje como error sin formato dinámico.
      return fmt.Errorf("input is less than zero: %d", input)
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

En este ejemplo, podemos observar la forma típica en la que se maneja un error
en Go. Van a encontrar `if err != nil` en multiples lugares de un programa de Go.

Go tiene una forma de "lanzar" errores por medio de la función `panic`, pero
esta debería ser reservada para casos muy extremos, ya que no es posible
recuperar el programa luego de esa invocación.
