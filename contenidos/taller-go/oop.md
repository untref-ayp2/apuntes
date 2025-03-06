---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# ¿Orientación a objetos?

De [FAQ: Is Go an object-oriented language?](https://go.dev/doc/faq#Is_Go_an_object-oriented_language):

> Si y no. Aunque Go tiene tipos y métodos y permite un estilo de programación
> orientado a objetos, no existe una jerarquía de tipos. El concepto de
> "interfaz" en Go proporciona un enfoque diferente que creemos que es fácil de
> usar y, en cierto modo, más general. También hay formas de incrustar tipos en
> otros tipos para proporcionar algo análogo, pero no idéntico, a la creación de
> subclases. Además, los métodos en Go son más generales que en C++ o Java: se
> pueden definir para cualquier tipo de datos, incluso tipos integrados, como
> enteros "sin caja". No están restringidos a estructuras (clases).
>
> Además, la falta de una jerarquía de tipos hace que los "objetos" en Go
> parezcan mucho más ligeros que en lenguajes como C++ o Java.

Veamos como poder definir un component que puede tener estado y comportamiento
asociado.

archivo `stack/stack.go`

```{code-cell} go
:tags: [remove-output]
package stack

import "errors"

type Stack struct {
    data []string
}

// Push agrega `x` en el tope de la pila.
func (s *Stack) Push(x string) {
    s.data = append(s.data, x)
}

// Pop remueve y retorna el valor en el tope de la pila.
// Devuelve un `error` si la pila está vacía.
func (s *Stack) Pop() (string, error) {
    if s.Size() == 0 {
        return "", errors.New("empty stack")
    }

    x := s.data[s.Size()-1]
    s.data = s.data[:s.Size()-1]
    return x, nil
}

// Size devuelve el número de elementos en la pila.
func (s *Stack) Size() int {
    return len(s.data)
}
```

Por un lado definimos una estructura la cual tiene "campos" (similar a lo que
llamamos atributos de una clase en Java). Luego, vamos a definir métodos que
tienen como receptor al tipo struct que creamos, de esta forma estos métodos
tendrán acceso a modificar los campos que no son exportados (cuyos nombres
comienzan con minúsculas).

archivo `main.go`

```{code-cell} go
:tags: [remove-output]
package main

import (
 "fmt"
 "tda/stack"
)

func main() {
 s := stack.Stack{}

 s.Push("world!")
 s.Push("Hello, ")

 for s.Size() > 0 {
  if x, err := s.Pop(); err == nil {
   fmt.Print(x)
  }
 }

 fmt.Println()
}
```

En nuestro caso, para crear una variable de tipo `Stack` podemos utilizar la
forma literal de declarar una estructura. También es común crear un método
llamado `NewStack` que sirve como constructor y que devuelva un puntero a un
variable de tipo `Stack`, el cual puede recibir argumentos y asignar esos
valores a los campos de la estructura.

Una vez creada la variable, podemos usar la notación de punto, como
acostumbramos a hacerlo al invocar métodos de un objeto.
