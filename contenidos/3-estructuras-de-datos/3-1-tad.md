---
label: tad
---

# Tipos Abstractos de Datos

## Definición

Podemos imaginar un Tipo Abstracto de Datos (TAD) o _Abstract Data Type_ (ADT) en inglés,
como una **caja negra** que contiene valores y define un conjunto de operaciones para
manipularlos. Quien usa el TAD solo conoce **qué** operaciones puede realizar, pero no
**cómo** están implementadas internamente.

```{admonition} Definición
---
class: hint
---
Un **TAD** es un modelo matemático caracterizado por:

*   **Valores**: los datos que se pueden almacenar y manipular.
*   **Operaciones**: las acciones que se pueden realizar sobre esos datos.
```

En un TAD distinguimos dos capas: la **estructura interna** donde realmente se almacenan
los datos, y la **interfaz** que expone hacia afuera las operaciones disponibles. Esta
separación es fundamental: quien usa el TAD solo necesita conocer la interfaz, no los
detalles internos.

Por ejemplo, un conjunto es un TAD que permite agregar elementos, consultar si un
elemento pertenece o eliminarlos. No tenemos acceso directo a la estructura interna que
lo implementa, solo podemos usar las operaciones que define su interfaz.

## Características de un TAD

### Abstracción

La abstracción implica definir un conjunto de operaciones que pueden realizarse sobre un
tipo de dato, sin revelar cómo se implementan internamente.

### Ocultamiento de información

Es el mecanismo que permite ocultar los detalles de implementación, encapsulando los
datos y las operaciones en una única estructura y exponiendo solo una interfaz bien
definida.

La **abstracción** se logra mediante el **ocultamiento de información**.

### Interfaz

Es la parte visible del TAD, que define cómo se puede interactuar con él. La interfaz es
el **contrato** que el TAD ofrece a sus usuarios.

### Comportamiento

Es el conjunto de operaciones que se pueden realizar sobre un TAD y los efectos que
producen.

El **comportamiento** de un TAD se define a través de su **interfaz**.

### Invariante de representación

El **invariante de representación** (o simplemente *invariante*) es una condición lógica
que debe cumplirse para todo estado **válido** del TAD. Es como una regla interna que
garantiza la integridad y coherencia de la estructura de datos.

Por ejemplo, en un TAD que modela un `Reloj` de 24 horas, el invariante podría ser que
la hora esté siempre entre 0 y 23. Si alguna primitiva dejara la hora en 25, el
invariante estaría roto.

```{admonition} Primitivas
---
class: note
---
Cada operación del TAD se denomina **primitiva**. Las primitivas son las únicas
operaciones disponibles para manipular el estado interno del TAD.
```

#### El invariante durante la ejecución de una primitiva

El invariante debe cumplirse **siempre**, con una salvedad importante: **durante la
ejecución de una primitiva el invariante puede dejar de cumplirse temporalmente**. Esto
es aceptable siempre que la primitiva lo **restablezca** antes de finalizar.

Supongamos un TAD con dos campos `a` y `b`, donde el invariante es `a == b`. Si una
primitiva ejecuta primero `a = a + 1` y luego `b = b + 1`, entre ambas operaciones el
invariante no se cumple. Esto es válido siempre que al terminar la primitiva la igualdad
se cumpla nuevamente.

#### Atomicidad de las primitivas

Las primitivas deben ser **atómicas**: deben ejecutarse por completo o no tener ningún
efecto. Si una primitiva falla a mitad de camino, el TAD debe quedar en el mismo estado
válido en el que estaba antes de ejecutarla. En otras palabras, una primitiva debe dejar
el invariante intacto, sin importar si la operación se completó exitosamente o no.

```{admonition} Importante
---
class: important
---
Un TAD cuyas primitivas no son atómicas puede dejar el invariante en un estado
inconsistente. Decimos entonces que el TAD está **roto**.
```

## Ejemplo paso a paso: TAD Contador

Vamos a construir un TAD `Contador` que mantiene un valor entero que puede
incrementarse o decrementarse dentro de un rango fijo.

### 1. Definir los valores

El Contador necesita tres valores enteros:

- `minimo`: el valor más chico que puede tomar el contador.
- `maximo`: el valor más grande que puede tomar el contador.
- `actual`: el valor actual del contador.

Además, para analizar el invariante vamos a llevar la cuenta de cuántas veces se
modificó el contador exitosamente:

- `cambios`: cantidad total de modificaciones realizadas.

### 2. Definir las operaciones (primitivas)

| Primitiva                 | Descripción                                          |
| ------------------------- | ---------------------------------------------------- |
| `NuevoContador(min, max)` | Crea un contador con `actual = min`                  |
| `Incrementar()`           | Aumenta `actual` en 1, si no supera `maximo`         |
| `Decrementar()`           | Disminuye `actual` en 1, si no es menor que `minimo` |
| `Valor()`                 | Devuelve el valor actual                             |
| `Cambios()`               | Devuelve la cantidad de modificaciones               |

### 3. Definir el invariante

El invariante del Contador tiene dos partes:

1. `minimo <= actual <= maximo`: el valor actual siempre está dentro del rango.
2. `cambios` es igual a la cantidad de veces que se ejecutaron `Incrementar` o
   `Decrementar` con éxito.

### 4. Analizar las transiciones de estado

Analicemos cada primitiva y cómo afecta al invariante.

**Constructor `NuevoContador(min, max)`**:

```
estado inicial:  (ninguno)
   ↓  validar que min <= max
   ↓  actual = min
   ↓  cambios = 0
estado final:    actual = min, cambios = 0
```

Después del constructor, el invariante se cumple: `min <= actual <= max` y `cambios`
es 0 (todavía no hubo modificaciones).

**Primitiva `Incrementar()`**:

```
estado inicial:  min <= actual <= max, cambios = n
   ↓  ¿actual < maximo?
   │   ├── No → devolver error (el estado no cambia)
   │   └── Sí → actual++             ←  el invariante se mantiene
   │            cambios++            ←  ¡el invariante podria romperse!
   ↓                                 ←  (explicacion a continuacion)
estado final:    min <= actual <= max, cambios = n + 1
```

¿En qué momento podría no cumplirse el invariante? En esta implementación simple, tanto
`actual++` como `cambios++` son operaciones elementales y al finalizar la primitiva el
invariante se cumple. El punto importante es que el orden de las operaciones importa:
si primero incrementáramos `cambios` y después `actual`, y la primitiva fallara entre
medio, quedaríamos con `cambios` desactualizado. Por eso las primitivas deben diseñarse
para que, si algo sale mal, el estado vuelva atrás.

### 5. Implementación en Go

```{code-block} go
---
linenos:
---
package contador

import "errors"

type Contador struct {
	actual  int
	minimo  int
	maximo  int
	cambios int
}

func NuevoContador(min, max int) (*Contador, error) {
	if min > max {
		return nil, errors.New("minimo no puede ser mayor que maximo")
	}
	return &Contador{
		actual:  min,
		minimo:  min,
		maximo:  max,
		cambios: 0,
	}, nil
}

func (c *Contador) Incrementar() error {
	if c.actual >= c.maximo {
		return errors.New("el contador ya alcanzó el máximo")
	}
	c.actual++
	c.cambios++
	return nil
}

func (c *Contador) Decrementar() error {
	if c.actual <= c.minimo {
		return errors.New("el contador ya alcanzó el mínimo")
	}
	c.actual--
	c.cambios++
	return nil
}

func (c *Contador) Valor() int {
	return c.actual
}

func (c *Contador) Cambios() int {
	return c.cambios
}
```

```{admonition} Código en el repositorio
---
class: tip
---
Este ejemplo completo con tests está disponible en
[`taller-tad/01-tipos-abstractos-de-datos/ejemplos/contador/`](https://github.com/untref-ayp2/taller-tad/tree/main/01-tipos-abstractos-de-datos/ejemplos/contador).
```

### 6. Verificar el invariante en cada primitiva

**`NuevoContador`**: valida que `min <= max` antes de crear el contador. Si la
validación falla, devuelve error y no se crea ningún contador (atomicidad). Si tiene
éxito, `actual = min` y `cambios = 0`. Invariante: ✅.

**`Incrementar`**: verifica que `actual < maximo`. Si no, devuelve error sin modificar
nada (atomicidad). Si sí, incrementa `actual` y `cambios`. Al terminar, `actual` sigue
siendo `<= maximo` (porque verificamos antes) y `cambios` aumentó en 1. Invariante: ✅.

**`Decrementar`**: análogo a `Incrementar` pero con `minimo`. Invariante: ✅.

**`Valor` y `Cambios`**: solo lectura, no modifican el estado. Invariante: ✅.

### 7. Atomicidad en la práctica

Observá el patrón que usan `Incrementar` y `Decrementar`:

1. **Validar** la condición que protege el invariante.
2. Si no se cumple → **error** sin modificar nada.
3. Si se cumple → **modificar** el estado.

Este patrón garantiza atomicidad: la primitiva se ejecuta por completo (modifica el
estado) o no tiene efecto (devuelve error). Nunca queda un estado intermedio donde
el invariante esté roto.

```{admonition} Nota
---
class: tip
---
En Go, el constructor devuelve un puntero `*Contador` y un `error`. Esta convención
permite que el constructor valide los parámetros y, si algo falla, devuelva un error
sin haber creado ningún estado inconsistente.
```

## Go: *struct* e *interface* para definir TADs

Go cuenta con *struct* e *interface* para definir nuevos tipos abstractos de datos. Las
estructuras nos permiten definir un conjunto de valores y operaciones asociadas. Algunas
operaciones pueden ser públicas (forman parte de la interfaz del TAD) y otras privadas
(para uso interno). Las interfaces permiten que varios tipos que presentan el mismo
comportamiento puedan manipularse como un único tipo.

En el ejemplo del Contador, `Contador` es un *struct* con campos en minúscula
(`actual`, `minimo`, `maximo`, `cambios`). Al estar en minúscula son privados: nadie
fuera del paquete `contador` puede accederlos directamente. Las funciones y métodos
con mayúscula (`NuevoContador`, `Incrementar`, `Valor`) son públicos: forman la
interfaz del TAD.

## Repositorio del taller de TAD

Los ejemplos y ejercicios de este capítulo están en el repositorio
[`untref-ayp2/taller-tad`](https://github.com/untref-ayp2/taller-tad). Está organizado
por capítulo (`01-tipos-abstractos-de-datos/`, `02-pilas-colas/`, etc.) y dentro de cada
uno hay dos carpetas:

- **`ejemplos/`**: programas completos que ilustran los conceptos del apunte.
- **`ejercicios/`**: esqueletos de código con partes incompletas para completar y tests
  automatizados para validar la solución.

Para ejecutar los tests de un ejercicio:

```{code-block} bash
cd taller-tad/01-tipos-abstractos-de-datos/ejercicios/01-fraccion
go test -v
```

## Ejercicios

Los ejercicios de este capítulo están en `01-tipos-abstractos-de-datos/ejercicios/` del
repositorio [taller-tad](https://github.com/untref-ayp2/taller-tad).

Este repositorio incluye las estructuras definidas en
[data-structures](https://github.com/untref-ayp2/taller-tad/tree/main/data-structures)
como un subdirectorio. Antes de resolver los ejercicios, asegurate de tener
implementadas las estructuras necesarias en `data-structures/`.
Ambas tareas se trabajan en paralelo: primero completás las implementaciones
en `data-structures` y después las usás acá.
