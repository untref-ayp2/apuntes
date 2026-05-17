---
label: archivos
---

# Archivos

Trabajar con archivos es una tarea común en casi cualquier programa. Go provee el paquete `os` para operaciones básicas de entrada/salida y `bufio` para lectura y escritura con *buffer*.

## Leer un archivo completo

La forma más simple de leer un archivo de texto es con `os.ReadFile`, que lee todo el contenido de una sola vez y devuelve un `[]byte`:

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    datos, err := os.ReadFile("ejemplo.txt")
    if err != nil {
        fmt.Println("Error al leer el archivo:", err)
        return
    }
    fmt.Println(string(datos))
}
```

`os.ReadFile` se encarga de abrir y cerrar el archivo automáticamente. Devuelve los bytes leídos y un error. Si el archivo no existe, el error será del tipo que indica que el archivo no fue encontrado.

## Escribir un archivo completo

Para escribir datos en un archivo, `os.WriteFile` recibe el nombre del archivo, los datos como `[]byte` y los permisos:

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    contenido := []byte("Hola, archivo!\n")
    err := os.WriteFile("salida.txt", contenido, 0644)
    if err != nil {
        fmt.Println("Error al escribir el archivo:", err)
        return
    }
    fmt.Println("Archivo escrito correctamente")
}
```

El tercer parámetro son los permisos en octal (`0644` significa lectura/escritura para el dueño, solo lectura para el resto). `os.WriteFile` crea el archivo si no existe, o lo trunca si ya existe.

## Abrir y cerrar archivos manualmente

Para tener más control, podemos abrir un archivo con `os.Open` (solo lectura) u `os.Create` (escritura, trunca si existe). Es importante cerrar el archivo con `Close` cuando terminamos, generalmente usando `defer`:

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    archivo, err := os.Open("ejemplo.txt")
    if err != nil {
        fmt.Println("Error al abrir el archivo:", err)
        return
    }
    defer archivo.Close()

    // leer del archivo...
    fmt.Println("Archivo abierto correctamente")
}
```

`defer archivo.Close()` garantiza que el archivo se cierre cuando la función termina, incluso si ocurre un error o *panic* después de abrirlo.

## Leer línea por línea con `bufio.Scanner`

Cuando el archivo es grande o queremos procesarlo línea por línea, `bufio.Scanner` es la herramienta adecuada:

```go
package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    archivo, err := os.Open("ejemplo.txt")
    if err != nil {
        fmt.Println("Error al abrir el archivo:", err)
        return
    }
    defer archivo.Close()

    scanner := bufio.NewScanner(archivo)
    linea := 1
    for scanner.Scan() {
        fmt.Printf("%d: %s\n", linea, scanner.Text())
        linea++
    }

    if err := scanner.Err(); err != nil {
        fmt.Println("Error al leer el archivo:", err)
    }
}
```

`scanner.Scan()` avanza a la siguiente línea y devuelve `true` mientras haya datos. `scanner.Text()` devuelve la línea actual (sin el salto de línea). Al finalizar, `scanner.Err()` indica si hubo algún error durante la lectura.

## Escribir con formato

Para escribir datos formateados en un archivo, podemos usar `fmt.Fprintf`, que es como `fmt.Printf` pero escribe en un archivo (o cualquier otro `io.Writer`):

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    archivo, err := os.Create("notas.txt")
    if err != nil {
        fmt.Println("Error al crear el archivo:", err)
        return
    }
    defer archivo.Close()

    fmt.Fprintf(archivo, "Alumno: %s\n", "Martín")
    fmt.Fprintf(archivo, "Nota: %d\n", 9)
    fmt.Fprintf(archivo, "Materia: %s\n", "Algoritmos II")
    fmt.Fprintln(archivo, "Primera línea")
    fmt.Fprintln(archivo, "Segunda línea")
}
```

## Ejercicios

Los ejercicios de este capítulo están en `09-archivos/ejercicios/`
del repositorio [taller-go](https://github.com/untref-ayp2/taller-go.git).
Cada directorio contiene un `README.md` con el enunciado y los esqueletos
para resolverlo.
