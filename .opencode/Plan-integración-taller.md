---
file: Plan-integración-taller.md
---

# Plan de Integración: taller-go → Apunte Sección 2

## Objetivo

Reestructurar el repositorio `~/AyP2/taller-go` para que sea el repositorio compañero
de la sección 2 ("Taller de Go") del apunte, con:

- **`ejemplos/`** — código resuelto que demuestra conceptos (lo que ya existe migrado)
- **`ejercicios/`** — esqueletos con `// TODO: implementar` + tests asociados
- **`soluciones/`** — (en otra rama) versiones completas de los ejercicios

## Mapeo: Apunte → taller-go

| Apunte | taller-go actual | Acción |
|--------|------------------|--------|
| `2-1-introduccion` | `00-hola`, `01-tipodatos`, `02-variables`, `03-constantes` | Migrar a `01-introduccion/ejemplos/` |
| `2-2-paquetes-y-modulos` | — | Crear ejemplos nuevos |
| `2-3-funciones` | `04-funciones` | Migrar a `03-funciones/ejemplos/` |
| `2-4-arreglos-slices` | `08-arreglos` | Migrar a `04-arreglos-slices/ejemplos/` |
| `2-5-maps` | `09-mapas` | Migrar a `05-maps/ejemplos/` |
| `2-6-punteros` | `07-punteros` | Migrar a `06-punteros/ejemplos/` |
| `2-7-structs-interfaces` | `10-figuras` (parte) | Migrar a `07-structs-interfaces/ejemplos/` |
| `2-8-archivos` | — | Crear ejemplos nuevos |
| `2-9-errores` | `11-errores` | Migrar a `09-errores/ejemplos/` |
| `2-10-oop` | `10-figuras` (parte) | Migrar a `10-oop/ejemplos/` |
| Extras | `05-condicionales`, `06-ciclos` | Mover a `extras/condicionales/` y `extras/ciclos/` |

## Estructura final del repo

```
taller-go/
├── README.md
├── go.mod                   # module github.com/untref-ayp2/taller-go (Go 1.20)
├── Makefile                 # test, fmt, test-ejercicios
│
├── 01-introduccion/              # ← 2-1
│   ├── ejemplos/
│   │   ├── 00-hola/
│   │   ├── 01-tipodatos/
│   │   ├── 02-variables/
│   │   └── 03-constantes/
│   └── ejercicios/
│       └── saludo-personalizado/
│           ├── main.go           # esqueleto
│           └── main_test.go
│
├── 02-paquetes-y-modulos/        # ← 2-2 (NUEVO)
│   └── ejemplos/
│       ├── 01-crear-modulo/      # go mod init + estructura
│       ├── 02-importar-paquete/  # imports, alias
│       └── 03-dependencias/      # go get, go mod tidy
│
├── 03-funciones/                 # ← 2-3
│   ├── ejemplos/                 # migrado de 04-funciones
│   │   ├── main.go
│   │   ├── genericas/
│   │   │   ├── saludos.go
│   │   │   └── swap.go
│   │   └── matematicas/
│   │       ├── sumar.go
│   │       └── dividir.go
│   └── ejercicios/
│       ├── promedio/
│       │   ├── promedio.go
│       │   └── promedio_test.go
│       └── aplicar/
│           ├── aplicar.go
│           └── aplicar_test.go
│
├── 04-arreglos-slices/           # ← 2-4
│   ├── ejemplos/                 # migrado de 08-arreglos
│   │   ├── main.go
│   │   ├── sumar.go
│   │   ├── subsecuenciaSumaMaxima.go
│   │   └── ordenamientos.go
│   └── ejercicios/
│       ├── invertir/
│       │   ├── invertir.go
│       │   └── invertir_test.go
│       ├── rotar/
│       │   ├── rotar.go
│       │   └── rotar_test.go
│       ├── eliminar/
│       │   ├── eliminar.go
│       │   └── eliminar_test.go
│       └── eliminar-duplicados/
│           ├── eliminar_duplicados.go
│           └── eliminar_duplicados_test.go
│
├── 05-maps/                      # ← 2-5
│   ├── ejemplos/                 # migrado de 09-mapas
│   │   └── main.go
│   └── ejercicios/
│       ├── contar-palabras/
│       │   ├── contar_palabras.go
│       │   └── contar_palabras_test.go
│       ├── igual/
│       │   ├── igual.go
│       │   └── igual_test.go
│       └── anagramas/
│           ├── anagramas.go
│           └── anagramas_test.go
│
├── 06-punteros/                  # ← 2-6
│   ├── ejemplos/                 # migrado de 07-punteros
│   │   ├── main.go
│   │   └── punteros/
│   │       └── punteros.go
│   └── ejercicios/
│       ├── swap/
│       │   ├── swap.go
│       │   └── swap_test.go
│       ├── sumar-punteros/
│       │   ├── sumar_punteros.go
│       │   └── sumar_punteros_test.go
│       ├── dividir/
│       │   ├── dividir.go
│       │   └── dividir_test.go
│       ├── inicializar-arreglo/
│       │   ├── inicializar_arreglo.go
│       │   └── inicializar_arreglo_test.go
│       └── maximo/
│           ├── maximo.go
│           └── maximo_test.go
│
├── 07-structs-interfaces/        # ← 2-7
│   ├── ejemplos/
│   │   ├── punto/                # migrado: Punto struct
│   │   │   ├── punto.go
│   │   │   └── main.go
│   │   └── rectangulo-cuadrado/  # migrado
│   │       ├── rectangulo.go
│   │       ├── cuadrado.go
│   │       └── main.go
│   └── ejercicios/               # (mínimos, el fuerte va en 10-oop)
│
├── 08-archivos/                  # ← 2-8 (NUEVO)
│   ├── ejemplos/
│   │   ├── leer-completo/
│   │   │   └── main.go           # os.ReadFile
│   │   ├── leer-lineas/
│   │   │   └── main.go           # bufio.Scanner
│   │   └── escribir/
│   │       └── main.go           # os.WriteFile, os.Create
│   └── ejercicios/
│       ├── contar-lineas/
│       │   ├── contar_lineas.go
│       │   └── contar_lineas_test.go
│       ├── copiar-archivo/
│       │   ├── copiar_archivo.go
│       │   └── copiar_archivo_test.go
│       ├── sumar-numeros/
│       │   ├── sumar_numeros.go
│       │   └── sumar_numeros_test.go
│       ├── agregar-linea/
│       │   ├── agregar_linea.go
│       │   └── agregar_linea_test.go
│       └── numerar-lineas/
│           ├── numerar_lineas.go
│           └── numerar_lineas_test.go
│
├── 09-errores/                   # ← 2-9
│   ├── ejemplos/                 # migrado de 11-errores
│   │   └── main.go
│   └── ejercicios/
│       ├── dividir/
│       │   ├── dividir.go
│       │   └── dividir_test.go
│       ├── clasificar/
│       │   ├── clasificar.go
│       │   └── clasificar_test.go
│       ├── buscar-producto/
│       │   ├── buscar_producto.go
│       │   └── buscar_producto_test.go
│       ├── extraer/
│       │   ├── extraer.go
│       │   └── extraer_test.go
│       └── leer-config/
│           ├── leer_config.go
│           └── leer_config_test.go
│
├── 10-oop/                       # ← 2-10
│   ├── ejemplos/                 # migrado de 10-figuras
│   │   ├── main.go
│   │   └── figuras/
│   │       ├── figura.go
│   │       ├── punto.go
│   │       ├── rectangulo.go
│   │       └── cuadrado.go
│   └── ejercicios/
│       └── sistema-figuras/
│           ├── figuras/
│           │   ├── figura.go      # interface + esqueleto
│           │   ├── rectangulo.go
│           │   └── cuadrado.go
│           ├── exportable/
│           │   └── exportable.go
│           ├── main.go
│           └── figuras_test.go
│
└── extras/                       # contenido que no encaja directamente
    ├── condicionales/            # migrado de 05-condicionales
    └── ciclos/                   # migrado de 06-ciclos
```

## Formato de esqueletos

Cada ejercicio tiene un archivo con `// TODO: implementar`:

```go
package main

// Invertir invierte el orden de los elementos del slice in-place.
func Invertir(s []int) {
    // TODO: implementar
}
```

Y un `*_test.go` asociado:

```go
package main

import "testing"

func TestInvertir(t *testing.T) {
    s := []int{1, 2, 3, 4, 5}
    Invertir(s)
    esperado := []int{5, 4, 3, 2, 1}
    for i := range s {
        if s[i] != esperado[i] {
            t.Errorf("esperado %v, obtuve %v", esperado, s)
            break
        }
    }
}

func TestInvertirVacio(t *testing.T) {
    s := []int{}
    Invertir(s) // no debe panic
}
```

## Convenciones

| Aspecto | Convención |
|---------|-----------|
| Placeholder | `// TODO: implementar` |
| Archivos | `kebab_case.go` (snake_case para evitar conflictos `_test.go`) |
| Tests | `kebab_case_test.go` |
| Paquete | `main` para ejercicios, nombre descriptivo para bibliotecas |
| Retorno por defecto | valores cero (`0`, `""`, `nil`, `false`) |
| Tests | mínimo 2 casos: normal + borde/de error |
| Mensajes test | español, describir qué se espera |
| Line length | 100 caracteres máximo en ejemplos |
| Comentarios | NO agregar comentarios en esqueletos (salvo `// TODO`) |

## Estrategia de ramas

- **`main`**: ejemplos resueltos + esqueletos de ejercicios
- **`soluciones`**: rama con todos los ejercicios completos (idéntica estructura pero con `// TODO:` reemplazado por implementación real)

Los estudiantes clonan `main`, intentan resolver, y si se traban pueden hacer `git checkout soluciones` para ver la respuesta.

## Actualizaciones al apunte

En cada archivo `2-X-tema.md`, al final de la sección de ejercicios, agregar:

> Los esqueletos de estos ejercicios están en `NN-tema/ejercicios/` del repositorio taller-go.
> Las soluciones están disponibles en la rama `soluciones`.

Actualizar la referencia en `2-1-introduccion-go.md` para que apunte a `01-introduccion/ejemplos/` en vez de a `00-hola/`.

## Pasos de implementación (orden sugerido)

1. `git mv` — reestructurar directorios existentes
   - `00-hola` → `01-introduccion/ejemplos/00-hola`
   - `01-tipodatos` → `01-introduccion/ejemplos/01-tipodatos`
   - `02-variables` → `01-introduccion/ejemplos/02-variables`
   - `03-constantes` → `01-introduccion/ejemplos/03-constantes`
   - `04-funciones` → `03-funciones/ejemplos`
   - `05-condicionales` → `extras/condicionales`
   - `06-ciclos` → `extras/ciclos`
   - `07-punteros` → `06-punteros/ejemplos`
   - `08-arreglos` → `04-arreglos-slices/ejemplos`
   - `09-mapas` → `05-maps/ejemplos`
   - `10-figuras/estructuras` → `07-structs-interfaces/ejemplos`
   - `10-figuras/interfaces` → `10-oop/ejemplos`
   - `10-figuras/figuras` → `10-oop/ejemplos/figuras`
   - `11-errores` → `09-errores/ejemplos`

2. Crear ejemplos nuevos
   - `02-paquetes-y-modulos/ejemplos/`
   - `08-archivos/ejemplos/`

3. Crear esqueletos + tests (todos los `ejercicios/`)

4. `Makefile` + actualizar `go.mod` si hace falta

5. Verificar: `go build ./...` y `go test ./...`

6. Crear rama `soluciones` (copia de `main` con esqueletos resueltos por `sed` o manual)

7. Actualizar referencias en el apunte

8. Commit final
