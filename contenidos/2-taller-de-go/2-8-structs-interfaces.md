---
label: structs-interfaces
---

# Estructuras e interfaces

## _Structs_

En Go las _structs_ son colecciones de campos. A diferencia de las clases en Java, una `struct` no soporta herencia, no tiene constructores explícitos ni métodos *static*. Sin embargo, puede tener métodos asociados (como veremos en breve) y puede incrustar otras _structs_ como forma de composición. Podríamos pensar una `struct` como una clase liviana que agrupa datos, sin el peso de un sistema de herencia ni la maquinaria de POO tradicional.

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

Para acceder a un campo de una estructura se usa la notación de punto, como lo hacemos para acceder a un atributo en Java. También podemos declarar una variable de tipo `struct` de forma literal.

```go
func main() {
    var p1 Persona
    p1.nombre = "Marcelo"
    p1.edad = 27

    p2 := Persona{nombre: "Laura", apellido: "Medina", edad: 25}

    fmt.Println(p1.nombre, p1.edad)
    fmt.Println(p2.nombre, p2.apellido)
}
```
```output
Marcelo 27
Laura Medina
```

### Métodos

Go no tiene clases como Java; sin embargo, permite definir métodos sobre ciertos tipos.

Un método es una función con un argumento especial **receptor**. El **receptor** aparece en su propia lista de argumentos entre la palabra clave `func` y el nombre del método.

```go
func (p Persona) NombreCompleto() string {
    return p.nombre + " " + p.apellido
}

func (p *Persona) CumplirAnios() {
    p.edad++
}
```

En este ejemplo, `NombreCompleto` tiene un receptor de tipo `Persona` llamado `p`. Al ser un receptor por valor, no modifica el original, solo accede a los campos. `CumplirAnios` tiene un receptor de tipo `*Persona` (puntero a `Persona`), necesario porque modifica el campo `edad`.

```go
func main() {
    p := Persona{nombre: "Ana", apellido: "López", edad: 30}
    fmt.Println(p.NombreCompleto())
    p.CumplirAnios()
    fmt.Println(p.edad)
}
```
```output
Ana López
31
```

### Punteros a *struct*

Podemos declarar una variable que sea un puntero a una estructura:

```go
func main() {
    p := &Persona{nombre: "Laura", apellido: "Medina", edad: 25}
    fmt.Println(p.nombre)  // equivalente a (*p).nombre
    p.nombre = "María"
    fmt.Println(p.nombre)
}
```
```output
Laura
María
```

Go permite acceder a los campos sin dereferenciar explícitamente el puntero. `p.nombre` equivale a `(*p).nombre`. Es azúcar sintáctico.

Los punteros a struct son útiles para:
- Evitar copiar la estructura al pasarla como parámetro
- Poder modificar los campos desde otra función o método

### Receptores: puntero vs. valor

| Receptor valor | Receptor puntero |
|---|---|
| No modifica el original | Modifica el original |
| Copia la *struct* | No copia (más eficiente) |
| Útil para consultas | Útil para mutaciones |

Go aplica azúcar sintáctico: si definimos un método con receptor puntero y lo llamamos sobre una variable no puntero, Go lo convierte automáticamente.

```go
func main() {
    p := Persona{nombre: "Ana", edad: 30}
    p.CumplirAnios()       // Go lo trata como (&p).CumplirAnios()
    fmt.Println(p.edad)    // 31
}
```
```output
31
```

Regla práctica: usar receptor puntero cuando el método modifica el receptor o cuando la *struct* es grande; usar receptor valor para consultas que no modifican estado.

### ¿Métodos de clase?

Go no tiene un equivalente directo a *static* de Java ni métodos de clase. Para simular este comportamiento se utilizan **funciones del paquete**. Por convención, suelen llamarse `New<Tipo>`:

```go
func NewPersona(nombre, apellido string, edad uint) Persona {
    return Persona{
        nombre:   nombre,
        apellido: apellido,
        edad:     edad,
    }
}

func main() {
    p := NewPersona("Laura", "Medina", 25)
    fmt.Println(p.nombre, p.apellido, p.edad)
}
```
```output
Laura Medina 25
```

Estas funciones reemplazan el rol de los constructores o fábricas estáticas.

## Interfaces

Como mencionamos anteriormente, en Go existe el concepto de interfaces, pero estas funcionan de forma algo diferente a como lo hacen en Java.

Un tipo `interface` se define como un conjunto de firmas de método[^firma]. Un valor de ese tipo de interfaz puede contener cualquier valor que implemente todos esos métodos.

[^firma]: Una **firma de método** (o firma de función) es la declaración de su nombre, parámetros y tipo de retorno, sin incluir el cuerpo. Por ejemplo, en `func (p *Persona) Avanzar(pasos int)`, la firma es `Avanzar(pasos int)`. La implementación (el cuerpo) no forma parte de la firma.

### Implementación de interfaces

En Go la implementación es **implícita** (o estructural): no hace falta declarar `implements`. Un tipo implementa una interfaz simplemente teniendo los métodos que la interfaz exige.

```go
type Caminante interface {
    Avanzar(pasos int)
    Girar(grados float32)
}

func (p *Persona) Avanzar(pasos int) {
    fmt.Printf("%s avanzó %d pasos\n", p.nombre, pasos)
}

func (p *Persona) Girar(grados float32) {
    fmt.Printf("%s giró %.1f grados\n", p.nombre, grados)
}
```

Como `*Persona` implementa ambos métodos, automáticamente satisface la interfaz `Caminante`. Esto significa que una variable de tipo `*Persona` puede usarse donde se espere un `Caminante`.

```go
func RealizarRecorrido(caminante Caminante) {
    caminante.Avanzar(5)
    caminante.Girar(180)
}

func main() {
    p := Persona{nombre: "Marcelo"}
    RealizarRecorrido(&p)
}
```
```output
Marcelo avanzó 5 pasos
Marcelo giró 180.0 grados
```

Notar que pasamos `&p` porque los métodos están definidos sobre `*Persona`, no sobre `Persona`.

Veamos otro tipo que también implemente `Caminante`:

```go
type Perro struct {
    nombre string
}

func (perro *Perro) Avanzar(pasos int) {
    fmt.Printf("%s avanzó %d pasos\n", perro.nombre, pasos)
}

func (perro *Perro) Girar(grados float32) {
    fmt.Printf("%s giró %.1f grados\n", perro.nombre, grados)
}
```

Tanto `*Persona` como `*Perro` implementan `Caminante`. Podemos escribir una misma función que trabaje con cualquiera de los dos:

```go
func HacerCaminar(c Caminante) {
    c.Avanzar(10)
    c.Girar(90)
}

func main() {
    HacerCaminar(&Persona{nombre: "Ana"})
    HacerCaminar(&Perro{nombre: "Rex"})
}
```
```output
Ana avanzó 10 pasos
Ana giró 90.0 grados
Rex avanzó 10 pasos
Rex giró 90.0 grados
```

La función `HacerCaminar` acepta cualquier tipo que implemente `Caminante`, sin importar su tipo concreto. Esto es **polimorfismo**: un mismo contrato (`Caminante`) es satisfecho por distintos tipos, y el código que usa la interfaz funciona igual para todos.

### Implementación de varias interfaces

Un mismo tipo puede implementar varias interfaces a la vez.

```go
type Trabajador interface {
    Trabajar(horas int) string
}

func (p *Persona) Trabajar(horas int) string {
    return fmt.Sprintf("%s trabajó %d horas", p.nombre, horas)
}

func main() {
    p := Persona{nombre: "Laura"}
    fmt.Println(p.Trabajar(8))
}
```
```output
Laura trabajó 8 horas
```

Ahora `*Persona` implementa tanto `Caminante` como `Trabajador`.

### Variables de tipo interfaz

Una variable declarada con un tipo interfaz puede almacenar cualquier valor que la implemente.

```go
func main() {
    ana := Persona{nombre: "Ana", apellido: "López", edad: 30}

    var c Caminante = &ana
    c.Avanzar(5)

    var t Trabajador = &ana
    fmt.Println(t.Trabajar(8))
}
```
```output
Ana avanzó 5 pasos
Ana López trabajó 8 horas
```

Una misma variable concreta (`ana`) puede verse a través de distintas interfaces: como `Caminante` para moverse o como `Trabajador` para trabajar. Esto es polimorfismo: el código que usa la interfaz queda desacoplado del tipo concreto.

## Ejercicios

Implementá un sistema de figuras geométricas en un solo archivo:

1. Definí un *struct* `Punto` con campos `X` e `Y` de tipo `float64`. Implementá una función `NewPunto(x, y float64) Punto`.

2. Definí una interfaz `Figura` con los métodos `Area() float64` y `Perimetro() float64`.

3. Creá un *struct* `Rectangulo` con dos puntos: `EsqInfIzq` y `EsqSupDer`. Implementá `NewRectangulo(infIzq, supDer Punto) Rectangulo` y los métodos de `Figura`.

4. Creá un *struct* `Circulo` con `Centro` (`Punto`) y `Radio` (`float64`). Implementá `NewCirculo(centro Punto, radio float64) Circulo` y los métodos de `Figura` usando `math.Pi`.

5. Creá un *struct* `Cuadrado` que incruste (`embedding`) un `Rectangulo`. Implementá `NewCuadrado(infIzq Punto, lado float64) Cuadrado`. `Cuadrado` usa `Area()` y `Perimetro()` de `Rectangulo` mediante la promoción de métodos del *embedding*.

6. Escribí un `main` que cree un `Rectangulo` de (0,0) a (3,4), un `Circulo` con centro en (0,0) y radio 5, y un `Cuadrado` desde (0,0) de lado 4. Almacenalos en `[]Figura` e imprimí área y perímetro de cada uno.

```go
// Salida esperada:
// Rectángulo: área = 12, perímetro = 14
// Círculo: área = 78.54, perímetro = 31.42
// Cuadrado: área = 16, perímetro = 16
```

Los esqueletos de estos ejercicios están en `08-structs-interfaces/ejercicios/figuras/` del repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git).
