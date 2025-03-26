---
file_format: mystnb
kernelspec:
  name: gophernotes
---
<!--
Esta celda oculta nos permite usar `fmt.Println` sin necesidad de importar
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
func (fw FmtWrapper) Printf(format string, a ...interface{}) {
    _, _ = f.Printf(format, a...)
}
var fmt FmtWrapper = FmtWrapper{}
```

# Patrones de Diseño

Los patrones de diseño son soluciones reutilizables para problemas comunes que surgen en el desarrollo de software. Estos patrones encapsulan buenas prácticas y ofrecen un enfoque probado para resolver problemas recurrentes, facilitando el diseño de sistemas más robustos y mantenibles.

Los patrones no son exclusivos de las ciencias informáticas, sino que también se encuentran en otras disciplinas como la arquitectura, el diseño industrial y la ingeniería. En cada caso, los patrones representan soluciones probadas que se pueden adaptar a diferentes contextos, manteniendo su esencia y efectividad.

Por ejemplo, en arquitectura, un patrón podría ser el diseño de una plaza central en una ciudad, que fomenta la interacción social y el flujo de personas. De manera similar, en el desarrollo de software, los patrones de diseño buscan resolver problemas recurrentes de manera eficiente, promoviendo la reutilización y la estandarización.

Es importante destacar que los patrones no son recetas estrictas, sino guías flexibles que deben ser adaptadas según las necesidades específicas del proyecto. Comprender el contexto y los requisitos es fundamental para aplicar un patrón de manera efectiva y evitar un uso inadecuado que pueda complicar el diseño en lugar de simplificarlo.

{attribution="[Christopher Alexander](https://es.wikipedia.org/wiki/Christopher_Alexander)"}
> “Cada patrón describe un problema que ocurre una y otra vez en nuestro entorno, y luego describe la esencia de la solución de ese problema, de tal manera en que se puede utilizar esta solución más de un millón de veces sin hacerlo igual siquiera dos veces” 

## Características principales de los patrones de diseño

Reutilizabilidad
: Los patrones permiten aplicar soluciones existentes a nuevos problemas, ahorrando tiempo y esfuerzo.

Flexibilidad
: Se pueden personalizar para adaptarse a las necesidades específicas de un proyecto o contexto.

Comunicación
: Proveen un lenguaje común entre desarrolladores, facilitando la colaboración y el entendimiento del diseño.

## Clasificación de los patrones de diseño

Los patrones de diseño se dividen en tres categorías principales:

Patrones creacionales
: Se centran en la creación de objetos, asegurando que el sistema sea independiente de cómo se crean, componen y representan los objetos. Ejemplos:

   - Singleton
   - Factory Method
   - Abstract Factory

Patrones estructurales
: Se ocupan de la composición de clases y objetos para formar estructuras más grandes. Ejemplos:

   - Adapter
   - Composite
   - Decorator

Patrones de comportamiento
: Se enfocan en la interacción y responsabilidad entre objetos. Ejemplos:

   - Observer
   - Strategy
   - Command

## Patrón _Adapter_


```{figure} ../assets/images/PatronAdapter.svg
---

name: adapter
---
Patrón Adapter
```

El patrón _adapter_ permite reutilizar código heredado o _legacy_ cuya interfaz no coincide con la esperada por el sistema en el que estamos trabajando. Este patrón actúa como un puente entre la interfaz existente y la requerida, permitiendo que componentes incompatibles trabajen juntos sin modificar su código original heredado.

En la figura {ref}`adapter2` se observan las siguientes componentes. 

```{figure} ../assets/images/PatronAdapter2.svg
---

name: adapter2
---
Diagrama de Clases del Patrón Adapter
```

Interfaz
: Define la interfaz esperada por el sistema nuevo.

Adaptado
: Representa la clase existente con la interfaz incompatible. Debe implementar el comportamiento necesario para cumplir con _Interfaz_.

Adaptador
: Convierte la interfaz del _Adaptado_ en la interfaz _Interfaz_. Dentro del método +request() se invoca el método específico del _Adaptado_ +specificrequest.

### Implementación en Go

```go
package main

import "fmt"

// Interfaz esperada
type Target interface {
    Request() string
}

// Clase existente incompatible con la interfaz esperada
type Adaptee struct{}

func (a *Adaptee) SpecificRequest() string {
    return "Respuesta del Adaptee"
}

// Adaptador que convierte la interfaz del Adaptee a la interfaz Target
type Adapter struct {
    adaptee *Adaptee
}

func (a *Adapter) Request() string {
    return a.adaptee.SpecificRequest()
}

func main() {
    adaptee := &Adaptee{}
    adapter := &Adapter{adaptee: adaptee}
    fmt.Println(adapter.Request())
}
```

En este ejemplo, el adaptador (_Adapter_) permite que la clase _Adaptee_ sea utilizada como si implementara la interfaz _Target_, resolviendo la incompatibilidad entre ambas.

### Patrón _Singleton_

El patrón _singleton_ asegura que una clase tenga una única instancia y proporciona un punto de acceso global a ella. Es útil para gestionar recursos compartidos como conexiones a bases de datos o configuraciones globales.

#### Implementación en Go

```go
package main

import (
    "fmt"
    "sync"
)

type Singleton struct{}

var instance *Singleton
var once sync.Once

func GetInstance() *Singleton {
    once.Do(func() {
        instance = &Singleton{}
    })
    return instance
}

func main() {
    s1 := GetInstance()
    s2 := GetInstance()
    fmt.Println(s1 == s2) // true
}
```

En este ejemplo, el uso de `sync.Once` garantiza que la instancia se cree una sola vez, incluso en entornos concurrentes.

Estos ejemplos ilustran cómo los patrones de diseño pueden resolver problemas comunes de manera eficiente, promoviendo la reutilización y la claridad en el diseño del software.