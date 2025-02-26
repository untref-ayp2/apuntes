---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Punteros

Un puntero es una variable que almacena una dirección de memoria a otra variable
de un determinado tipo.

Si asignamos un `int`, un `struct` o un `array`, se copia el contenido del
elemento. Para lograr el mismo efecto que con las referencias a variables en
Java, Go usa punteros.

Para cualquier tipo `T`, existe un correspondiente tipo puntero `*T`, que
determina un puntero a un valor de tipo `T`.

Si declaramos una variable de tipo `int`, podemos crear un puntero que apunte a
esa variable, este puntero será de tipo `*int`:

```{code-cell} go
:tags: [remove-output]
import "fmt"

var a int = 7
var pa *int = &a

fmt.Println("pa:", pa)
fmt.Println("*pa:", *pa)
```

```{code-cell} go
:tags: [remove-input]
fmt.Println("pa:", pa)
fmt.Println("*pa:", *pa)
nil
```

Los punteros son tanto poderosos como simples, pero es posiblemente uno de los
temas más difíciles de asimilar. Hablemos un poco de sintaxis, cuando trabajamos
con punteros utilizamos 2 operadores, por un lado el operador de "desreferencia"
que es `*` y por otro lado el operador `&` que devuelve la posición de memoria
de una variable.

Cómo podemos ver en nuestro código estamos obteniendo la dirección de memoria de
la variable `a` (es decir su puntero) y lo almacenamos en la variable `pa` que
es de tipo `*int` (no confundir el operador `*` con el asterisco que se agrega
delante del nombre de un tipo para indicar que en realidad es el **puntero** a
un tipo).

El término "desreferenciar" significa tomar la posición de memoria y hacer
referencia al contenido de esa posición de memoria, no a la dirección en sí. Por
eso, cuando hacemos `*pa` estamos refiriendo al espacio de memoria donde fué
definida la variable `a`.

En Java, dependiendo el tipo de dato, los valores eran pasados por referencia o
por valor. En Go, nosotros debemos explicitar si vamos a recibir un valor por
referencia o por valor, al momento de definir los argumentos de nuestras
funciones.
