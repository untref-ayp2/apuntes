---
label: patrones-diseno
---

# Patrones de Diseño

Los patrones de diseño son soluciones reutilizables para problemas comunes que surgen en el desarrollo de software. Estos patrones encapsulan buenas prácticas y ofrecen un enfoque probado para resolver problemas recurrentes, facilitando el diseño de sistemas más robustos y mantenibles {cite}`gamma2002patrones`.

Los patrones no son exclusivos de las ciencias informáticas, sino que también se encuentran en otras disciplinas como la arquitectura, el diseño industrial y la ingeniería. En cada caso, los patrones representan soluciones probadas que se pueden adaptar a diferentes contextos, manteniendo su esencia y efectividad.

Por ejemplo, en arquitectura, un patrón podría ser el diseño de una plaza central en una ciudad, que fomenta la interacción social y el flujo de personas. De manera similar, en el desarrollo de software, los patrones de diseño buscan resolver problemas recurrentes de manera eficiente, promoviendo la reutilización y la estandarización.

Es importante destacar que los patrones no son recetas estrictas, sino guías flexibles que deben ser adaptadas según las necesidades específicas del proyecto. Comprender el contexto y los requisitos es fundamental para aplicar un patrón de manera efectiva y evitar un uso inadecuado que pueda complicar el diseño en lugar de simplificarlo.

```{epigraph}
“Cada patrón describe un problema que ocurre una y otra vez en nuestro entorno, y luego describe la esencia de la solución de ese problema, de tal manera en que se puede utilizar esta solución más de un millón de veces sin hacerlo igual siquiera dos veces”

-- [Christopher Alexander](https://es.wikipedia.org/wiki/Christopher_Alexander)
```

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
:
: - Singleton
: - Factory Method
: - Abstract Factory

Patrones estructurales
: Se ocupan de la composición de clases y objetos para formar estructuras más grandes. Ejemplos:
:
: - Adapter
: - Composite
: - Decorator

Patrones de comportamiento
: Se enfocan en la interacción y responsabilidad entre objetos. Ejemplos:
:
: - Observer
: - Strategy
: - Command

Veremos con más profundidad algunos de estos patrones.

## Patrón _Adapter_

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronAdapter.svg
---
name: adapter
---
Patrón _Adapter_
```

El patrón _adapter_ permite reutilizar código heredado o _legacy_ cuya interfaz no coincide con la esperada por el sistema en el que estamos trabajando. Este patrón actúa como un puente entre la interfaz existente y la requerida, permitiendo que componentes incompatibles trabajen juntos sin modificar su código original heredado.

En la figura a continuación se observan los siguientes componentes.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronAdapter2_light.svg
---
class: only-light-mode
---
Diagrama de Clases del Patrón _Adapter_
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronAdapter2_dark.svg
---
class: only-dark-mode
---
Diagrama de Clases del Patrón _Adapter_
```

Cliente
: Representa el sistema nuevo que espera una interfaz específica. En este ejemplo se observa que el cliente espera una interfaz que tiene el método `request()`.

Interfaz
: Define la interfaz esperada por el sistema nuevo.

Adaptado
: Representa la clase existente con la interfaz incompatible. En este ejemplo se observa que cuenta con el método `specificRequest()`.

Adaptador
: Convierte la interfaz del _Adaptado_. Dentro del método `request()` en el _Adaptador_ se invoca el método específico del _Adaptado_ `specificRequest()`. Eventualmente puede realizar alguna transformación de datos o invocar otros métodos del _Adaptado_ para conseguir que `request()` cumpla con la interfaz esperada.

### Cómo Proceder

1. Identificar los actores en juego: el _**Cliente**_ y el _**Adaptado**_ (componente _legacy_).
2. Identificar la _**Interfaz**_ que requiere el _**Cliente**_.
3. Verificar que el _**Adaptado**_ que se quiere utilizar puede cumplir con la _**Interfaz**_ solicitada.
4. Diseñar un envoltorio (_**Adaptador**_) que va a contener al _**Adaptado**_.
5. Implementar el _**Adaptador**_ para que cumpla con la _**Interfaz**_ esperada por el _**Cliente**_.
6. El _**Cliente**_ interactúa con el _**Adaptador**_ como si fuera el _**Adaptado**_.

### Ejemplo

Supongamos que tenemos un robot que realiza mediciones, cuyo sistema de control proporciona los métodos `Medir()` que devuelve un par de enteros, donde el primer número representa la distancia en metros y el segundo número la distancia en centímetros. Por ejemplo si la última medición fue de 10,5 m, entonces `Medir()` devolverá el par `(10, 50)`.

Nuestra empresa ha concretado la venta del robot a un cliente que necesita incorporar el robot a su sistema de producción, pero el sistema de control del cliente espera que el método `Medir` devuelva un solo número que represente la distancia en pulgadas.

1. Identificar los actores en juego: el _**Cliente**_ y el _**Adaptado**_ (componente _legacy_).

   - _**Cliente**_: Sistema de control del cliente.
   - _**Adaptado**_: Robot que realiza mediciones.

2. Identificar la _**Interfaz**_ que requiere el _**Cliente**_.

   - _**Interfaz**_: Método `Medir()` que devuelve la distancia en pulgadas.

3. Verificar que el _**Adaptado**_ que se quiere utilizar puede cumplir con la _**Interfaz**_ solicitada.

   - _**Adaptado**_: Robot que realiza mediciones con el método `Medir()` que devuelve la distancia en metros y centímetros y se puede convertir a pulgadas.

4. Diseñar un envoltorio (_**Adaptador**_) que va a contener al _**Adaptado**_.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Adaptador que convierte la interfaz del Adaptado a la interfaz esperada
   type RobotAdaptado struct {
       adaptado *Robot
   }
   ```

5. Implementar el _**Adaptador**_ para que cumpla con la _**Interfaz**_ esperada por el _**Cliente**_.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Implementación del método requerido por la interfaz esperada
   func (r *RobotAdaptado) Medir() float64 {
       metros, centimetros := r.adaptado.Medir()
       totalCentimetros := (metros * 100) + centimetros
       pulgadas := float64(totalCentimetros) / 2.54
       return pulgadas
   }
   ```

6. El _**Cliente**_ interactúa con el _**Adaptador**_ como si fuera el _**Adaptado**_.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Cliente
   robot := &Robot{}
   adaptado := &RobotAdaptado{adaptado: robot}
   distancia := adaptado.Medir()
   fmt.Println(distancia) // distancia en pulgadas
   ```

   En este ejemplo, el _**Adaptador**_ `RobotAdaptado` convierte la interfaz del `Robot` en la interfaz requerida por el _**Cliente**_, permitiendo que el sistema de control del cliente pueda utilizar el robot para realizar mediciones **sin modificar el código original** del robot.

## Patrón _Composite_

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronComposite.svg
---
name: composite
---
Patrón _Composite_
```

El patrón _composite_ permite tratar tanto a objetos individuales como a composiciones de objetos de manera uniforme. Esto significa que se pueden tratar tanto a un objeto simple como a un grupo de objetos de la misma manera, sin tener que distinguir entre ellos. Esto simplifica el diseño y la implementación de estructuras jerárquicas de objetos.

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronComposite2_light.svg
---
class: only-light-mode
---
Diagrama de Clase del Patrón _Composite_
```

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronComposite2_dark.svg
---
class: only-dark-mode
---
Diagrama de Clase del Patrón _Composite_
```

Componente
: Define la interfaz común para todos los elementos de la estructura.

Simple
: Representa los elementos individuales de la estructura.

Compuesto
: Representa los elementos que contienen otros elementos. Puede contener tanto objetos _Simples_ como _Compuestos_. Se debe prever un método para agregar elementos a la colección, ya sea elementos _Simple_ o _Compuesto_.

### Cómo Proceder

1. Definir una interfaz común para todos los elementos de la estructura (_**Componente**_).
2. Implementar los tipos de datos que representen los elementos individuales (_**Simple**_), asegurándose de que cumplan con la interfaz común (_**Componente**_).
3. Implementar los tipos de datos que representen los elementos compuestos (_**Compuesto**_), que contienen una colección de elementos (_**Componente**_), asegurándose de que cumplan con la interfaz común (_**Componente**_) y contemplen la posibilidad de agregar elementos a la colección.
4. Tratar tanto a los elementos simples como a los compuestos de manera uniforme, sin tener que distinguir entre ellos.

### Ejemplo

Supongamos que queremos modelar un sistema de archivos. Cada elemento del sistema —ya sea un archivo individual o una carpeta que contiene otros elementos— debe poder reportar su tamaño total en bytes. Queremos calcular el tamaño de una carpeta que puede contener archivos y otras carpetas, sin tener que distinguir entre ellos.

1. Definir una interfaz común para todos los elementos de la estructura (_**Componente**_).

   ```{code-block} go
   ---
   linenos: true
   ---
   // Componente define la operación común a archivos y carpetas
   type Componente interface {
       Tamanio() int64
   }
   ```

2. Implementar los tipos de datos que representen los elementos individuales (_**Simple**_), asegurándose de que cumplan con la interfaz común (_**Componente**_).

   ```{code-block} go
   ---
   linenos: true
   ---
   // Archivo representa un elemento simple (hoja) del sistema
   type Archivo struct {
       nombre string
       bytes  int64
   }

   func (a *Archivo) Tamanio() int64 {
       return a.bytes
   }
   ```

3. Implementar los tipos de datos que representen los elementos compuestos (_**Compuesto**_), que contienen una colección de elementos (_**Componente**_), asegurándose de que cumplan con la interfaz común (_**Componente**_) y contemplen la posibilidad de agregar elementos a la colección.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Carpeta representa un elemento compuesto que contiene otros componentes
   type Carpeta struct {
       nombre      string
       componentes []Componente
   }

   func (c *Carpeta) Tamanio() int64 {
       var total int64
       for _, comp := range c.componentes {
           total += comp.Tamanio()
       }
       return total
   }

   func (c *Carpeta) Agregar(comp Componente) {
       c.componentes = append(c.componentes, comp)
   }
   ```

4. Tratar tanto a los elementos simples como a los compuestos de manera uniforme, sin tener que distinguir entre ellos.

   Por ejemplo, queremos calcular el tamaño total de un directorio de proyecto que contiene archivos y subcarpetas:

   ```{code-block} go
   ---
   linenos: true
   ---
   readme := &Archivo{nombre: "README.md", bytes: 2048}
   licencia := &Archivo{nombre: "LICENSE", bytes: 1024}

   src := &Carpeta{nombre: "src"}
   src.Agregar(&Archivo{nombre: "main.go", bytes: 4096})
   src.Agregar(&Archivo{nombre: "utils.go", bytes: 1536})

   docs := &Carpeta{nombre: "docs"}
   docs.Agregar(&Archivo{nombre: "manual.pdf", bytes: 524288})

   proyecto := &Carpeta{nombre: "mi-proyecto"}
   proyecto.Agregar(readme)
   proyecto.Agregar(licencia)
   proyecto.Agregar(src)
   proyecto.Agregar(docs)

   fmt.Println(proyecto.Tamanio()) // 532992
   ```

   `proyecto.Tamanio()` recorre recursivamente todos los componentes —archivos y carpetas— sin necesidad de saber si cada uno es simple o compuesto. El método `Agregar` recibe un `Componente`, por lo que acepta tanto `Archivo` como `Carpeta`.

## Patrón _Iterator_

```{figure} ../_static/figures/4-diseno-de-algoritmos/4-2-patrones-de-diseno/PatronIterator.svg
---
name: iterator
---
Patrón _Iterator_
```

El patrón _Iterator_ o Iterador permite recorrer los elementos de una colección cualquiera sin exponer su estructura interna. El Iterador provee una interfaz uniforme con dos métodos:

`Siguiente() bool`
: Avanza el iterador al siguiente elemento y devuelve `true`. Si no quedan más elementos por recorrer, devuelve `false`. La primera llamada a `Siguiente()` posiciona el iterador en el primer elemento de la colección.

`Valor() int`
: Devuelve el valor del elemento sobre el cual está posicionado el iterador. Solo debe llamarse después de que `Siguiente()` haya devuelto `true`.

El patrón de uso típico en Go es:

```{code-block} go
---
linenos: true
---
it := coleccion.Iterador()
for it.Siguiente() {
    fmt.Println(it.Valor())
}
```

Cada llamada a `Siguiente()` cumple dos funciones: verifica si hay un elemento disponible y avanza la posición interna. `Valor()` simplemente retorna el elemento actual sin modificar el estado del iterador.

### Cómo Proceder

1. Definir el comportamiento del **Iterador** con los métodos `Siguiente()` y `Valor()`. Si se necesita recorrer en ambos sentidos, se puede agregar un método `Anterior()`.
2. Dentro de la **colección** definir un método fábrica `Iterador()` que devuelva un iterador nuevo apuntando al inicio.
3. Implementar el **Iterador** vinculado siempre a una única colección.
4. Recorrer la **colección** con `for it.Siguiente()`.

### Ejemplo

Supongamos que tenemos una lista enlazada simple y queremos recorrerla con un iterador. Por simplicidad la lista contiene solo números enteros.

Primero definimos la estructura de la lista y su operación de inserción al final:

```{code-block} go
---
linenos: true
---
type Nodo struct {
    valor int
    sig   *Nodo
}

type Lista struct {
    cabeza *Nodo
}

func (l *Lista) AgregarAlFinal(valor int) {
    nuevo := &Nodo{valor: valor}
    if l.cabeza == nil {
        l.cabeza = nuevo
        return
    }
    actual := l.cabeza
    for actual.sig != nil {
        actual = actual.sig
    }
    actual.sig = nuevo
}
```

El iterador se implementa como un struct que mantiene una referencia al nodo actual:

```{code-block} go
---
linenos: true
---
type Iterador struct {
    actual *Nodo
}

func (l *Lista) Iterador() *Iterador {
    return &Iterador{actual: l.cabeza}
}

// Siguiente avanza al próximo nodo.
// La primera llamada posiciona el iterador en la cabeza.
// Devuelve false cuando no hay más elementos.
func (it *Iterador) Siguiente() bool {
    if it.actual == nil {
        return false
    }
    // La primera vez, no avanza: devuelve la cabeza.
    // Las siguientes, avanza al nodo siguiente.
    if it.actual != nil {
        // guardamos el actual y avanzamos
    }
    return true
}

// Valor devuelve el valor del nodo actual.
func (it *Iterador) Valor() int {
    return it.actual.valor
}
```

El código anterior es una simplificación. La implementación real necesita un mecanismo para distinguir la primera llamada de las siguientes. A continuación la versión completa:

```{code-block} go
---
linenos: true
---
type Iterador struct {
    actual  *Nodo
    primera bool
}

func (l *Lista) Iterador() *Iterador {
    return &Iterador{actual: l.cabeza, primera: true}
}

func (it *Iterador) Siguiente() bool {
    if it.actual == nil {
        return false
    }
    if !it.primera {
        it.actual = it.actual.sig
        if it.actual == nil {
            return false
        }
    }
    it.primera = false
    return true
}

func (it *Iterador) Valor() int {
    return it.actual.valor
}
```

La bandera `primera` evita que la llamada inicial a `Siguiente()` avance más allá del primer elemento. A partir de la segunda llamada, `Siguiente()` avanza al nodo siguiente antes de verificar si hay elemento.

Finalmente, el uso:

```{code-block} go
---
linenos: true
---
lista := &Lista{}
lista.AgregarAlFinal(1)
lista.AgregarAlFinal(2)
lista.AgregarAlFinal(3)

it := lista.Iterador()
for it.Siguiente() {
    fmt.Println(it.Valor())
}
// Salida:
// 1
// 2
// 3
```

## Ejercicios

Los ejercicios de este capítulo cubren los tres patrones vistos: **Adapter**, **Composite** e **Iterator**. Están en el directorio
`02-patrones-de-diseno/ejercicios/`
del repositorio
`taller-algoritmos`.
Cada ejercicio tiene un esqueleto con `// Completar` y su correspondiente batería de tests.
Para resolverlos, clonar el repositorio, completar las funciones y ejecutar `go test ./...`.
