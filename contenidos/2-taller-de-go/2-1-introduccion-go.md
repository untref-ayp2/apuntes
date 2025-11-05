---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Introducción a Go

## Características Principales

Go es un lenguaje de programación desarrollado por Google, que se lanzó oficialmente en 2009. Es un lenguaje compilado, es decir que una vez escrito el código fuente se debe traducir a código máquina para poder ejecutarlo, esta operación de traducción se conoce como compilación.

Los creadores de Go, [Robert Griesemer](https://en.wikipedia.org/wiki/Robert_Griesemer){target="\_blank"}, [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike){target="\_blank"} y [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson){target="\_blank"}, han dicho que aunque la sintáxis del lenguaje está inspirada principalmente en C y en Python y en menor medida en Java, el objetivo siempre fue crear un nuevo lenguaje simple y eficiente. Go fue diseñado para ambientes altamente productivos y concurrentes (es decir donde varios programas se ejecutan al mismo tiempo y comparten recursos). Fue liberado cómo código abierto y está disponible para todos los sistemas operativos.

```{attention}
Los lenguajes compilados cuyo código fuente se traduce de antemano a código máquina, en general suelen ser muy eficientes, ya que se pueden ejecutar directamente sobre la máquina sin "intermediarios".
```

Go es un lenguaje **fuertemente tipado** y con **tipado estático**, es decir que al momento de compilar, debe estar claramente establecido de que tipo son sus variables. Por lo tanto, cuando escribimos código, al declarar una variable se debe declarar de que tipo es.

Fuertemente tipado significa que no se puede realizar operaciones entre distintos tipos de datos que no están previamente establecidas por el lenguaje o el programador. Las conversiones entre distintos tipos se deben realizar explicitamente, por ejemplo si queremos sumarle a un número entero un número en decimal (en punto flotante) primero debemos convertir el número en punto flotante a entero y así el resultado será otro entero.

```{note}
Un sistema de tipos permite definir que valores puede tomar una variable y que operaciones se pueden hacer con esos valores.
```

La gestión de la memoria es automática, es decir el programador puede desentenderse de liberar la memoria que ya no se utiliza. Go implementa un **recolector de basura** o _garbage collector_, que identifica y libera zonas de la memoria que el programa en ejecución ya no necesita. La asignación de memoria también es automática, cuando se declara una variable, como se declara el tipo de la misma, Go sabe exactamente cuanta memoria reservar para almacenar cualquier dato del tipo declarado.

Go no es un lenguaje orientado a objetos, es decir no hay clases ni objetos como en Java por ejemplo, sino que utiliza `struct`{l=go}, a la C, lo que nos permite definir nuevos tipos de datos.

### Ejemplos

En el repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git){target="\_blank"} encontrarán código de ejemplo para empezar a sumergirnos en Go.

Se recomienda crear una carpeta en el disco local, por ejemplo con el nombre taller-go, y clonar el repositorio

```console
git clone https://github.com/untref-ayp2/taller-go.git
```

El siguiente fragmento se encuentra en el archivo `00-hola/main.go`

````{admonition} <code class="docutils literal notranslate"><span class="pre">00-hola/main.go</span></code>
---
class: note
---
```go
package main

import "fmt"

func main() {
    fmt.Println("¡Hola mundo!")
}
```

````

Si ejecutamos en una terminal:

```console
go run main.go
```

obtendremos como resultado:

```output
"¡Hola mundo!"
```

Aquí vemos un ejemplo de una función simple que recibe 2 argumentos de tipo `int`{l=go} y devuelve un nuevo valor de tipo `int`{l=go}.

```go
func sumar(a, b int)int{
    return a + b
}
```

Para utilizar dicha función solo debemos invocarla por su nombre y proporcionarle los parametros requeridos.

```go
sumar(32, 7)
```

```output
39
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

- [Página principal de Go](https://go.dev/){target="\_blank"}
- [Descargar Go](https://go.dev/dl/){target="\_blank"}
- [Tour interactivo de Go](https://go.dev/tour/){target="\_blank"}
- [Documentación basada en ejemplos](https://gobyexample.com/){target="\_blank"}
- [Go FAQ](https://go.dev/doc/faq){target="\_blank"}
- [Go Playground](https://go.dev/play/){target="\_blank"} (entorno online ara ejecutar código en Go)

## Instalación

El sitio oficial de Go es [https://go.dev/](https://go.dev/){target="\_blank"} de donde se puede descargar versiones listas para instalar o el código fuente para compilar e instalar. Se recomienda seguir las instrucciones. Una vez finalizado el proceso se puede verificar la correcta instalación, abriendo una terminal y ejecutando el siguiente comando:

```console
go version
```

Si la instalación fué exitosa, deberíamos ver una salida como la siguiente:

```output
go version go1.24.0 linux/amd64
```

### Go Playground

Go ofrece un servicio online llamado Playground [https://go.dev/play](https://go.dev/play/p/kBGNnaPKcvt){target="\_blank"} que nos permite escribir y ejecutar fragmentos de código de forma simple y sin necesidad de instalar Go localmente.

### Entornos de Desarrollo (IDEs)

Se puede utilizar cualquier entorno de desarrollo disponbile, por ejemplo [Visual Studio Code](https://code.visualstudio.com/){target="\_blank"}.

## Estructura de un programa en Go

Utilizando el clásico ejemplo de un hola mundo, vamos a mostrar cómo se organiza el código en Go.

El código se organiza en **paquetes**. Por ejemplo, podemos definir un paquete llamado `saludo`{l=go}, con una función que se exporta llamada `Saludar`{l=go}.

````{admonition} <code class="docutils literal notranslate"><span class="pre">saludo/saludo.go</span></code>
---
class: note
---
```go
package saludo

import "fmt"

func Saludar() {
    fmt.Println("¡Hola mundo!")
}
```

````

Como en muchos lenguajes de programación, el punto de entrada a un programa es por medio de una función `main`{l=go}, como podemos ver a continuación, donde nuestro programa hace uso del paquete `saludo`{l=go}:

````{admonition} <code class="docutils literal notranslate"><span class="pre">main.go</span></code>
---
class: note
---
```go
package main

import ".saludo"

func main() {
    saludo.Saludar()
}
```

````

````{admonition} ¡Para practicar!
---
class: hint
---
Se recomienda recrear el ejemplo previamente presentado y ejecutarlo para corroborar que todo funciona correctamente y que los paquetes definidos por nosotros mismos se pueden importar sin problemas.

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

````

### Declaración de variables

Existen varias formas de declarar una variable en Go. Primero es utilizando la palabra clave `var`{l=go}, donde debemos especificar el nombre de la variable y su tipo.

```go
var edad int
edad = 42
```

Opcionalmente podríamos inicializar esa variable en la misma línea como sucede en muchos lenguajes de programación.

```go
var edad int = 42
```

Otra forma de declarar una variable es utilizando la notación de asignación corta (`:=`{l=go}), que determina el tipo de la variable de forma implícita. Por lo que podemos escribir:

```go
edad := 42
```

Tipos básicos de datos en Go:

- `bool`{l=go}
- `string`{l=go}
- `int`{l=go}, `int8`{l=go}, `int16`{l=go}, `int32`{l=go}, `int64`{l=go}
- `uint`{l=go}, `uint8`{l=go}, `uint16`{l=go}, `uint32`{l=go}, `uint64`{l=go}
- `float32`{l=go}, `float64`{l=go}
- `complex64`{l=go}, `complex128`{l=go}
- `byte`{l=go} (alias de `uint8`{l=go})
- `rune`{l=go} (alias de `int32`{l=go}, representa una posición en código Unicode)
- `uintptr`{l=go} (tipo utilizado para guardar una dirección de puntero)

Go es un lenguaje fuertemente tipado. A diferencia de Java, Go no hace conversión automática de tipos por lo que cada vez que necesitemos pasar de un tipo a otro debemos realizar un casteo explicito.

```go
var edad int32 = 42
var edad64 int64 = edad
```

Este código dará como resultado el siguiente error:

```output
cannot use edad (variable of type int32) as int64 value in variable declaration
```

En cambio, debemos realizar el casteo explicito para indicar al compilador de Go que realmente queremos asignar un valor de tipo `int32`{l=go} a una variable de tipo `int64`{l=go}.

```go
var edad int32 = 42
var edad64 int64 = int64(edad)
```

### Control de flujo en Go

Los bloques condicionales `if`{l=go}/`else`{l=go} se utilizan de forma muy similar a como estamos acostumbrado en Java (con la salvedad de que los paréntesis no son necesarios en las condiciones).

```go
num := 7

if num < 0 {
    fmt.Println(num, "es negativo")
} else if num < 10 {
    fmt.Println(num, "tiene 1 dígito")
} else {
    fmt.Println(num, "tiene múltiples dígitos")
}
```

```output
7 tiene 1 dígito
```

A diferencia de Java, Go cuenta sólo con una instrucción de iteración: el `for`{l=go}. Pero este se puede utilizar de diferentes formas.

De forma análoga a un `while` como lo vimos en Java, cuando `for`{l=go} solo recibe una condición, va a ejecutar el bloque de código "mientras" la condición sea verdadera.

```go
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

También puede utilizarse de la forma clásica, indicando la inicialización, la condición y la operación luego de cada iteración.

```go
for j := 7; j <= 9; j++ {
    fmt.Println(j)
}
```

```output
7
8
9
```

Si `for`{l=go} no recibe condición, se comporta de la misma forma que `while(true)`.

```go
for {
    fmt.Println("loop")
    break
}
```

```output
loop
```

También existen las instrucciones `break`{l=go} y `continue`{l=go} para alterar la ejecución de las iteraciones.

```go
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
