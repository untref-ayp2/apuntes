---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Punteros

Un puntero es una variable que almacena una dirección de memoria a otra variable de un determinado tipo.

Si asignamos un `int`{l=go}, un `struct`{l=go} o un _array_, se copia el contenido del elemento. Para lograr el mismo efecto que con las referencias a variables en Java, Go usa punteros.

Para cualquier tipo `T`{l=go}, existe un correspondiente tipo puntero `*T`{l=go}, que determina un puntero a un valor de tipo `T`{l=go}.

Si declaramos una variable de tipo `int`, podemos crear un puntero que apunte a esa variable, este puntero será de tipo `*int`{l=go}:

```go
import "fmt"

var a int = 7
var pa *int = &a

fmt.Println("pa:", pa)
fmt.Println("*pa:", *pa)
```

```output
pa: 0xc00052a000
*pa: 7
```

Los punteros son tanto poderosos como simples, pero es posiblemente uno de los temas más difíciles de asimilar. Hablemos un poco de sintaxis, cuando trabajamos con punteros utilizamos 2 operadores, por un lado el operador de "desreferencia" que es `*`{l=go} y por otro lado el operador `&`{l=go} que devuelve la posición de memoria de una variable.

Cómo podemos ver en nuestro código estamos obteniendo la dirección de memoria de la variable `a`{l=go} (es decir su puntero) y lo almacenamos en la variable `pa`{l=go} que es de tipo `*int`{l=go} (no confundir el operador `*`{l=go} con el asterisco que se agrega delante del nombre de un tipo para indicar que en realidad es el **puntero** a un tipo).

El término "desreferenciar" significa tomar la posición de memoria y hacer referencia al contenido de esa posición de memoria, no a la dirección en sí. Por eso, cuando hacemos `*pa`{l=go} estamos refiriendo al espacio de memoria donde fué definida la variable `a`{l=go}.

En Java, dependiendo el tipo de dato, los valores eran pasados por referencia o por valor. En Go, nosotros debemos explicitar si vamos a recibir un valor por referencia o por valor, al momento de definir los argumentos de nuestras funciones.
