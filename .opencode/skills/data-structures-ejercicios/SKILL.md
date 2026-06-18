---
name: data-structures-ejercicios
description: Crea y mantiene esqueletos del repositorio data-structures. Documenta la estructura de paquetes, convenciones de nombres, estilo de código y README.
license: CC-BY-SA-4.0
compatibility: opencode
---

<role>
Sos un asistente especializado en la creación y mantenimiento de esqueletos de estructuras de datos para el repositorio `data-structures` de la materia Algoritmos y Programación II (UNTREF).
</role>

<context>
Este repositorio funciona como template de GitHub Classroom. Los esqueletos son importados por `taller-tad`.

**Consultar `ESTILOS.md` §5 para convenciones de ejercicios en el apunte.**
</context>

## Arquitectura de un paquete

```
paquete/
├── paquete.go             # interfaz del TAD
├── una_impl.go            # esqueleto de implementación
├── otra_impl.go           # esqueleto de otra implementación
├── una_impl_test.go       # tests
└── paquete_test.go        # tests compartidos
```

- **Siempre** hay un archivo de interfaz (salvo TADs sin interfaz exportable, como `BitMap`).
- Cada implementación en su propio archivo.
- Tests en `package foo` (mismo package, no `foo_test`).

## Convenciones de nombres de archivo

| Paquete | Patrón | Ejemplos |
|---|---|---|
| `stack/` | `stack_slice.go`, `stack_list.go` | `stack_slice.go`, `stack_list.go` |
| `queue/` | `queue_slice.go`, `queue_list.go` | `queue_slice.go`, `queue_list.go` |
| `list/` | `singly_linked.go`, `doubly_linked.go`, etc. | `singly_linked.go` |
| `set/` | `set_map.go`, `set_hashtable.go`, `set_ordered.go` | `set_map.go` |
| `hashtable/` | `hashtable_chaining.go`, `hashtable_open_addressing.go` | `hashtable_chaining.go` |
| `bitmap/` | `bitmap.go` | — |

## Convenciones de código

### Constructores

Siempre `New` + `TypeName`: `NewSinglyLinkedList[T]()`, `NewSliceStack[T]()`, `NewHashTableChaining[K, V]()`.

### Esqueletos

- Las funciones retornan el valor cero de su tipo (`return nil`, `return 0`, `return false`).
- El cuerpo es `// Completar`.
- Parámetros y retornos completos y tipados.

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
- `// Completar` como cuerpo, no como doc comment.

### Errores

- Operaciones que pueden fallar retornan `error` como último valor.
- Usar `var zero T` para valor cero genérico.

```go
func (ht *HashTableChaining[K, V]) Get(key K) (V, error) {
	var zero V
	return zero, nil
}
```

## Convenciones de tests

- Mismo package (`package foo`).
- Nombres: `TestNombreMetodo` (PascalCase).
- Mensajes en español con `t.Errorf` / `t.Fatalf`.
- Incluir casos borde: vacío, un elemento, duplicados, valores inválidos.

```go
func TestMapSetAddAndContains(t *testing.T) {
	s := NewMapSet[int]()
	s.Add(1)
	if !s.Contains(1) { t.Error("Debería contener 1") }
	if s.Contains(3)  { t.Error("No debería contener 3") }
}
```

## Flujo para agregar un nuevo paquete

1. Crear directorio: `mkdir ~/AyP2/data-structures/dictionary`
2. Crear interfaz `dictionary/dictionary.go`
3. Crear esqueletos `dictionary/hash_map_dictionary.go`
4. Crear tests `dictionary/dictionary_test.go`
5. Actualizar README raíz en `## Estructura`:
   ```
   dictionary/  # interface Dictionary[K, V] + HashMapDictionary[K, V] + tests
   ```

## Flujo para agregar una implementación

1. Crear archivo con constructor `NewXxxImpl[T]()`
2. Agregar tests
3. Actualizar README raíz: agregar `+ XxxImpl[T]` a la línea del paquete

## Relación con taller-tad

Las interfaces de `data-structures` son importadas por `taller-tad`. Al agregar una nueva interfaz, crear ejercicios en `taller-tad` que la usen.
