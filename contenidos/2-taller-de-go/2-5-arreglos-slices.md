---
label: arreglos-slices
---

# Arreglos y Slices

## Arreglos

En Go, los arreglos o _arrays_ son estructuras de datos que almacenan una cantidad arbitraria de valores **del mismo tipo**. A nivel de memoria, todos sus elementos se encuentran en posiciones contiguas.

El tamaño de un _array_ es definido al momento de su creación y determina su "tipo". Es decir, un array de enteros de 7 elementos tiene un tipo diferente a un array de enteros de 3 elementos.

Podemos declarar un array de la siguiente forma:

```{code-block} go
---
linenos:
---
var numeros [7]int
```

Aquí creamos una variable de tipo `[7]int` a la que referenciaremos con el nombre `numeros`.

Para acceder a los elementos de un arreglo o modificarlos, utilizamos su índice. Tal como sucede en la mayoría de los lenguajes de programación, los índices en Go comienzan en `0` y terminan en `largo - 1`.

```{code-block} go
---
linenos:
---
numeros[0] = 42
numeros[3] = 1337

fmt.Println(numeros[0] + numeros[3])
```

```output
1379
```

En el caso de un _array_ de 7 elementos, podremos acceder a los elementos en los índices desde el `0` hasta el `6` inclusive. Intentar acceder a un índice fuera de este rango va a causar un error.

```{code-block} go
---
linenos:
---
numeros[7]
```

```output
panic: runtime error: index out of range [7] with length 7
```

A diferencia de los _slices_ que veremos más adelante, cuando un _array_ es pasado como argumento en una función o método, este se pasa por **valor**. Es decir, se crea una copia completa del arreglo, por lo que las modificaciones dentro de la función no afectan al arreglo original (a menos que usemos punteros).

En Go para conocer el largo de un _array_ existe la función `len`.

```{code-block} go
---
linenos:
---
len(numeros)
```

```output
7
```

Para recorrer un _array_ en Go existe la instrucción `range`, que genera un iterador sobre el array devolviendo el índice (`i`) y el valor (`v`), en cada iteración del `for`. Veamos un ejemplo:

```{code-block} go
---
linenos:
---
nombres := [4]string{"Fabián", "Martín", "Valeria", "Santiago"}

for i, v := range nombres {
    fmt.Println(i, "|", v)
}
```

```output
0 | Fabián
1 | Martín
2 | Valeria
3 | Santiago
```

## _Slices_

Los _slices_ (o tajadas) en castellano representan secuencias de longitud variable cuyos elementos son del mismo tipo. Un tipo de _slice_ se escribe como `[]T`, donde los elementos son de tipo `T`; se asemeja a un tipo de _array_ sin tamaño.

Los _arreglos_ y los _slices_ están estrechamente relacionados. Un _slice_ es una estructura de datos ligera que da acceso a una subsecuencia (o a todos) los elementos de un arreglo. Ese arreglo se conoce como el **arreglo subyacente** del _slice_.

Un _slice_ tiene tres componentes internos:

- **puntero**: apunta al primer elemento del arreglo accesible desde el _slice_ (no necesariamente el elemento 0 del arreglo)
- **longitud** (`len`): cantidad de elementos que contiene el _slice_
- **capacidad** (`cap`): cantidad máxima de elementos disponibles desde esa posición hasta el final del arreglo subyacente

La longitud no puede superar la capacidad. Las funciones `len` y `cap` devuelven estos valores para cualquier _slice_.

Podemos imaginar que un _slice_ es como una ventana que podemos deslizar sobre un arreglo y nos permite acceder a una parte del mismo.

```{code-block} go
---
linenos:
---
var s []byte
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-struct_light.svg
---
class: only-light-mode
width: 200px
---
Estructura interna de un _slice_.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-struct_dark.svg
---
class: only-dark-mode
width: 200px
---
Estructura interna de un _slice_.
```

```{code-block} go
---
linenos:
---
s = make([]byte, 5, 5)
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-1_light.svg
---
class: only-light-mode
---
_Slice_ de longitud 5 y capacidad 5: El arreglo subyacente tiene tamaño 5 y la ventana del slice "ve" todo el arreglo.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-1_dark.svg
---
class: only-dark-mode
---
_Slice_ de longitud 5 y capacidad 5: El arreglo subyacente tiene tamaño 5 y la ventana del slice "ve" todo el arreglo.
```

A medida que hacemos _slicing_ de `s`, observamos los cambios en la estructura de datos del _slice_ y su relación con el arreglo subyacente:

```{code-block} go
---
linenos:
---
s = s[2:4]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-2_light.svg
---
class: only-light-mode
---
_Slice_ de longitud 2 y capacidad 3: La ventana del slice ahora ve desde la posición 2 del arreglo subyacente hasta la posición 3 (longitud 2, el último elemento no se incluye). Sin embargo, la capacidad es 3, lo que indica que el slice todavía puede crecer una posición más sobre el mismo arreglo.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-2_dark.svg
---
class: only-dark-mode
---
_Slice_ de longitud 2 y capacidad 3: La ventana del slice ahora ve desde la posición 2 del arreglo subyacente hasta la posición 3 (longitud 2, el último elemento no se incluye). Sin embargo, la capacidad es 3, lo que indica que el slice todavía puede crecer una posición más sobre el mismo arreglo.
```

El _slicing_ no copia los datos del _slice_. En su lugar, crea un nuevo valor de _slice_ que apunta a otra porción del arreglo original. Esto hace que las operaciones con _slices_ sean tan eficientes como manipular índices de arreglos. Modificar los elementos de un _slice_ modifica los elementos del arreglo subyacente:

```{code-block} go
---
linenos:
---
s = s[:cap(s)]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-3_light.svg
---
class: only-light-mode
---
_Slice_ de longitud 3 y capacidad 3: Ahora la ventana del slice se agrandó y ve desde la posición 2 hasta el final del arreglo subyacente.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-3_dark.svg
---
class: only-dark-mode
---
_Slice_ de longitud 3 y capacidad 3: Ahora la ventana del slice se agrandó y ve desde la posición 2 hasta el final del arreglo subyacente.
```

Múltiples _slices_ pueden compartir el mismo array subyacente y pueden referirse a partes superpuestas de ese array. La siguiente figura muestra un array de cadenas para los meses del año y dos _slices_ superpuestos de este. El array se declara como:

```{code-block} go
---
linenos:
---
meses := [12]string{"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}
```

El operador _slice_ `s[i:j]` crea un nuevo _slice_ con los elementos desde `i` hasta `j-1` del _array_ o _slice_ `s`, donde $0 \leq i \leq j \leq \texttt{cap(s)}$ y el resultado tiene `j-i` elementos. Si se omite `i`, se toma 0; si se omite `j`, se toma `len(s)`.

Sobre `meses`, podemos crear slices que referencien subconjuntos. Por ejemplo:

- `meses[0:12]` y `meses[:]` abarcan **todos** los meses
- `meses[1:]` abarca de Febrero a Diciembre

Definamos slices superpuestos para el segundo trimestre y el invierno:

```{code-block} go
---
linenos:
---
t2 := meses[3:6]
invierno := meses[5:8]
```

```{code-block} go
---
linenos:
---
fmt.Println("t2 =", t2, "\ninvierno =", invierno)
```

```output
t2 = [Abril Mayo Junio]
invierno = [Junio Julio Agosto]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/overlapping-slices_light.svg
---
class: only-light-mode
---
Dos _slices_ sobre el mismo array de meses.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/overlapping-slices_dark.svg
---
class: only-dark-mode
---
Dos _slices_ sobre el mismo array de meses.
```

Hacer _slicing_ más allá de `cap(s)` causa un pánico, pero hacer _slicing_ más allá de `len(s)` extiende el _slice_, por lo que el resultado puede ser más largo que el original:

```{code-block} go
---
linenos:
---
fmt.Println(invierno[:20])
```

```output
panic: runtime error: slice bounds out of range [:20] with capacity 7
```

```{code-block} go
---
linenos:
---
inviernoSinFin := invierno[:5]
fmt.Println(inviernoSinFin)
```

```output
[Junio Julio Agosto Septiembre Octubre]
```

### Agregando elementos a un _slice_

Para agregar elementos a un _slice_ se usa la función `append`. Esta recibe un _slice_ y uno o más elementos del mismo tipo, y devuelve un nuevo _slice_ con todos los elementos originales más los nuevos.

Si el _slice_ resultante entra en la capacidad actual, `append` reutiliza el mismo arreglo subyacente. Si no entra, `append` crea un nuevo arreglo subyacente con capacidad aproximadamente el doble de la original, copia todos los elementos y luego agrega los nuevos.

```{code-block} go
---
linenos:
---
s := []int{1, 2, 3}
fmt.Println(s, "\nlen =", len(s), "\ncap =", cap(s))
```

```output
[1 2 3]
len = 3
cap = 3
```

```{code-block} go
---
linenos:
---
s = append(s, 4, 5)
fmt.Println(s, "\nlen =", len(s), "\ncap =", cap(s))
```

```output
[1 2 3 4 5]
len = 5
cap = 6
```

Puede darse el caso en el que, si tenemos dos _slices_ sobre un mismo _array_ subyacente, al agregar un elemento a uno de los _slices_, el otro también se vea modificado:

```{code-block} go
---
linenos:
---
x := make([]int, 0, 4)
x = append(x, 0, 1, 2)

y := x
y = append(y, 3)

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2]
y = [0 1 2 3]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-1_light.svg
---
class: only-light-mode
width: 50%
---
Slices x e y comparten el mismo arreglo subyacente.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-1_dark.svg
---
class: only-dark-mode
width: 50%
---
Slices x e y comparten el mismo arreglo subyacente.
```

```{code-block} go
---
linenos:
---
x = append(x, 4)

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 4]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-2_light.svg
---
class: only-light-mode
width: 50%
---
Modificar x también afecta a y al compartir el arreglo subyacente.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-2_dark.svg
---
class: only-dark-mode
width: 50%
---
Modificar x también afecta a y al compartir el arreglo subyacente.
```

También si el _slice_ sobre el que agregamos el nuevo elemento no tiene más capacidad para agregar elementos, se crea un nuevo _slice_ con aproximadamente el doble de capacidad y se copian los elementos del slice original:

```{code-block} go
---
linenos:
---
y = append(y, 4)

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 4 4]
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-3_light.svg
---
class: only-light-mode
---
Al superar la capacidad, y apunta a un nuevo arreglo subyacente.
```

```{figure} ../_static/figures/2-taller-de-go/2-5-arreglos-slices/slice-append-entangled-3_dark.svg
---
class: only-dark-mode
---
Al superar la capacidad, y apunta a un nuevo arreglo subyacente.
```

Cuando `y = append(y, 4)` superó la capacidad, `append` creó un nuevo arreglo subyacente para `y` y copió allí los elementos. El slice `x`, en cambio, sigue apuntando al arreglo subyacente original.

Por eso, modificar los valores de `y` ya no afecta a `x`:

```{code-block} go
---
linenos:
---
y[3] = 3

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 3 4]
```

## Ejercicios

Los ejercicios de este capítulo están en `05-arreglos-slices/ejercicios/`
del repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git).
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.

## Enlaces recomendados

- [Go Slices: usage and internals](https://go.dev/blog/slices-intro) - Un artículo que explica el uso y la estructura interna de los _slices_ en Go.
