---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Mapas

Los **maps** están implementados como `HashMap` y permiten buscar un valor por
un clave de forma eficiente. Para crear un map vacío, hacemos lo siguiente:

```{code-cell} go
m := make(map[string]int)
```

De esta forma hemos creado un `map` donde las claves son de tipo `string` y los
valores de tipo `int`.

Los valores se asignan y se leen por medio de una notación similar a la de los
arrays/slices.

```{code-cell} go
m["Juan"] = 1337
```

Es importante destacar que leer el contenido para una determinada clave,
devuelve 2 valores. En primer lugar el valor almacenado y en segundo lugar un
booleano que indica si la clave existe en el `map` o no.

```{code-cell} go
v, ok := m["Juan"]
```

```{code-cell} go
:tags: [remove-input]
m["Juan"]
```

Si el `map` no contiene la clave solicitada, entonces se devuelve el "valor
nulo" del tipo de los valores.

```{code-cell} go
m["Jose"] = 14
m["Maria"] = 0
```

```{code-cell} go
:tags: [remove-input]
m
```

Podemos  ver que si queremos el valor que tiene Jose, podemos accederlo con:

```{code-cell} go
v1, ok := m["Jose"]
```

```{code-cell} go
:tags: [remove-input]
m["Jose"]
```

Obtenemos el valor y `true` ya que el valor existe.

Pero que sucede si queremos pedir el valor que tiene Maria, que en este caso
coincide con el "valor nulo" del tipo `int`.

```{code-cell} go
v2, ok := m["Maria"]
```

```{code-cell} go
:tags: [remove-input]
m["Maria"]
```

Si solo obtenemos el valor, sin el `ok`, no podemos saber si el valor `0`
obtenido es el valor almacenado o simplemente el valor por defecto que devuelve
`map`.

```{code-cell} go
vNot, ok := m["Pedro"]
```

```{code-cell} go
:tags: [remove-input]
m["Pedro"]
```
