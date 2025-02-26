---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Arreglos y Slices

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
