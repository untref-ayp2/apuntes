---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Arreglos y Slices

## Arreglos

En Go los arreglos o _arrays_ son estructuras de datos que almanecenan una cantidad arbitraria de valores **del mismo tipo**. A nivel de memoria, todos sus elementos se encuentran en posiciones contiguas.

El tamaño de un array es definido al momento de su creación y determina su "tipo". Es decir, un array de 7 elementos tiene un tipo diferente a un array de 3.

Podemos declarar un array de la siguiente forma:

```go
var numeros [7]int
```

Aquí creamos una variable de tipo `[7]int`{l=go} a la que referenciaremos con el nombre `numeros`{l=go}.

La forma de acceder o modificar los valores en las distintas posiciones de un array es por medio del índice que indica la posición, como ya se ha visto en materias anteriores y como en la mayoría los lenguajes de programación (aunque no todos), empezando de `0` hasta el largo menos 1.

```go
numeros[0] = 42
numeros[3] = 1337

fmt.Println(numeros[0] + numeros[3])
```

```output
1379
```

En el caso, de un array de 7 elementos, podremos acceder a los elementos en los indices desde el `0` hasta el `6` inclusive. Intentar acceder a un índice fuera de este rango va a causar un error.

```go
numeros[7]
```

```output
panic: runtime error: index out of range [7] with length 7
```

Cuando un array es pasado como argumento en una función o método, este pasa por "referencia". Es decir, que la fución que recibe esa referencia tendrá la libertad de modifcar el contenido de dicho array.

En Go para conocer el largo de un array existe la función `len`{l=go}.

```go
len(numeros)
```

```output
7
```

Para recorrer un array en Go existe la instrucción `range`{l=go}, que genera un iterador sobre el array devolviendo el índice (`i`) y el valor (`v`), en cada iteración del `for`{l=go}, veamos un ejemplo:

```go
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

Los _slices_ representan secuencias de longitud variable cuyos elementos son del mismo tipo. Un tipo de _slice_ se escribe como `[]T`{l=go}, donde los elementos son de tipo `T`{l=go}; se asemeja a un tipo de _array_ sin tamaño.

Los _arreglos_ y los _slices_ están estrechamente relacionados. Un _slice_ es una estructura de datos ligera que da acceso a una subsecuencia (o quizás a todos) de los elementos de un arreglo, conocido como el arreglo subyacente de la _slice_. Una _slice_ tiene tres componentes: un **puntero**, una **longitud** y una **capacidad**. El puntero apunta al primer elemento del arreglo accesible a través de la _slice_, que no es necesariamente el primer elemento del arreglo. La longitud es el número de elementos de la _slice_; no puede exceder la capacidad, que generalmente es el número de elementos entre el inicio de la _slice_ y el final del arreglo subyacente. Las funciones integradas `len`{l=go} y cap devuelven estos valores.

```go
var s []byte
```

```{figure} ../assets/images/arreglos-slices/slice-struct.png
---
name: slice-struct
---
Estructura interna de un _slice_.
```

```go
s = make([]byte, 5, 5)
```

```{figure} ../assets/images/arreglos-slices/slice-1.png
---
name: slice-1
---
_Slice_ de longitud 5 y capacidad 5.
```

A medida que hacemos _slicing_ de `s`, observamos los cambios en la estructura de datos del _slice_ y su relación con el arreglo subyacente:

```go
s = s[2:4]
```

```{figure} ../assets/images/arreglos-slices/slice-2.png
---
name: slice-2
---
_Slice_ de longitud 2 y capacidad 3.
```

El _slicing_ no copia los datos del _slice_. En su lugar, crea un nuevo valor de _slice_ que apunta al arreglo original. Esto hace que las operaciones con _slices_ sean tan eficientes como manipular índices de arreglos. Por lo tanto, modificar los elementos (no el _slice_ en sí) de un _re-slice_ modifica los elementos del _slice_ original:

```go
s = s[:cap(s)]
```

```{figure} ../assets/images/arreglos-slices/slice-3.png
---
name: slice-3
---
_Slice_ de longitud 3 y capacidad 3.
```

Múltiples _slices_ pueden compartir el mismo array subyacente y pueden referirse a partes superpuestas de ese array. La Figura 4.1 muestra un array de cadenas para los meses del año y dos _slices_ superpuestos de este. El array se declara como:

```go
meses := [12]string{"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}
```

El operador slice `s[i:j]`{l=go}, donde $0 \leq i \leq j \leq \texttt{cap(s)}$, crea un nuevo slice que hace referencia a los elementos desde `i`{l=go} hasta `j-1`{l=go} de las secuencias, que pueden ser una variable de array, un puntero a un array, u otro slice. El slice resultante tiene `j-i`{l=go} elementos. Si se omite `i`{l=go}, su valor es 0, y si se omite `j`{l=go}, su valor es `len(s)`{l=go}. Así, el slice `months[0:12]`{l=go} hace referencia a todo el rango de meses válidos, al igual que el slice `months[1:]`{l=go}; el slice `months[:]`{l=go} hace referencia a todo el array. Definamos slices superpuestos para el segundo trimestre y el invierno:

```go
t2 := meses[3:6]
invierno := meses[5:8]
```

```go
fmt.Println("t2 =", t2, "\ninvierno =", invierno)
```

```output
t2 = [Abril Mayo Junio]
invierno = [Junio Julio Agosto]
```

```{figure} ../assets/images/arreglos-slices/overlaping-slices.drawio.svg
---
name: overlaping-slices
---
Dos _slices_ sobre el mismo array de meses.
```

Hacer _slicing_ más allá de `cap(s)`{l=go} causa un pánico, pero hacer _slicing_ más allá de `len(s)`{l=go} extiende el _slice_, por lo que el resultado puede ser más largo que el original:

```go
fmt.Println(invierno[:20])
```

```output
panic: runtime error: slice bounds out of range [:20] with capacity 7
```

```go
inviernoSinFin := invierno[:5]
fmt.Println(inviernoSinFin)
```

```output
[Junio Julio Agosto Septiembre Octubre]
```

### Agregando elementos a un _slice_

Para agregar elementos a un _slice_ se utiliza la función `append`{l=go}, que toma un _slice_ y uno o más elementos del mismo tipo que el _slice_ y devuelve un nuevo _slice_ que contiene todos los elementos del _slice_ original más los nuevos elementos. Si el _slice_ resultante es mayor que la capacidad del _slice_ original, `append`{l=go} crea un nuevo _slice_ que es el doble de grande, copia los elementos del _slice_ original y luego agrega los nuevos elementos:

```go
s := []int{1, 2, 3}
fmt.Println(s, "\nlen =", len(s), "\ncap =", cap(s))
```

```output
[1 2 3]
len = 3
cap = 3
```

```go
s = append(s, 4, 5)
fmt.Println(s, "\nlen =", len(s), "\ncap =", cap(s))
```

```output
[1 2 3 4 5]
len = 5
cap = 6
```

Puede darse el caso en el que si tenemos dos slices sobre un mismo array subyacente, al agregar un elemento a uno de los slices, el otro también se vea modificado:

```go
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

```{figure} ../assets/images/arreglos-slices/slice-append-entangled-1.drawio.svg
---
name: slice-append-entangled-1
---
```

```go
x = append(x, 4)

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 4]
```

```{figure} ../assets/images/arreglos-slices/slice-append-entangled-2.drawio.svg
---
name: slice-append-entangled-2
---
```

También si el _slice_ sobre el que agregamos el nuevo elemento, no tiene más capacidad para agregar elementos, se crea un nuevo _slice_ con el doble de capacidad y se copian los elementos del slice original:

```go
y = append(y, 4)

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 4 4]
```

```{figure} ../assets/images/arreglos-slices/slice-append-entangled-3.drawio.svg
---
name: slice-append-entangled-3
---
```

es importante notar que el array subyacente ya no es el mismo ya que el slice original fue copiado a un nuevo array, pero el segundo slice sigue apuntando al array subyacenter original. Si modificamos algunos de los valores de `y`{l=go}, no va a afectar a `x`{l=go}:

```go
y[3] = 3

fmt.Println("x =", x, "\ny =", y)
```

```output
x = [0 1 2 4]
y = [0 1 2 3 4]
```

## Ejercicios

1. Escriba una función `invertir`{l=go} que invierta un slice. Por ejemplo, el slice `[1, 2, 3, 4]`{l=go} invertido sería `[4, 3, 2, 1]`{l=go}.
2. Escriba una función `rotar`{l=go} que rote un slice en un número `n`{l=go} de posiciones. Por ejemplo, el slice `[1, 2, 3, 4, 5]`{l=go} rotado en 2 posiciones sería `[3, 4, 5, 1, 2]`{l=go}.
3. Escriba una función `eliminar`{l=go} que elimine un elemento de un slice. Por ejemplo, el slice `[1, 2, 3, 4, 5]`{l=go} eliminando el elemento en la posición 2 sería `[1, 2, 4, 5]`{l=go}.
4. Escriba una función `eliminarDuplicados`{l=go} que elimine los elementos duplicados de un slice. Por ejemplo, el slice `[1, 2, 2, 3, 4, 4, 5]`{l=go} sin duplicados sería `[1, 2, 3, 4, 5]`{l=go}.

## Links recomendados

- [Go Slices: usage and internals](https://go.dev/blog/slices-intro){target="\_blank"} - Un artículo que explica el uso y la estructura interna de los slices en Go.
