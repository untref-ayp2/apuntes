---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Introducción a Go

<!--
Este bloque oculto nos permite usar `fmt.Println` sin necesidad de importar
"fmt", el objetivo es que no se imprima la salida que tiene `fmt.Println` ya
que devuelve la cantidad de caracteres impresos y un error.
-->

```{code-cell} go
:tags: [remove-cell]
import f "fmt"

type FmtWrapper struct{}

func (fw FmtWrapper) Println(a ...interface{}) {
    _, _ = f.Println(a...)
}

var fmt FmtWrapper = FmtWrapper{}
```

## Características Principales

Go es un lenguaje de programación desarrollado por Google, que se lanzó
oficialmente en 2009. Es un lenguaje compilado, es decir que una vez escrito el
código fuente se debe traducir a código máquina para poder ejecutarlo, esta
operación de traducción se conoce como compilación.

Los creadores de Go, [Robert
Griesemer](https://en.wikipedia.org/wiki/Robert_Griesemer), [Rob
Pike](https://en.wikipedia.org/wiki/Rob_Pike) y [Ken
Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), han dicho que aunque la
sintáxis del lenguaje está inspirada principalmente en C y en Python y en menor
medida en Java, el objetivo siempre fue crear un nuevo lenguaje simple y
eficiente. Go fue diseñado para ambientes altamente productivos y concurrentes
(es decir donde varios programas se ejecutan al mismo tiempo y comparten
recursos). Fue liberado cómo código abierto y está disponible para todos los
sistemas operativos.

```{attention}
Los lenguajes compilados cuyo código fuente se traduce de antemano a código
máquina, en general suelen ser muy eficientes, ya que se pueden ejecutar
directamente sobre la máquina sin "intermediarios".
```

Go es un lenguaje **fuertemente tipado** y con **tipado estático**, es decir que
al momento de compilar, debe estar claramente establecido de que tipo son sus
variables. Por lo tanto, cuando escribimos código, al declarar una variable se
debe declarar de que tipo es.

Fuertemente tipado significa que no se puede realizar operaciones entre
distintos tipos de datos que no están previamente establecidas por el lenguaje o
el programador. Las conversiones entre distintos tipos se deben realizar
explicitamente, por ejemplo si queremos sumarle a un número entero un número en
decimal (en punto flotante) primero debemos convertir el número en punto
flotante a entero y así el resultado será otro entero.

```{note}
Un sistema de tipos permite definir que valores puede tomar una variable y que
operaciones se pueden hacer con esos valores.
```

La gestión de la memoria es automática, es decir el programador puede
desentenderse de liberar la memoria que ya no se utiliza. Go implementa un
**recolector de basura** o _garbage collector_, que identifica y libera zonas de
la memoria que el programa en ejecución ya no necesita. La asignación de memoria
también es automática, cuando se declara una variable, como se declara el tipo
de la misma, Go sabe exactamente cuanta memoria reservar para almacenar
cualquier dato del tipo declarado.

Go no es un lenguaje orientado a objetos, es decir no hay clases ni objetos como
en Java por ejemplo, sino que utiliza `struct`, a la C, lo que nos permite
definir nuevos tipos de datos.

### Ejemplos

En el repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git) encontrarán código de ejemplo para empezar a sumergirnos en Go.

Se recomienda crear una carpeta en el disco local, por ejemplo con el nombre taller-go, y clonar el repositorio

```console
git clone https://github.com/untref-ayp2/taller-go.git
```

El siguiente fragmento se encuentra en el archivo `main.go`

:::{admonition} `main.go`
:class: note

```go
package main

import "fmt"

func main() {
    fmt.Println("¡Hola mundo!")
}
```

:::

Si ejecutamos en una terminal:

```console
go run main.go
```

obtendremos como resultado:

```output
"¡Hola mundo!"
```

Aquí vemos un ejemplo de una función simple que recibe 2 argumentos de tipo
`int` y devuelve un nuevo valor de tipo `int`.

```{code-cell} go
func sumar(a, b int)int{
    return a + b
}
```

Para utilizar dicha función solo debemos invocarla por su nombre y
proporcionarle los parametros requeridos.

```{code-cell} go
sumar(32, 7)
```

## Similitudes entre Java y Go

- Son lenguajes compilados y con chequeo estático de tipos.
- Implementan un recolector de basura (_Garbage Collector_).

## Principales diferencias entre Java y Go

- Go no es orientado a objetos.
- Go utiliza punteros de forma directa.
- Go permite devolver multiples valores desde una función o un método.
- Go no tiene excepciones.
- Go tiene interfaces pero funcionan de manera distinta que en Java.

## Links útiles

- [Página principal de Go](https://go.dev/)
- [Descargar Go](https://go.dev/dl/)
- [Tour interactivo de Go](https://go.dev/tour/)
- [Documentación basada en ejemplos](https://gobyexample.com/)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (entorno online ara ejecutar código en
  Go)

## Instalación

El sitio oficial de Go es <https://go.dev/> de donde se puede descargar
versiones listas para instalar o el código fuente para compilar e instalar. Se
recomienda seguir las instrucciones. Una vez finalizado el proceso se puede
verificar la correcta instalación, abriendo una terminal y ejecutando el
siguiente comando:

```console
go version
```

Si la instalación fué exitosa, deberíamos ver una salida como la siguiente:

```output
go version go1.24.0 linux/amd64
```

### Go Playground

Go ofrece un servicio online llamado Playground
[https://go.dev/play](https://go.dev/play/p/kBGNnaPKcvt) que nos permite
escribir y ejecutar fragmentos de código de forma simple y sin necesidad de
instalar Go localmente.

### Entornos de Desarrollo (IDEs)

Se puede utilizar cualquier entorno de desarrollo disponbile, por ejemplo
[Visual Studio Code](https://code.visualstudio.com/).

## Estructura de un programa en Go

Utilizando el clásico ejemplo de un hola mundo, vamos a mostrar cómo se organiza
el código en Go.

El código se organiza en **paquetes**. Por ejemplo, podemos definir un paquete
llamado `saludo`, con una función que se exporta llamada `Saludar`.

:::{admonition} `saludo/saludo.go`
:class: note

```go
package saludo

import "fmt"

func Saludar() {
    fmt.Println("¡Hola mundo!")
}
```

:::

Como en muchos lenguajes de programación, el punto de entrada a un programa es
por medio de una función `main`, como podemos ver a continuación, donde nuestro
programa hace uso del paquete `saludo`:

:::{admonition} `main.go`
:class: note

```go
package main

import ".saludo"

func main() {
    saludo.Saludar()
}
```

:::

:::{admonition} ¡Para practicar!
:class: hint

Se recomienda recrear el ejemplo previamente presentado y ejecutarlo para
corroborar que todo funciona correctamente y que los paquetes definidos por
nosotros mismos se pueden importar sin problemas.

Notar que la estructura de archivos que se debe generar es:

```text
ejemplo
├── saludo
│   └── saludo.go
└── main.go
```

Luego desde una terminal, deberán ejecutar:

```console
go run main.go
```

:::

### Declaración de variables

Existen varias formas de declarar una variable en Go. Primero es utilizando la
palabra clave `var`, donde debemos especificar el nombre de la variable y su
tipo.

```{code-cell} go
var edad int
edad = 42
```

Opcionalmente podríamos inicializar esa variable en la misma línea como sucede
en muchos lenguajes de programación.

```{code-cell} go
var edad int = 42
```

Otra forma de declarar una variable es utilizando la notación de asignación
corta (`:=`), que determina el tipo de la variable de forma implícita. Por lo
que podemos escribir:

```{code-cell} go
edad := 42
```

Tipos básicos de datos en Go:

- `bool`
- `string`
- `int`, `int8`, `int16`, `int32`, `int64`
- `uint`, `uint8`, `uint16`, `uint32`, `uint64`
- `float32`, `float64`
- `complex64`, `complex128`
- `byte` (alias de `uint8`)
- `rune` (alias de `int32`, representa una posición en código Unicode)
- `uintptr` (tipo utilizado para guardar una dirección de puntero)

Go es un lenguaje fuertemente tipado. A diferencia de Java, Go no hace
conversión automática de tipos por lo que cada vez que necesitemos pasar de un
tipo a otro debemos realizar un casteo explicito.

```{code-cell} go
:tags: [remove-output]
var edad int32 = 42
var edad64 int64 = edad
```

Este código dará como resultado el siguiente error:

```output
cannot use edad (variable of type int32) as int64 value in variable declaration
```

En cambio, debemos realizar el casteo explicito para indicar al compilador de Go
que realmente queremos asignar un valor de tipo `int32` a una variable de tipo
`int64`.

```{code-cell} go
var edad int32 = 42
var edad64 int64 = int64(edad)
```

### Control de flujo en Go

Los bloques condicionales `if`/`else` se utilizan de forma muy similar a como
estamos acostumbrado en Java (con la salvedad de que los paréntesis no son
necesarios en las condiciones).

```{code-cell} go
num := 7

if num < 0 {
    fmt.Println(num, "es negativo")
} else if num < 10 {
    fmt.Println(num, "tiene 1 dígito")
} else {
    fmt.Println(num, "tiene múltiples dígitos")
}
```

A diferencia de Java, Go cuenta sólo con una instrucción de iteración: el `for`.
Pero este se puede utilizar de diferentes formas.

De forma análoga a un `while` como lo vimos en Java, cuando `for` solo recibe
una condición, va a ejecutar el bloque de código "mientras" la condición sea
verdadera.

```{code-cell} go
:tags: [remove-output]
i := 1

for i <= 3 {
    fmt.Println(i)
    i = i + 1
}
```

```output
1
2
3
```

También puede utilizarse de la forma clásica, indicando la inicialización, la
condición y la operación luego de cada iteración.

```{code-cell} go
:tags: [remove-output]
for j := 7; j <= 9; j++ {
    fmt.Println(j)
}
```

```output
7
8
9
```

Si `for` no recibe condición, se comporta de la misma forma que `while(true)`.

```{code-cell} go
:tags: [remove-output]
for {
    fmt.Println("loop")
    break
}
```

```output
loop
```

También existen las instrucciones `break` y `continue` para alterar la ejecución
de las iteraciones.

```{code-cell} go
:tags: [remove-output]
for n := 0; n <= 5; n++ {
    if n%2 == 0 {
        continue
    }
    fmt.Println(n)
}
```

```output
1
3
5
```
