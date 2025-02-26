---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Exportado/No exportado

En Go, la visibilidad y el acceso a los componentes definidos en un módulo está
dado por una convención de nombres. Si los nombres dados a los distintos
elementos en un paquete (variables, funciones, estructuras, etc.) comienzan con
una letra mayúsculas, entonces ese elemento se considera exportado y por lo
tanto puede ser considerado como parte de la "interfaz pública" del paquete (en
términos de Java).

```{code-cell} go
:tags: [remove-output]
package ejemplo

import "fmt"

var datoProtegido string = "mi contraseña"

var DatoPublico float32 = 3.1415926

func HolaMundo() {
    fmt.Println("¡Hola Mundo!")
}
```

Esto también aplica a nivel de los campos de una estructura:

```{code-cell} go
:tags: [remove-output]
package seguridad

type Boveda struct {
    Id   int
    dato string
}
```

En este ejemplo, `Id` será un dato accesible desde cualquier punto en el
programa que importe este paquete. Pero `dato` solo será accesible desde dentro
del mismo paquete. Para modificar este valor podemos definir métodos que operen
sobre estos campos no exportados.

```{code-cell} go
:tags: [remove-output]
package seguridad

func (b *Boveda) actualizarDato(dato string) {
    if dato {
        b.dato = dato
    }
}
```
