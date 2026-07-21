---
label: herramientas
---

# Herramientas para Cursar

En esta materia vamos a usar varias herramientas: un editor de código, un lenguaje de programación, un sistema de control de versiones y una plataforma para recibir y entregar trabajos. Este anexo explica cómo instalar y usar cada una.

```{important}
La mayoría de las instrucciones asumen que empezás desde cero, sin nada instalado.
```

## Instalación de Git y Git Bash

Git es el sistema de control de versiones que usamos para gestionar el código. En Windows, al instalar Git se incluye **Git Bash**, una terminal que funciona como la de Linux.

::::{tab-set}
:::{tab} Windows
1. Ir a https://git-scm.com y descargar el instalador.
2. Ejecutar el `.exe` y dejar las opciones por defecto.
3. Al finalizar, abrir **Git Bash** desde el menú Inicio.
4. Verificar la instalación:

   ```console
   $ git --version
   git version 2.4x.x
   ```
:::

:::{tab} Linux
```console
$ sudo apt install git
```

O el comando equivalente según la distribución (pacman, dnf, etc.).
Verificar:

```console
$ git --version
git version 2.4x.x
```
:::

:::{tab} macOS
**Opción A** — Xcode Command Line Tools (incluye Git):

```console
$ xcode-select --install
```

**Opción B** — Descargar desde https://git-scm.com.

Verificar:

```console
$ git --version
git version 2.4x.x
```
:::
::::

## Terminal / línea de comandos

La terminal permite ejecutar comandos para navegar archivos, correr programas y usar Git. En Windows usamos **Git Bash**; en Linux y macOS la terminal nativa.

Los comandos básicos son los mismos en los tres sistemas:

| Comando | Qué hace |
|---|---|
| `pwd` | Muestra el directorio actual |
| `ls` | Lista los archivos y carpetas |
| `cd <carpeta>` | Cambia al directorio indicado |
| `cd ..` | Sube un nivel |
| `mkdir <nombre>` | Crea una carpeta |
| `touch <archivo>` | Crea un archivo vacío |
| `Tab` | Autocompleta comandos y rutas |
| ⬆ ⬇ | Navega el historial de comandos |

```{tip}
En Git Bash (Windows) los comandos son los mismos que en Linux y macOS.
No hace falta aprender comandos diferentes para cada sistema.
```

Estructura de rutas:

- **Windows (Git Bash):** `/c/Users/TuUsuario/` equivale a `C:\Users\TuUsuario\`
- **Linux:** `/home/tu-usuario/`
- **macOS:** `/Users/tu-usuario/`

## Instalación de Go

Necesitamos Go para compilar y ejecutar los ejercicios de los talleres.

::::{tab-set}
:::{tab} Windows
1. Ir a https://go.dev/dl y descargar el `.msi` para Windows.
2. Ejecutar el instalador. Agrega Go al PATH automáticamente.
3. Abrir **Git Bash** y verificar:

   ```console
   $ go version
   go version go1.22.x windows/amd64
   ```
:::

:::{tab} Linux
```console
$ sudo apt install golang
```

O descargar el tarball oficial desde https://go.dev/dl y seguir las
instrucciones de instalación.

Verificar:

```console
$ go version
go version go1.22.x linux/amd64
```
:::

:::{tab} macOS
**Opción A** — Descargar el `.pkg` desde https://go.dev/dl.

**Opción B** — Con Homebrew:

```console
$ brew install go
```

Verificar:

```console
$ go version
go version go1.22.x darwin/amd64
```
:::
::::

## Visual Studio Code

VS Code es el editor que usamos en la cursada. Es liviano y tiene soporte para Go con las extensiones adecuadas.

::::{tab-set}
:::{tab} Windows
1. Ir a https://code.visualstudio.com y descargar el instalador.
2. Ejecutar el `.exe`. Marcar **"Agregar a PATH"** durante la instalación.
3. Abrir VS Code desde el menú Inicio.
:::

:::{tab} Linux
Descargar el `.deb` o `.rpm` desde https://code.visualstudio.com, o usar el
gestor de paquetes:

```console
$ sudo snap install code --classic
```
:::

:::{tab} macOS
Descargar el `.zip` desde https://code.visualstudio.com, o con Homebrew:

```console
$ brew install --cask visual-studio-code
```
:::
::::

## Extensiones de VS Code

Para trabajar con Go necesitamos algunas extensiones. Desde VS Code:

1. Ir al icono de extensiones (cuadrados en la barra izquierda, o `Ctrl+Shift+X`).
2. Buscar cada extensión por nombre o ID.
3. Click en **Install**.

| Extensión | ID | Para qué sirve |
|---|---|---|
| **Go** | `golang.go` | Autocompletado, formato, navegación, análisis de código |
| **Error Lens** | `usernamehw.errorlens` | Muestra los errores inline, al lado del código |
| **GitHub Pull Requests** | `GitHub.vscode-pull-request-github` | Revisar y comentar Pull Requests (incluyendo el Feedback PR) |
| Go Test Explorer UI | `premparihar.gotestexplorer` | Explorador visual de tests (opcional) |

## Slack

Usamos Slack para la comunicación del curso: anuncios, consultas, canales por tema.

1. Crear una cuenta en https://slack.com si no tenés una.
2. Unirte al workspace del curso con el enlace que te dan los docentes.
3. Explorar los canales: `#general` (anuncios), `#consultas`, `#taller-go`, etc.
4. Para consultar a un docente o ayudante, escribir `@usuario` en cualquier canal.
5. Las notificaciones llegan en la aplicación y por correo.

## Classroom50 y gh CLI

Classroom50 es la plataforma que usamos para recibir y entregar los trabajos. Se accede por línea de comandos con `gh` (GitHub CLI) o por web.

La materia se dicta en dos sedes. Cada una tiene su propia organización:

| Sede | Organización |
|---|---|
| UNTREF | `untref-ayp2-estudiantes` |
| CUDI | `cudi-ayp2-estudiantes` |

Usar la que corresponda a tu cursada en todos los comandos.

### Instalación de gh CLI

::::{tab-set}
:::{tab} Windows
Descargar el instalador desde https://cli.github.com y ejecutarlo.
Luego abrir Git Bash y continuar con los pasos siguientes.
:::

:::{tab} Linux
```console
$ sudo apt install gh
```

O seguir las instrucciones en https://cli.github.com.
:::

:::{tab} macOS
```console
$ brew install gh
```
:::
::::

### Extensión de Classroom50

```console
$ gh extension install foundation50/gh-student
```

### Iniciar sesión

```console
$ gh student login
```

Se abre el navegador para autorizar. Completar el proceso y volver a la terminal.

### Aceptar una tarea

```console
$ gh student accept untref-ayp2-estudiantes <clase> <tarea>
```

Reemplazar `<clase>` por el nombre de tu clase y `<tarea>` por el slug de la tarea (ej. `taller-go`).

Esto crea un repositorio propio en GitHub con el código inicial.

### Entregar

```console
$ cd <repositorio>
$ gh student submit
```

Esto ejecuta los tests automáticos y publica el resultado. Se puede entregar varias veces; la última entrega es la que cuenta.

## Classroom50 desde la web

Además de la línea de comandos, Classroom50 se puede usar desde el navegador.

1. Ir a https://classroom50.org.
2. Click en **"Sign in with GitHub"** y autorizar la aplicación.
3. Seleccionar la organización (`untref-ayp2-estudiantes` o `cudi-ayp2-estudiantes`).
4. Elegir la clase correspondiente.
5. Se ven las tareas asignadas, su estado (pendiente/entregada) y el puntaje obtenido.
6. Desde cada tarea se puede acceder al repositorio, al Feedback PR y al detalle de la última entrega.

## Feedback PR

El **Feedback PR** es un Pull Request que se crea automáticamente al entregar la primera vez. Es el espacio donde los docentes dejan comentarios sobre tu código.

Está en la pestaña **"Pull requests"** del repositorio, con el título **Feedback**.

### Desde el navegador web (GitHub)

1. Ir al repositorio en github.com.
2. Click en la pestaña **Pull requests**.
3. Click en **"Feedback"**.
4. Para comentar una línea específica:
   - Click en el número de línea → icono `+` → escribir comentario → **"Add single comment"**.
5. Para hacer una consulta general:
   - Ir al final del PR, escribir en la caja de texto y click en **"Comment"**.
6. Para **@mencionar** a un docente o ayudante:
   - Escribir `@usuario` (ej. `@martin-albarracin`).
   - Le llega una notificación por correo.
7. Para responder a un comentario:
   - Click en **"Reply"** debajo del comentario.
8. Las notificaciones se ven en la campana de GitHub (arriba a la derecha).

### Desde VS Code

1. Abrir el repositorio en VS Code.
2. Click en el icono de PR en la barra lateral izquierda (extensión GitHub Pull Requests).
3. Seleccionar **"Feedback"** de la lista.
4. Comentar una línea: click en el número de línea → icono de comentario → escribir.
5. @mencionar y responder funciona igual que en la web.

## Cómo ejecutar tests

Los tests verifican que tu código funciona correctamente. Se ejecutan desde la terminal (Git Bash, terminal de Linux o macOS).

### Todos los tests

```console
$ go test ./...
```

### Tests de un tema específico

```console
$ go test ./01-introduccion/...
```

### Con detalle (muestra cada caso)

```console
$ go test -v ./...
```

### Usando Makefile (si el repo tiene uno)

```console
$ make test
```

### Cómo leer el output

- `ok` — todos los tests pasaron.
- `FAIL` — algún test falló.
- `=== RUN` — nombre del test que se está ejecutando.
- `--- PASS` — test pasado.
- `--- FAIL` — test fallado, con el mensaje de error.
