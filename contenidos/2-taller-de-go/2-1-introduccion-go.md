---
label: intro-go
---

# Introducción a Go

## Características principales

Go es un lenguaje de programación desarrollado por Google y lanzado oficialmente en 2009. Es un lenguaje compilado, es decir, una vez escrito el código fuente se debe traducir a código máquina para poder ejecutarlo; esta operación de traducción se conoce como compilación.

```{figure} ../_static/figures/2-taller-de-go/2-1-introduccion-go/Go-Logo_Blue.svg
---
align: center
width: 200px
---
```

Los creadores de Go, [Robert Griesemer](https://en.wikipedia.org/wiki/Robert_Griesemer), [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike) y [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), han dicho que aunque la sintaxis del lenguaje está inspirada principalmente en C y en Python, y en menor medida en Java, el objetivo siempre fue crear un nuevo lenguaje simple y eficiente. Go fue diseñado para ambientes altamente productivos y concurrentes (es decir, donde varios programas se ejecutan al mismo tiempo y comparten recursos). Fue liberado como código abierto y está disponible para todos los sistemas operativos.

```{admonition} Atención
---
class: caution
---
Los lenguajes compilados cuyo código fuente se traduce de antemano a código máquina, en general suelen ser muy eficientes, ya que se pueden ejecutar directamente sobre la máquina sin "intermediarios".
```

Go es un lenguaje **fuertemente tipado** y con **tipado estático**, es decir que al momento de compilar, debe estar claramente establecido de qué tipo son sus variables. Por lo tanto, cuando escribimos código, al declarar una variable se debe declarar de qué tipo es.

Fuertemente tipado significa que no se pueden realizar operaciones entre distintos tipos de datos que no están previamente establecidas por el lenguaje o el programador. Las conversiones entre distintos tipos se deben realizar explícitamente, por ejemplo, si queremos sumarle a un número entero un número en decimal (en punto flotante) primero debemos convertir el número en punto flotante a entero y así el resultado será otro entero.

Tipado estático significa que el tipo de una variable se determina en el momento de escribir el código y no puede cambiar durante la ejecución del programa.

```{admonition} Sistema de Tipos
---
class: important
---
Un sistema de tipos permite definir qué valores puede tomar una variable y qué operaciones se pueden hacer con esos valores.
```

### Gestión de memoria

La gestión de memoria se refiere a cómo se reserva espacio para las variables y cómo se libera ese espacio cuando ya no se necesitan dichas variables. En Go, este proceso es **automático**, por lo que el programador no necesita pedir ni liberar memoria explícitamente (al estilo de `malloc` y `free` en C).

#### Reserva de memoria: Stack vs Heap

Go utiliza principalmente dos áreas de memoria para almacenar datos:

- **Pila (*Stack*):** Es una memoria muy rápida donde se almacenan las variables locales de las funciones y los parámetros. El espacio se reserva al declarar la variable y se libera automáticamente e instantáneamente cuando la función termina.
- **Montículo (*Heap*):** Es una región de memoria más grande que se utiliza para datos que deben persistir más allá de la ejecución de una función o que tienen un tamaño dinámico (como *slices* o mapas), es decir que el tamaño no se conoce al momento de declarar la variable.

Para reservar memoria, el programador simplemente declara la variable; el compilador e incluso el ambiente de ejecución (*runtime*) se encargan de asignar el espacio necesario:

```go
var edad int                 // Reserva automática para un entero
nombres := make([]string, 0) // Reserva dinámica para un slice
```

El compilador decide automáticamente dónde colocar cada variable mediante un proceso llamado **análisis de escape** (*escape analysis*). Si detecta que una variable local "escapa" de su función (por ejemplo, si se devuelve un puntero a esa variable o se guarda en una estructura global), la moverá automáticamente al *heap*.

#### Liberación de memoria: Garbage Collector

Para liberar la memoria reservada en el *heap*, Go utiliza un **recolector de basura** (*Garbage Collector* o GC). El GC se ejecuta de forma periódica realizando las siguientes tareas:

1. **Rastreo:** Identifica qué objetos en el *heap* ya no son accesibles desde ninguna parte activa del código.
2. **Barrido:** Libera el espacio que ocupaban esos objetos para que pueda ser reutilizado.

Este enfoque evita errores críticos como las **fugas de memoria** (*memory leaks*) —olvidar liberar la memoria que reservamos— o el acceso a **punteros colgantes** (*dangling pointers*) —intentar usar memoria que el programa ya liberó—.

```{figure} ../_static/figures/2-taller-de-go/2-1-introduccion-go/garbage_collector_light.svg
---
class: only-light-mode
---
Funcionamiento del Garbage Collector: rastreo y liberación de objetos inalcanzables.
```

```{figure} ../_static/figures/2-taller-de-go/2-1-introduccion-go/garbage_collector_dark.svg
---
class: only-dark-mode
---
Funcionamiento del Garbage Collector: rastreo y liberación de objetos inalcanzables.
```

En la imagen los objetos 4, 5 y 6 ya no son referenciados por ninguna variable, por lo tanto el GC los eliminará en la próxima ejecución.

### Orientación a objetos

Go no es un lenguaje orientado a objetos, es decir, no hay clases ni objetos como en Java, por ejemplo, sino que utiliza `struct`, a la C, lo que nos permite definir nuevos tipos de datos.

```go
type Persona struct {
    Nombre string
    Edad   int
}
```

Define una estructura de datos llamada `Persona` con dos campos: `Nombre` de tipo `string` y `Edad` de tipo `int`.

```go
var p Persona
p.Nombre = "Fabián"
p.Edad = 32
```

`p` es una variable de tipo `Persona` y podemos acceder a sus campos utilizando el operador punto (`.`), en este caso `p.Nombre` tiene el valor `"Fabián"` y `p.Edad` tiene el valor `32`.

En Go no existe la herencia, pero sí existe la composición, que nos permite crear nuevos tipos de datos a partir de otros. En el capítulo {ref}`structs-interfaces` vamos a profundizar en las estructuras y veremos cómo funciona la composición en Go.

### Ejemplos

En el repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git) encontrarán código de ejemplo para empezar a sumergirnos en Go.

El siguiente fragmento se encuentra en el archivo `01-introduccion/ejemplos/00-hola/main.go`

```go
package main

import "fmt"

func main() {
    fmt.Println("¡Hola mundo!")
}
```

Si ejecutamos en una terminal:

```console
go run main.go
```

obtendremos como resultado:

```output
¡Hola mundo!
```

Aquí vemos un ejemplo de una función simple que recibe dos argumentos de tipo `int` y devuelve un nuevo valor de tipo `int`.

```go
func sumar(a, b int) int {
    return a + b
}
```

Para utilizar dicha función solo debemos invocarla por su nombre y proporcionarle los parámetros requeridos.

```go
fmt.Println(sumar(32, 7))
```

```output
39
```

## Instalación

El sitio oficial de Go es [https://go.dev/](https://go.dev/) de donde se puede descargar versiones listas para instalar o el código fuente para compilar e instalar. Se recomienda seguir las instrucciones. Una vez finalizado el proceso se puede verificar la correcta instalación, abriendo una terminal y ejecutando el siguiente comando:

```console
go version
```

Si la instalación fue exitosa, deberíamos ver una salida como la siguiente:

```output
go version go1.24.0 linux/amd64
```

### Go Playground

Go ofrece un servicio *online* llamado Playground [https://go.dev/play](https://go.dev/play/) que nos permite escribir y ejecutar fragmentos de código de forma simple y sin necesidad de instalar Go localmente.

## Ejercicios

1. Verificá si Go está instalado en tu PC ejecutando el comando `go version` en una terminal. Si no lo está, descargalo e instalalo desde [https://go.dev/dl/](https://go.dev/dl/).

2. Cloná el repositorio `taller-go`, ubicate en el directorio `01-introduccion/ejemplos/00-hola/` y ejecutá el programa con `go run main.go`. ¿Qué salida se obtiene?

3. Andá al [Go Playground](https://go.dev/play/), escribí un programa que sume los números `42` y `18` e imprima el resultado, luego ejecutalo y compartí el *link* haciendo *clic* en el botón _Share_.

4. Modificá el archivo `main.go` de `01-introduccion/ejercicios/saludo-personalizado/`
   para que la función `saludar(nombre string)` devuelva `"¡Hola, <nombre>!"`,
   ejecutalo y verificá que pase el test ejecutando `go test` en ese directorio.

El enunciado completo y el esqueleto de este ejercicio están en
`01-introduccion/ejercicios/saludo-personalizado/` del repositorio
[taller-go](https://github.com/untref-ayp2/taller-go.git),
con tests para validar tu solución.

## Repositorio del taller de Go

El siguiente [repositorio](https://github.com/untref-ayp2/taller-go.git) es el material de trabajo para este taller de Go. Está organizado por temas (intro, funciones, structs, etc.) y dentro de cada tema hay dos carpetas:

- **`ejemplos/`**: programas completos y fragmentos que ilustran los conceptos explicados en el apunte. Sirven para seguir la teoría en la práctica y experimentar.
- **`ejercicios/`**: esqueletos de código con partes incompletas que se corresponden con los ejercicios propuestos a lo largo de este taller. La idea es que completen esos archivos como práctica.

Para clonarlo:

```console
git clone https://github.com/untref-ayp2/taller-go.git
```

Una vez clonado, tienen acceso a todo el contenido en su máquina local. Si se actualiza el repo pueden usar:

```console
git pull
```

## Links útiles

- [Página principal de Go](https://go.dev/)
- [Descargar Go](https://go.dev/dl/)
- [Tour interactivo de Go](https://go.dev/tour/)
- [Documentación basada en ejemplos](https://gobyexample.com/)
- [Go FAQ](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (entorno online para ejecutar código en Go)
