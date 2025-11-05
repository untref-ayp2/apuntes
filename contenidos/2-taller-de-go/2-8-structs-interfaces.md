---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Estructuras e interfaces

## _Structs_

En Go las _structs_ son colecciones de campos, podríamos pensar una `struct`{l=go} cómo una clase que solo declara atributos (los campos).

```go
type Direccion struct {
    calle, ciudad, provincia string
    numero                   uint
}

type Persona struct {
    nombre, apellido string
    edad             uint
    direccion        Direccion
}
```

Para acceder a un campo de una estructura, se usa la notación de punto, como lo hacemos para acceder a un atributo en Java.

```go
var p1 Persona
p1.nombre = "Marcelo"
p1.edad = 27
```

También podemos declarar una variable de tipo `struct`{l=go} de forma literal:

```go
p2 := Persona{nombre: "Laura", apellido: "Medina", edad: 25}
```

### Métodos

Go no tiene clases como Java, sin embargo permite definir métodos sobre ciertos tipos.

Un método es una función con un argumento especial **receptor** . El **receptor** aparece en su propia lista de argumentos entre la palabra clave `func`{l=go} y el nombre del método.

```go
import "math"

type Vector struct {
    X, Y float64
}

func (v Vector) Modulo() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vector) Escalar(factor float64) {
    v.X *= factor
    v.Y *= factor
}
```

En este ejemplo, el método `Modulo`{l=go} tiene un receptor de tipo `Vector`{l=go} llamado `v`{l=go}. Y el método `Escalar`{l=go} recibe un puntero a `Vector`{l=go}, ya que en este contexto es necesario contar con la referencia a la variable apuntada, ya que este método modifica el "estado" del receptor.

## Interfaces

Como mencionamos anteriormente, en Go existe el concepto de interfaces pero funcionan de forma algo diferente a como lo hacen en Java.

Un tipo `interface`{l=go} se define como una conjunto de firmas de método. Un valor de ese tipo de interfaz, puede contener a cualquier valor que implemente (todos) esos métodos.

```go
type Caminante interface {
    Avanzar(pasos int)
    Girar(grados float32)
}
```

Luego si un tipo implementa todos esos métodos:

```go
func (p *Persona) Avanzar(pasos int) { /* ... */ }

func (p *Persona) Girar(grados float32) { /* ... */ }
```

Podemos pasar como parámetro una variable de tipo `Persona`{l=go} siempre se espere un argumento de tipo `Caminante`{l=go}.

```go
func RealizarRecorrido(caminante Caminante) { /* ... */ }

p := Persona{}

RealizarRecorrido(p)
```
