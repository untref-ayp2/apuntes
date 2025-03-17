---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Arreglos y Slices

```{code-cell} go
:tags: [remove-cell]
import f "fmt"

type FmtWrapper struct{}

func (fw FmtWrapper) Println(a ...interface{}) {
    _, _ = f.Println(a...)
}

var fmt FmtWrapper = FmtWrapper{}
```

## Arreglos

En Go los arreglos o _arrays_ son estructuras de datos que almanecenan una
cantidad arbitraria de valores **del mismo tipo**. A nivel de memoria, todos sus
elementos se encuentran en posiciones contiguas.

El tamaño de un array es definido al momento de su creación y determina su
"tipo". Es decir, un array de 7 elementos tiene un tipo diferente a un array de 3.

Podemos declarar un array de la siguiente forma:

```{code-cell} go
var numeros [7]int
```

Aquí creamos una variable de tipo `[7]int` a la que referenciaremos con el
nombre `numeros`.

La forma de acceder o modificar los valores en las distintas posiciones de un
array es por medio del índice que indica la posición, como ya se ha visto en
materias anteriores y como en la mayoría los lenguajes de programación (aunque
no todos), empezando de `0` hasta el largo menos 1.

```{code-cell} go
numeros[0] = 42
numeros[3] = 1337

fmt.Println(numeros[0] + numeros[3])
```

En el caso, de un array de 7 elementos, podremos acceder a los elementos en los
indices desde el `0` hasta el `6` inclusive. Intentar acceder a un índice fuera
de este rango va a causar un error.

```go
numeros[7]
```

```output
panic: runtime error: index out of range [7] with length 7
```

Cuando un array es pasado como argumento en una función o método, este pasa por
"referencia". Es decir, que la fución que recibe esa referencia tendrá la
libertad de modifcar el contenido de dicho array.

En Go para conocer el largo de un array existe la función `len`.

```{code-cell} go
len(numeros)
```

Para recorrer un array en Go existe la instrucción `range`, que genera un
iterador sobre el array devolviendo el índice (`i`) y el valor (`v`), en
cadaiteración del `for`, veamos un ejemplo:

```{code-cell} go
:tags: [remove-output]
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

Los **slices** en Go son similares a `List` en Java. En Go también existen los
arrays de tamaño fijo.

```{code-cell} go
s := []int{1, 2, 3}
```

```{code-cell} go
s = append(s, 4)
```

```{code-cell} go
:tags: [remove-input]
s
```

Un slice es como un arreglo dinámico, al que le podemos agregar elementos luego
de haberlos declarado (a diferencia de los arrays básicos, con tamaño fijo).

```{code-cell} go
len(s)
```

Para conocer el tamaño actual de un slice, deberos utilizar la función
_built-in_ de Go `len`. En este caso `s` tiene una longitud de `4`.

```{code-cell} go
s[1]
```

Para acceder a los elementos de la lista lo hacemos por medio de indices (cómo
lo haríamos con un array convencional).

```{code-cell} go
s[1:3]
```

El nombre _slice_ está dado por la capacidad de estas estructuras de devolver
"tajadas", mediante el operador _slice_ (el operador `[:]`, si es un poco
confuso). En nuestro ejemplo anterior: `s[1:3]` devuelve un slice `[]int{2, 3}`
que es el rango de valores entre la posición 1 hasta la 3 (sin incluir esta
última).

Un array puede ser convertido en un _slice_ utilizando el operador de _slicing_
sobre el array: `arr[:]`.
