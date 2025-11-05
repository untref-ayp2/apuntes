---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Patrones de Diseño

Los patrones de diseño son soluciones reutilizables para problemas comunes que surgen en el desarrollo de software. Estos patrones encapsulan buenas prácticas y ofrecen un enfoque probado para resolver problemas recurrentes, facilitando el diseño de sistemas más robustos y mantenibles.

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

Veremos en más profundidad algunos de estos patrones.

## Patrón _Adapter_

```{figure} ../assets/images/PatronAdapter.svg
---
name: adapter
---
Patrón _Adapter_
```

El patrón _adapter_ permite reutilizar código heredado o _legacy_ cuya interfaz no coincide con la esperada por el sistema en el que estamos trabajando. Este patrón actúa como un puente entre la interfaz existente y la requerida, permitiendo que componentes incompatibles trabajen juntos sin modificar su código original heredado.

En la figura {ref}`adapter2` se observan los siguientes componentes.

```{figure} ../assets/images/PatronAdapter2.svg
---
name: adapter2
---
Diagrama de Clases del Patrón _Adapter_
```

Cliente
: Representa el sistema nuevo que espera una interfaz específica. En este ejemplo se observa que el cliente espera una interfaz que tiene el método `request()`{l=go}.

Interfaz
: Define la interfaz esperada por el sistema nuevo.

Adaptado
: Representa la clase existente con la interfaz incompatible. En este ejemplo se observa que cuenta con el método `specifirequest()`{l=go}.

Adaptador
: Convierte la interfaz del _Adaptado_. Dentro del método `request()`{l=go} en el _Adapatador_ se invoca el método específico del _Adaptado_ `specificrequest()`{l=go}. Eventualmente puede realizar alguna transformación de datos o invocar otros métodos del _Adaptado_ para conseguir que `request()`{l=go} cumpla con la interfaz esperada.

### Cómo Proceder

1. Identificar los actores en juego: el _**Cliente**_ y el _**Adaptado**_ (componente _legacy_).
2. Identificar la _**Interfaz**_ que requiere el _**Cliente**_.
3. Verificar que el _**Adaptado**_ que se quiere utilizar puede cumplir con la _**Interfaz**_ solicitada.
4. Diseñar un envoltorio (_**Adaptador**_) que va a contener al _**Adaptado**_.
5. Implementar el _**Adaptador**_ para que cumpla con la _**Interfaz**_ esperada por el _**Cliente**_.
6. El _**Cliente**_ interactúa con el _**Adaptador**_ como si fuera el _**Adaptado**_.

### Ejemplo

Supongamos que tenemos un robot que realiza mediciones, cuyo sistema de control proporciona los métodos `Medir()`{l=go} que devuelve un par de enteros, donde el primer número representa la distancia en metros y el segundo número la distancia en centímetros. Por ejemplo si la última medición fue de 10,5 m, entonces `Medir()`{l=go} devolverá el par `(10, 50)`{l=go}.

Nuestra empresa ha concretado la venta del robot a un cliente que necesita incorporar el robot a su sistema de producción, pero el sistema de control del cliente espera que el método `Medir`{l=go} devuelva un solo número que represente la distancia en pulgadas.

1. Identificar los actores en juego: el _**Cliente**_ y el _**Adaptado**_ (componente _legacy_).

   - _**Cliente**_: Sistema de control del cliente.
   - _**Adaptado**_: Robot que realiza mediciones.

2. Identificar la _**Interfaz**_ que requiere el _**Cliente**_.

   - _**Interfaz**_: Método `Medir()`{l=go} que devuelve la distancia en pulgadas.

3. Verificar que el _**Adaptado**_ que se quiere utilizar puede cumplir con la _**Interfaz**_ solicitada.

   - _**Adaptado**_: Robot que realiza mediciones con el método `Medir()`{l=go} que devuelve la distancia en metros y centímetros y se puede convertir a pulgadas.

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

   En este ejemplo, el _**Adaptador**_ `RobotAdaptado`{l=go} convierte la interfaz del `Robot`{l=go} en la interfaz requerida por el _**Cliente**_, permitiendo que el sistema de control del cliente pueda utilizar el robot para realizar mediciones **sin modificar el código original** del robot.

## Patrón _Composite_

```{figure} ../assets/images/PatronComposite.svg
---
name: composite
---
Patrón _Composite_
```

El patrón _composite_ permite tratar tanto a objetos individuales como a composiciones de objetos de manera uniforme. Esto significa que se pueden tratar tanto a un objeto simple como a un grupo de objetos de la misma manera, sin tener que distinguir entre ellos. Lo que simplifica el diseño y la implementación de estructuras jerárquicas de objetos.

```{figure} ../assets/images/PatronComposite2.svg
---
name: composite2
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

Supongamos que queremos modelar una estructura jerárquica de figuras, donde los elementos pueden ser rectángulos, círculos o triángulos o grupos compuestos. Queremos poder calcular el área total de la estructura, independientemente de si se trata de un rectángulo individual o de un grupo de elementos.

1. Definir una interfaz común para todos los elementos de la estructura (_**Componente**_).

   ```{code-block} go
   ---
   linenos: true
   ---
   // Interfaz común para todos los elementos de la estructura
   type Figura interface {
       Area() float64
   }
   ```

2. Implementar los tipos de datos que representen los elementos individuales (_**Simple**_), asegurándose de que cumplan con la interfaz común (_**Componente**_).

   ```{code-block} go
   ---
   linenos: true
   ---
   // Implementación de los tipos de datos que representan los elementos individuales
   import "math"

   type Rectangulo struct {
       Base   float64
       Altura float64
   }

   func (r *Rectangulo) Area() float64 {
       return r.Base * r.Altura
   }

   type Circulo struct {
       Radio float64
   }

   func (c *Circulo) Area() float64 {
       return math.Pi * c.Radio * c.Radio
   }

   type Triangulo struct {
       Base   float64
       Altura float64
   }

   func (t *Triangulo) Area() float64 {
       return (t.Base * t.Altura) / 2
   }
   ```

3. Implementar los tipos de datos que representen los elementos compuestos (_**Compuesto**_), que contienen una colección de elementos (_**Componente**_), asegurándose de que cumplan con la interfaz común (_**Componente**_) y contemplen la posibilidad de agregar elementos a la colección.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Implementación de los tipos de datos que representan los elementos compuestos
   // que contienen una colección de elementos
   type Grupo struct {
       Figuras []Figura
   }

   func (g *Grupo) Area() float64 {
       var areaTotal float64
       for _, f := range g.Figuras {
           areaTotal += f.Area()
       }
       return areaTotal
   }

   func (g *Grupo) Agregar(f Figura) {
       g.Figuras = append(g.Figuras, f)
   }
   ```

4. Tratar tanto a los elementos simples como a los compuestos de manera uniforme, sin tener que distinguir entre ellos.

   Por ejemplo queremos calcular el área de un tren compuesto por una locomotora y dos vagones, cada uno con su respectiva estructura de figuras.

   ```{figure} ../assets/images/PatronTren.svg
   ---
   name: tren
   ---
   Tren Compuesto de Figuras
   ```

   ```{code-block} go
   ---
   linenos: true
   ---
   locomotora := &Grupo{}
   locomotora.Agregar(&Rectangulo{Base: 7, Altura: 3}) //cuerpo de la locomotora
   locomotora.Agregar(&Circulo{Radio: 1}) //rueda de la locomotora
   locomotora.Agregar(&Circulo{Radio: 1}) //rueda de la locomotora
   locomotora.Agregar(&Triangulo{Base: 2, Altura: 4}) //chimenea
   locomotora.Agregar(&Rectangulo{Base: 2, Altura: 3}) //cabina

   vagon1 := &Grupo{}
   vagon1.Agregar(&Rectangulo{Base: 7, Altura: 3}) //cuerpo del vagon
   vagon1.Agregar(&Circulo{Radio: 1}) //rueda del vagon
   vagon1.Agregar(&Circulo{Radio: 1}) //rueda del vagon

   vagon2 := &Grupo{}
   vagon2.Agregar(&Rectangulo{Base: 7, Altura: 3}) //cuerpo del vagon
   vagon2.Agregar(&Circulo{Radio: 1}) //rueda del vagon
   vagon2.Agregar(&Circulo{Radio: 1}) //rueda del vagon

   tren := &Grupo{}
   tren.Agregar(locomotora)
   tren.Agregar(vagon1)
   tren.Agregar(vagon2)

   fmt.Println("El área del tren es: ", tren.Area()) //91.84955592153875
   ```

## Patrón _Iterator_

```{figure} ../assets/images/PatronIterator.svg
---
name: iterator
---
Patrón Iterador
```

El patrón _Iterator_ o Iterador permite recorrer los elementos de una colección cualquiera sin exponer su estructura interna. El Iterador declara un conjunto de métodos o funciones para acceder secuencialmente a los elementos. Los métodos más comunes son:

`Primero()`{l=go}
: Se posiciona el iterador en el primer elemento de la colección

`Siguiente()`{l=go}
: Avanza el iterador al siguiente elemento

`HaySiguiente()`{l=go}
: Devuelve `true`{l=go} si todavía quedan elementos por recorrer en la colección o `false`{l=go} en caso contario

`Actual()`{l=go}
: Devuelve el elemento actual donde está el iterador

### Cómo Proceder

1. Definir el comportamiento del **Iterador**, es decir los métodos para obtener el siguiente, etc. Es posible agregar más métodos a los mencionados, por ejemplo si necesitamos un iterador que pueda avanzar y retroceder en su recorrido habrá que agregar los métodos correspondientes.
2. Dentro de la **colección** definir un método para crear el **Iterador**
3. Implementar el **Iterador** vinculado siempre a una única colección
4. Recorrer la **colección** con el iterador creado

### Ejemplo

Supongamos que tenemos una lista enlazada simple y nos interesa crear un iterador que nos permita recorrerla e imprimir cada elemento de la lista. Por simplicidad suponemos que la lista enlazada solo contiene números enteros.

```{code-block} go
---
linenos: true
---
type Nodo struct {
    Valor     int
    Siguiente *Nodo
}

type ListaEnlazada struct {
    Primero *Nodo
}

// Método para insertar un elemento al inicio de la lista
func (l *ListaEnlazada) InsertarAlInicio(valor int) {
    if l.Primero == nil {
        l.Primero = &Nodo{Valor: valor}
    } else {
        nuevoNodo := &Nodo{Valor: valor, Siguiente: l.Primero}
        l.Primero = nuevoNodo
    }
}
```

1. Definir el comportamiento del **Iterador**, es decir los métodos para obtener el siguiente, etc. Es posible agregar más métodos a los mencionados, por ejemplo si necesitamos un iterador que pueda avanzar y retroceder en su recorrido habrá que agregar los métodos correspondientes.

   ```{code-block} go
   ---
   linenos: true
   ---
   // Interfaz del Iterador
   // Define los métodos que debe implementar el iterador
   type Iterador interface {
       Primero()
       Siguiente()
       HaySiguiente() bool
       Actual() int
   }
   ```

2. Dentro de la **colección** definir un método para crear el **Iterador**

   ```{code-block} go
   ---
   linenos: true
   emphasize-lines: 20, 21, 22, 23
   ---
   type Nodo struct {
       Valor     int
       Siguiente *Nodo
   }

   type ListaEnlazada struct {
       Primero *Nodo
   }

   // Método para insertar un elemento al inicio de la lista
   func (l *ListaEnlazada) InsertarAlInicio(valor int) {
       if l.Primero == nil {
           l.Primero = &Nodo{Valor: valor}
       } else {
           nuevoNodo := &Nodo{Valor: valor, Siguiente: l.Primero}
           l.Primero = nuevoNodo
       }
   }

   // Método para crear un iterador de la lista
   func (l *ListaEnlazada) CrearIterador() Iterador {
       return &IteradorLista{lista: l, actual: l.Primero}
   }
   ```

3. Implementar el **Iterador** vinculado siempre a una única colección

   ```{code-block} go
   ---
   linenos: true
   ---
   type IteradorLista struct {
       lista  *ListaEnlazada
       actual *Nodo
   }

   func (i IteradorLista) Primero() {
       i.actual = i.lista.Primero
   }

   func (i IteradorLista) Siguiente() {
       i.actual = i.actual.Siguiente
   }

   func (i IteradorLista) HaySiguiente() bool {
       return i.actual != nil
   }

   func (i IteradorLista) Actual() int {
       return i.actual.Valor
   }
   ```

4. Recorrer la **colección** con el iterador creado

   ```{code-block} go
   ---
   linenos: true
   ---
   lista := &ListaEnlazada{}
   lista.InsertarAlInicio(3)
   lista.InsertarAlInicio(2)
   lista.InsertarAlInicio(1)

   iterador := lista.CrearIterador()
   for iterador.Primero(); iterador.HaySiguiente(); iterador.Siguiente() {
       fmt.Println(iterador.Actual(), " ")
   }
   ```

## Ejercicios

1. Dada la siguiente definición de una matriz de números enteros:

   ```{code-block} go
   ---
   linenos: true
   ---
   type Matriz struct {
       Filas int
       Columnas int
       Datos [][]int
   }
   ```

   - Implementar un iterador que permita recorrer la matriz fila por fila.
   - Implementar un iterador que permita recorrer la matriz columna por columna.

   Los iteradores deben implementar la interfaz 'Iterador' definida anteriormente.

2. Implementar un iterador para recorrer una lista enlazada doblemente, es decir que permita avanzar y retroceder en el recorrido de la lista.

   ```{code-block} go
   ---
   linenos: true
   ---
   type IteradorDoble interface {
       Anterior()
       Siguiente()
       HayAnterior() bool
       HaySiguiente() bool
   }
   ```
