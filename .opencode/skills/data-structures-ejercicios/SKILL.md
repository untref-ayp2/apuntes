---
name: data-structures-ejercicios
description: Crea y mantiene esqueletos del repositorio data-structures. Documenta la estructura de paquetes, convenciones de nombres, estilo de código y README.
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un asistente especializado en la creación y mantenimiento de esqueletos de estructuras de datos para el repositorio `data-structures` de la materia Algoritmos y Programación II (UNTREF). Conocés las convenciones de nomenclatura, estilo de código Go y el formato de los README.
</role>

<context>
Este repositorio funciona como template de GitHub Classroom: cada alumno lo forkeará e implementará las estructuras. Por eso debe ser ejemplar: cualquier inconsistencia se multiplica en decenas de copias.

Existen dos ubicaciones relacionadas:

- **`~/AyP2/data-structures/`** — Repositorio real (template). Contiene interfaces, esqueletos .go, tests y README raíz.
- **`~/AyP2/apuntes/data-structures/`** — Mirror dentro del apunte (si existe). Sirve como referencia de estructura.

Los esqueletos de `data-structures` son importados por el repositorio `taller-tad` (ver skill `taller-tad-ejercicios` para los ejercicios prácticos).
</context>

## Arquitectura de un paquete en data-structures

```
paquete/
├── paquete.go             # interfaz del TAD
├── una_impl.go            # esqueleto de una implementación
├── otra_impl.go           # esqueleto de otra implementación
├── una_impl_test.go       # tests de una_impl
├── otra_impl_test.go      # tests de otra_impl (o todo en paquete_test.go)
└── paquete_test.go        # tests compartidos
```

Reglas:

- **Siempre** hay un archivo de interfaz (salvo que el TAD no defina una interfaz exportable, como `BitMap`).
- Cada implementación va en su propio archivo (no todo en un mismo archivo).
- Los tests pueden ir en un archivo compartido (`paquete_test.go`) o separados por impl (`una_impl_test.go`), según convenga. Se usa `package foo` (mismo package, no `foo_test`).

## Convenciones de nombres de archivo

Cada paquete tiene su propia convención, documentada en el README raíz:

| Paquete | Patrón de archivos | Ejemplos |
|---|---|---|
| `stack/` | `stack_slice.go`, `stack_list.go` | `stack_slice.go`, `stack_list.go` |
| `queue/` | `queue_slice.go`, `queue_list.go` | `queue_slice.go`, `queue_list.go` |
| `list/` | `singly_linked.go`, `doubly_linked.go`, `circular_linked.go`, `sentinel_linked.go` | `singly_linked.go` |
| `set/` | `set_map.go`, `set_hashtable.go`, `set_ordered.go` | `set_map.go` |
| `hashtable/` | `hashtable_chaining.go`, `hashtable_open_addressing.go` | `hashtable_chaining.go` |
| `bitmap/` | `bitmap.go` | — |

Al agregar un paquete nuevo, definir un patrón de nombres coherente y documentarlo en el README raíz.

## Convenciones de código

### Constructores

Siempre `New` + `TypeName`:

| Bien | Mal |
|---|---|
| `NewSinglyLinkedList[T]()` | `New()` |
| `NewSliceStack[T]()` | `NewStack()` |
| `NewHashTableChaining[K, V]()` | `NewChainingHashTable()` |
| `NewBitMap(n uint8)` | `New(n uint8)` |

### Esqueletos

- Las funciones retornan el valor cero de su tipo de retorno (`return nil` para punteros/slices/maps/interfaces, `return 0` para números, `return false` para bools).
- El cuerpo de la función es `// Completar`.
- Los parámetros y retornos están completos y tipados; el alumno solo completa el cuerpo.

```go
func (s *MapSet[T]) Add(element T) {
	// Completar
}

func (s *MapSet[T]) Contains(element T) bool {
	// Completar
	return false
}

func NewMapSet[T comparable]() *MapSet[T] {
	// Completar
	return nil
}
```

### Documentación

- Comentarios Godoc en español.
- `// Completar` va como cuerpo, no como doc comment. El doc comment describe qué hace la función.
- Las interfaces tienen doc comments en cada método.
- Los constructores describen qué crean.

### Errores

- Las operaciones que pueden fallar retornan `error` como último valor de retorno.
- Usar `var zero T` para el valor cero genérico en funciones que retornan `(T, error)`.

```go
func (ht *HashTableChaining[K, V]) Get(key K) (V, error) {
	// Completar
	var zero V
	return zero, nil
}
```

### Structs

- Los campos pueden declararse como pista (especialmente en implementaciones simples) o dejarse como `// Completar` si se prefiere que el alumno los deduzca.
- La decisión es por paquete; no mezclar estilos dentro de un mismo paquete.

## Convenciones de tests

- Mismo package (`package foo`, no `package foo_test`).
- Importar solo `"testing"` (y `"errors"` si se necesita comparar errores).
- Nombres de función: `TestNombreMetodo` (PascalCase).
- Mensajes en español, con `t.Errorf` para errores no fatales y `t.Fatalf` si no tiene sentido continuar.
- Incluir casos borde: valores inválidos, vacío, un solo elemento, duplicados.

```go
func TestMapSetAddAndContains(t *testing.T) {
	s := NewMapSet[int]()
	s.Add(1)
	s.Add(2)

	if !s.Contains(1) {
		t.Error("Debería contener 1")
	}
	if s.Contains(3) {
		t.Error("No debería contener 3")
	}
}

func TestMapSetRemoveNonExistent(t *testing.T) {
	s := NewMapSet[int]()
	s.Add(1)
	s.Remove(99)

	if s.Size() != 1 {
		t.Error("Remove de elemento inexistente no debería cambiar Size")
	}
}
```

## Formato del README raíz

Al agregar un paquete nuevo, actualizar `## Estructura` con una línea como:

```
stack/       # interface Stack[T] + SliceStack[T] + StackList[T] + tests
```

Formato: `paquete/     # descripción con interfaces + implementaciones + tests`

Si el paquete introduce una convención de nombres nueva, documentarla en el párrafo posterior (`## Estructura`):

```
Cada paquete define una **interfaz** que los alumnos deben implementar en su
fork. La convención de nombres varía según el paquete:

- `stack/`, `queue/`: `*_slice.go` para la impl. sobre slices, `*_list.go` ...
- `list/`: `*_linked.go` según el tipo de enlace
- ...
```

No modificar las secciones `## Requisitos`, `## Cómo usar`, `## Uso con taller-tad` ni `## Licencia` a menos que haya un cambio estructural (ej: nueva versión de Go).

## Flujo para agregar un nuevo paquete

Ejemplo: agregar `dictionary/` con interfaz `Dictionary[K, V]` e implementación `HashMapDictionary[K, V]`.

### 1. Crear el directorio

```bash
mkdir ~/AyP2/data-structures/dictionary
```

### 2. Crear la interfaz

`dictionary/dictionary.go`:

```go
package dictionary

// Dictionary define las operaciones de un diccionario clave-valor.
type Dictionary[K comparable, V any] interface {
	Set(key K, value V)
	Get(key K) (V, error)
	Delete(key K) error
	Contains(key K) bool
	Size() int
	Keys() []K
	Values() []V
}
```

### 3. Crear esqueletos de implementación

`dictionary/hash_map_dictionary.go`:

```go
package dictionary

// HashMapDictionary implementa Dictionary[K, V] usando una HashTable.
type HashMapDictionary[K comparable, V any] struct {
	// Completar
}

func NewHashMapDictionary[K comparable, V any]() *HashMapDictionary[K, V] {
	// Completar
	return nil
}

func (d *HashMapDictionary[K, V]) Set(key K, value V) {
	// Completar
}

// ... resto de métodos siguiendo el mismo patrón
```

### 4. Crear tests

`dictionary/dictionary_test.go`:

```go
package dictionary

import "testing"

func TestHashMapDictionarySetAndGet(t *testing.T) {
	d := NewHashMapDictionary[string, int]()
	d.Set("a", 1)
	val, err := d.Get("a")
	if err != nil {
		t.Fatalf("error inesperado: %v", err)
	}
	if val != 1 {
		t.Errorf("esperaba 1, obtuve %d", val)
	}
}

// ... más tests cubriendo Delete, Contains, Size, Keys, Values, casos borde
```

### 5. Actualizar README raíz

Agregar en `README.md`:

```
dictionary/  # interface Dictionary[K, V] + HashMapDictionary[K, V] + tests
```

## Flujo para agregar una implementación a un paquete existente

Ejemplo: agregar `SliceSet[T]` al paquete `set/`.

### 1. Crear el archivo

`set/set_slice.go` — con un constructor `NewSliceSet[T comparable]()`.

### 2. Agregar tests

En `set/set_test.go` o en un archivo `set/set_slice_test.go`. Seguir el mismo estilo que las impl existentes.

### 3. Actualizar README raíz

Agregar `+ SliceSet[T]` a la línea de `set/` en `## Estructura`.

## Relación con taller-tad

Las interfaces y tipos definidos en `data-structures` son importados por `taller-tad` para sus ejercicios. Al agregar:

- Una **nueva interfaz**: crear ejercicios en `taller-tad` que la usen (ver skill `taller-tad-ejercicios`).
- Una **nueva implementación** de una interfaz existente: no requiere cambios en `taller-tad` (los ejercicios existentes ya funcionan contra la interfaz).
