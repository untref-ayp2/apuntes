---
label: diccionarios
---

# Diccionarios

Un **diccionario** (también llamado mapa o arreglo asociativo) es un Tipo Abstracto de Datos (TAD) que permite almacenar colecciones de pares de elementos `(clave, valor)`. La clave es un identificador único que nos permite almacenar, recuperar y eliminar de manera eficiente el valor asociado a ella.

La analogía clásica para entender un diccionario es la de una agenda o guía telefónica. En ella, el nombre de la persona actúa como la **clave** y el número de teléfono es el **valor** asociado. Utilizando un índice alfabético (por ejemplo, buscando la letra "M"), podemos localizar rápidamente el número de teléfono de "Maria" sin necesidad de recorrer secuencialmente toda la guía.

```{figure} ../_static/figures/3-estructuras-de-datos/3-7-diccionarios/diccionario_light.svg
---
name: fig-diccionario-light
class: only-light-mode
---
Concepto de diccionario como una agenda telefónica indexada.
```

```{figure} ../_static/figures/3-estructuras-de-datos/3-7-diccionarios/diccionario_dark.svg
---
class: only-dark-mode
---
Concepto de diccionario como una agenda telefónica indexada.
```

## Relación con las tablas de *hash*

En la práctica, la forma estándar y más eficiente de implementar el TAD Diccionario es mediante una **tabla de *hash*** (estructura que ya estudiamos en detalle en el capítulo {ref}`hashing`).

Como vimos, una tabla de *hash* utiliza una función de dispersión para mapear las claves a posiciones específicas en un arreglo subyacente. Gracias a esto, un diccionario implementado sobre una tabla de *hash* nos garantiza un costo de tiempo promedio constante ($O(1)$) para las operaciones de inserción, búsqueda y eliminación:

|             Operación             | Complejidad Promedio |
| :-------------------------------: | :------------------: |
|    Insertar/Actualizar (`Set`)    |        $O(1)$        |
|          Obtener (`Get`)          |        $O(1)$        |
|        Eliminar (`Delete`)        |        $O(1)$        |
| Verificar existencia (`Contains`) |        $O(1)$        |
|          Tamaño (`Size`)          |        $O(1)$        |
|      Listar Claves (`Keys`)       |        $O(n)$        |
|     Listar Valores (`Values`)     |        $O(n)$        |

## Interfaz en Go

Para formalizar este TAD dentro de nuestra biblioteca de estructuras de datos, definimos la *interface* genérica `Dictionary` en Go. El contrato exige que las claves pertenezcan al constraint `comparable` de Go (ya que deben poder compararse por igualdad) y los valores pueden ser de cualquier tipo:

```{code-block} go
---
linenos:
---
package dictionary

// Dictionary define las operaciones abstractas de un diccionario clave-valor.
type Dictionary[K comparable, V any] interface {
    // Set almacena un par clave-valor. Si la clave ya existe, actualiza su valor.
    Set(key K, value V)

    // Get devuelve el valor asociado a la clave.
    // El booleano indica si la clave existe (sigue el idiom coma-ok de Go).
    Get(key K) (V, bool)

    // Delete elimina la clave y su valor del diccionario. Retorna error si no existe.
    Delete(key K) error

    // Contains devuelve true si la clave está presente en el diccionario.
    Contains(key K) bool

    // Size devuelve la cantidad total de pares clave-valor almacenados.
    Size() int

    // Keys devuelve un slice con todas las claves presentes en el diccionario.
    Keys() []K

    // Values devuelve un slice con todos los valores presentes en el diccionario.
    Values() []V

    // String devuelve una representación en cadena del diccionario.
    String() string
}
```

## El tipo `map` nativo de Go

Go no cuenta con un tipo de datos `Set` o `Stack` nativo, pero sí provee soporte integrado para diccionarios mediante el tipo `map`. Un `map` en Go es una implementación interna y altamente optimizada de una tabla de *hash* abierta.

La sintaxis básica para declarar un mapa asociando claves de tipo `K` con valores de tipo `V` es:

```{code-block} go
---
linenos:
---
var m map[TipoClave]TipoValor
```

### Inicialización y uso básico

Para poder operar con un mapa en Go es necesario inicializarlo previamente. La forma más común es utilizando la función interna `make()`:

```{code-block} go
---
linenos:
---
// Declaración e inicialización
edades := make(map[string]int)

// Inserción y actualización de elementos
edades["Juan"] = 25
edades["Maria"] = 30

// Recuperación de un valor
edadJuan := edades["Juan"] // edadJuan valdrá 25

// Eliminación de un par clave-valor
delete(edades, "Juan")
```

### Verificación de existencia (El *idiom* de la coma-ok)

En Go, si intentamos acceder a una clave que no existe en el mapa, el lenguaje no genera un pánico ni un error: nos devuelve el valor cero del tipo del valor (por ejemplo, `0` si el tipo de valor es `int`, o `""` si es `string`).

Para poder distinguir entre una clave que realmente tiene asociado el valor cero y una clave que no existe en absoluto, Go provee la sintaxis especial conocida como el *idiom* de la *comma-ok*:

```{code-block} go
---
linenos:
---
if edad, ok := edades["Juan"]; ok {
    fmt.Printf("Juan tiene %d años\n", edad)
} else {
    fmt.Println("Juan no está en la agenda")
}
```

Aquí, `ok` es un booleano que vale `true` si la clave existe en el mapa y `false` en caso contrario.

### Recorrido del mapa

Para iterar sobre los pares de un mapa, utilizamos un bucle `for` combinado con la estructura `range`. Es muy importante recordar que **el recorrido de un mapa en Go es no determinista y desordenado** (el orden de los elementos cambia entre ejecuciones consecutivas para evitar que los programas dependan del orden interno de la tabla de *hash*):

```{code-block} go
---
linenos:
---
for nombre, edad := range edades {
    fmt.Printf("%s tiene %d años\n", nombre, edad)
}
```

## Estrategias de implementación del TAD

Al momento de construir estructuras que satisfagan nuestra interfaz `Dictionary` en la cursada, existen dos aproximaciones principales:

1. **Envoltura de `map` de Go**:
   Se puede implementar la interfaz construyendo un *struct* que encapsule un mapa nativo de Go. Esta es la forma más rápida y directa, delegando la lógica de dispersión y colisiones al compilador.
2. **Uso de la `HashTable` de la cursada**:
   Se puede implementar la interfaz encapsulando la estructura genérica `HashTable` que implementamos en el capítulo 3-5 (ya sea la versión con sondeo lineal o la de encadenamiento separado). Al hacerlo, el diccionario simplemente actúa como una capa de abstracción sobre los métodos ya testeados de la tabla de *hash*.

## Inyección de la estructura base por constructor

En el esquema del repositorio `data-structures`, la implementación `HashMapDictionary` no crea la `HashTable` internamente, sino que la recibe ya construida a través del constructor:

```{code-block} go
---
linenos:
---
func NewHashMapDictionary[K comparable, V any](
    table hashtable.HashTable[K, V],
) *HashMapDictionary[K, V] {
    return &HashMapDictionary[K, V]{table: table}
}
```

Esta técnica se conoce como **inyección de dependencias** y es un mecanismo habitual para componer TADs a partir de otros TADs más pequeños. Al recibir la tabla de *hash* por parámetro:

- El diccionario funciona con *cualquier* implementación de `HashTable`. Podemos pasarle una `*HashTableChaining`, una `*HashTableOpenAddressing`, o incluso un *mock* en los tests.
- Separamos la responsabilidad de construir la tabla de la responsabilidad de usarla. Quien crea el diccionario decide qué variante de `HashTable` emplear.
- La delegación es total: cada método del diccionario se limita a invocar el método correspondiente sobre la tabla interna.

La siguiente porción de código muestra cómo usaríamos el diccionario con distintas implementaciones de la tabla de *hash*:

```{code-block} go
---
linenos:
---
// Diccionario con encadenamiento separado
tablaEncadenada := hashtable.NewHashTableChaining[string, int]()
dict1 := NewHashMapDictionary[string, int](tablaEncadenada)

// Diccionario con sondeo lineal (misma interfaz)
tablaSondeo := hashtable.NewHashTableOpenAddressing[string, int]()
dict2 := NewHashMapDictionary[string, int](tablaSondeo)
```

Este mismo patrón es el que aplicamos en el capítulo anterior con `NewHashTableSet`: el constructor recibe (o crea internamente) una `HashTable[T, struct{}]` para almacenar los elementos del conjunto. La diferencia es que en `HashMapDictionary` exponemos la tabla en el constructor para que quien use la estructura pueda elegir la implementación más conveniente según el contexto.

## Ejercicios

Los ejercicios de este capítulo están en `07-diccionarios/ejercicios/` del
repositorio [taller-tad](https://github.com/untref-ayp2/taller-tad).

Antes de comenzar, asegurate de tener implementadas las estructuras necesarias en
[data-structures](https://github.com/untref-ayp2/data-structures).
Ambas tareas se trabajan en paralelo: primero completás las implementaciones
en `data-structures` y después las usás acá.
