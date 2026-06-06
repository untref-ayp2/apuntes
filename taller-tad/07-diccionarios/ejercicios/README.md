# Ejercicios: Diccionarios

Antes de comenzar, implementá `HashMapDictionary` en tu repositorio
data-structures, paquete `dictionary/`.

Luego completá los siguientes ejercicios usando `Dictionary[K, V]`:

---

## 1. Registro de stock de productos

Un depósito necesita gestionar el stock de sus productos. Cada producto
tiene un código único (clave `string`) y una cantidad en stock
(valor `int`).

**Valores**: pares código de producto (`string`) → cantidad en stock (`int`).

**Operaciones**:

- `NuevoStock() *Stock` — crea un registro de stock vacío
- `IngresarStock(codigo string, cantidad int)` — agrega `cantidad` unidades
  al producto (si el producto no existe, lo crea con esa cantidad)
- `RetirarStock(codigo string, cantidad int) error` — descuenta `cantidad`
  unidades del producto. Error si el producto no existe o si el stock
  resultante sería negativo.
- `StockActual(codigo string) (int, error)` — devuelve la cantidad en stock
  de un producto. Error si el producto no existe.
- `ProductoConMenorStock() (string, error)` — devuelve el código del producto
  con menor cantidad en stock. Error si no hay productos registrados.
- `ProductosConStockCero() []string` — devuelve los códigos de los productos
  sin stock (cantidad = 0), ordenados alfabéticamente.

**Invariante**:

- El stock de un producto nunca puede ser negativo.
- `RetirarStock` no debe modificar el stock si la operación falla.
- No debe haber productos con clave duplicada (el diccionario lo garantiza).

**Preguntas**:

- ¿Qué complejidad tiene cada operación?
- ¿Cómo implementaste `ProductoConMenorStock`? ¿Hay forma de hacerlo más
  eficiente si la estructura interna fuera otra?
- ¿Por qué es útil que `RetirarStock` devuelva `error` en lugar de simplemente
  no hacer nada?

→ `01-stock/`

---

## 2. Directorio telefónico con búsqueda inversa

Implementar una agenda telefónica que permita buscar contactos tanto por
nombre como por número de teléfono. Para la búsqueda inversa (teléfono →
nombre) se debe mantener un segundo diccionario que relacione teléfonos con
nombres.

**Valores**: dos diccionarios — uno nombre → `Contacto` y otro teléfono → nombre.

**Estructura `Contacto`**:

```go
type Contacto struct {
    Nombre   string
    Telefono string
}
```

**Operaciones**:

- `NuevoDirectorio() *Directorio` — crea un directorio vacío
- `AgregarContacto(nombre, telefono string) error` — agrega un contacto. Error
  si el nombre ya existe o si el teléfono ya está asociado a otro contacto.
- `BuscarPorNombre(nombre string) (Contacto, error)` — devuelve el contacto
  por su nombre. Error si no existe.
- `BuscarPorTelefono(telefono string) (Contacto, error)` — devuelve el contacto
  por su número de teléfono. Error si no existe.
- `ActualizarTelefono(nombre string, nuevoTelefono string) error` — cambia el
  teléfono de un contacto. Error si el nombre no existe o el nuevo teléfono ya
  está en uso por otro contacto.
- `ContactosConNombreLargo(n int) []Contacto` — devuelve los contactos cuyo
  nombre tenga más de `n` caracteres.

**Invariante**:

- Cada nombre está asociado a exactamente un teléfono.
- Cada teléfono está asociado a exactamente un nombre.
- Al actualizar un teléfono, el índice inverso debe reflejar el cambio.

**Preguntas**:

- ¿Qué sucede si dos personas quisieran tener el mismo número de teléfono?
  ¿Cómo modificarías el diseño para permitirlo?
- ¿Qué complejidad tiene `BuscarPorTelefono` con esta implementación?
  ¿Cómo se compara con `BuscarPorNombre`?
- ¿Por qué es necesario mantener dos diccionarios en lugar de uno solo?

→ `02-directorio/`
