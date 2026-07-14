---
label: git
---

# Introducción a Git y GitHub

Cuando trabajamos en un proyecto, es común que necesitemos compartir nuestro trabajo con otros. Para ello, es necesario contar con una herramienta que nos permita llevar un registro de los cambios realizados, y que nos permita compartirlos con otros.

Cuando trabajamos en equipo en un proyecto surgen muchas preguntas:

- ¿Cómo **sincronizamos** el trabajo?
- ¿Cómo **dividimos** las partes a realizar?
- ¿Cómo volvemos a **juntarlas**?
- ¿Qué sucede si la **persona** que iba a juntar todo, no llega a hacerlo?
- ¿Qué hacemos si hay que volver a una **versión anterior**?
- ¿Cómo hacemos **experimentos** sobre el trabajo?

Para responder a estas preguntas, existen herramientas que nos permiten llevar un registro de los cambios realizados en un proyecto y compartirlos con otros. Una de las herramientas más utilizadas es **Git**.

Git es un sistema de control de versiones (SCV).

## ¿Qué es un SCV?

Un sistema de control de versiones es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante.

```{admonition} Analogía
:class: note

Imaginemos que Git es una cámara de fotos. En este caso, la analogía es muy buena, ya que Git es la herramienta, y no "la cosa" que haremos.
```

## Configuración inicial de Git

Antes de empezar a usar Git, es necesario configurar tu nombre y correo electrónico. Git los usa para firmar cada uno de tus _commits_:

```{code-block} console
~ $ git config --global user.name "Tu Nombre"

~ $ git config --global user.email "tuemail@ejemplo.com"
```

Este paso se hace una sola vez. Git asocia esos datos a cada _commit_ que crees. Se puede verificar la configuración con:

```{code-block} console
~ $ git config --global --list
user.name=Tu Nombre
user.email=tuemail@ejemplo.com
```

## Creando un repositorio

El primer paso, es la creación de un repositorio Git. Nótese que no es "un Git", sino un repositorio (repo). Entonces, dentro de la carpeta donde queremos crear nuestro repo, ejecutamos el siguiente comando:

```console
~ $ mkdir ayp2-repo

~ $ cd ayp2-repo

~/ayp2-repo $ git init
Initialized empty Git repository in ~/ayp2-repo/.git/
```

Antes de comenzar a hacer cambios, queremos ver el estado de nuestro repo:

```console
~/ayp2-repo $ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

```{admonition} ¡Consejo!
:class: hint

Es muy importante siempre prestar atención a los mensajes que los distintos comandos de Git nos devuelven. En este caso, nos dice que no hay nada para hacer, ya que no hemos creado nada aún.

En general, son comentarios útiles y nos ayudan a saber que posibilidades tenemos desde donde estamos parados.
```

Ahora podemos empezar a trabajar en nuestro proyecto. Cuando hayamos creado una porción de código que consideramos suficiente, debemos indicar cuáles de esos cambios queremos dejar asentados en el registro de cambios de nuestro repo.

## Registrando cambios

Imaginemos que hemos creado un archivo llamado `ejercicios.go` y hemos escrito un par de líneas de código. Si ahora ejecutamos `git status`, veremos que el archivo no está en el registro de cambios, por lo que debemos primero **agregarlos**.

```{code-block} console
---
emphasize-lines: 9
---
~/ayp2-repo $ nvim ejercicios.go

~/ayp2-repo $ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ejercicios.go

nothing added to commit but untracked files present (use "git add" to track)
```

Podemos ver que Git no solo nos cuenta cuál es el estado de nuestros cambios, sino que también nos dice qué comando deberíamos usar para agregar el archivo al registro de cambios, entonces hagamos eso mismo:

```{code-block} console
---
emphasize-lines: 8
---
~/ayp2-repo $ git add ejercicios.go

~/ayp2-repo $ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   ejercicios.go
```

Ahora nuestro archivo pasó del grupo de los _Untracked files_ a _Changes to be committed_. Esto significa que ya está preparado para ser registrado en el repo.

Estamos listos para dejar registro de nuestro primer cambio. Como lo que hacemos es registrar la historia de cómo nuestro código va evolucionando, debemos llevar una bitácora que nos servirá de guía para saber qué hicimos en cada momento. En este caso, la bitácora es un mensaje que describe el cambio que estamos haciendo.

```{code-block} console
~/ayp2-repo $ git commit -m "Primera versión de ejercicios.go"
[main (root-commit) a068b64] Primera versión de ejercicios.go
 1 file changed, 5 insertions(+)
 create mode 100644 ejercicios.go
```

Si ahora volvemos a consultar el estado del repo (cosa que como ya se habrán dado cuenta, se hace muy seguido), podemos ver que ya no hay cambios pendientes de registrar y nuestro _working tree_ está limpio.

```{code-block} console
---
emphasize-lines: 3
---
~/ayp2-repo $ git status
On branch main
nothing to commit, working tree clean
```

Cuando "commiteamos" los cambios indicamos un mensaje, ese mensaje junto con información relacionada al commit generado puede ser consultado usando:

```{code-block} console
~/ayp2-repo $ git log
commit a068b643d8b6bb6b8ba51d51e919694dd665ed36 (HEAD -> main)
Author: Santiago Rojo <tiagox@gmail.com>
Date:   Fri Mar 28 18:38:18 2025 -0300

    Primera versión de ejercicios.go
```

```{admonition} En resumen
:class: note

Desde aquí en adelante, cada vez que hagamos un cambio en el repo, debemos seguir los mismos pasos:

1. Editar el archivo
2. Agregarlo al registro de cambios: `git add <archivo>`
3. Registrar el cambio con un mensaje: `git commit -m "<mensaje>"`

... volver al principio.
```

### Ignorando archivos

No todos los archivos de un proyecto deberían estar en el repositorio. Archivos ejecutables, binarios compilados o archivos temporales del editor no forman parte del código fuente. Para indicarle a Git qué archivos ignorar, se crea un archivo `.gitignore` en la raíz del repositorio:

```{code-block} text
# Compilados
*.exe
*.out

# Archivos temporales
*.tmp
*.log
```

Cada línea del `.gitignore` es un patrón de archivos que Git no va a trackear. Esto mantiene el repositorio limpio y evita subir archivos innecesarios.

## Trabajando en equipo

### _Branches_

Las _branches_ o ramas, nos permiten trabajar en paralelo en un proyecto. Podríamos crear ramas paralelas de desarrollo en donde hacer pruebas o cambios experimentales, para luego decidir si son cambios que queremos integrar a nuestra rama principal o no.

Para crear una nueva rama, usamos el comando:

```{code-block} console
~/ayp2-repo $ git switch -c pruebas
Switched to a new branch 'pruebas'
```

Esto crea una nueva rama llamada `pruebas` y nos "cambia" a esa rama. Si ahora hacemos `git status`, veremos que estamos en la rama `pruebas`.

```{code-block} console
---
emphasize-lines: 2
---
~/ayp2-repo $ git status
On branch pruebas
nothing to commit, working tree clean
```

Para listar las _branches_ que tenemos, usamos el comando `git branch`:

```{code-block} console
---
emphasize-lines: 3
---
~/ayp2-repo $ git branch
  main
* pruebas
```

El asterisco indica en qué rama estamos parados. En este caso, en la rama `pruebas`.

Para movernos entre las distintas _branches_, usamos el mismo comando `git switch`. Por ejemplo, si quisiéramos volver a la rama principal, usaríamos:

```{code-block} console
~/ayp2-repo $ git switch main
Switched to branch 'main'
```

El flujo de trabajo es el mismo que comentamos al principio de este capítulo. Primero editamos el archivo, luego lo agregamos al registro de cambios y finalmente lo registramos con un mensaje.

### Integrando los cambios de nuestra rama

Si quisiéramos incorporar la _branch_ `pruebas` que creamos anteriormente, debemos utilizar el comando `git merge`.

Primero debemos estar parados sobre la _branch_ donde queremos integrar los cambios. En este caso, la rama principal `main`.

```{code-block} console
~/ayp2-repo $ git switch main
Switched to branch 'main'

~/ayp2-repo $ git merge pruebas
Updating a068b64..13495a7
Fast-forward
 ejercicios.go | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### Resolviendo conflictos

Si dos ramas modifican las mismas líneas de un archivo, Git no puede decidir automáticamente qué versión conservar. En ese caso, el *merge* se pausa y Git marca el conflicto en el archivo:

```{code-block} console
~/ayp2-repo $ git merge pruebas
Auto-merging ejercicios.go
CONFLICT (content): Merge conflict in ejercicios.go
Automatic merge failed; fix conflicts and then commit the result.
```

Al abrir el archivo conflictivo se ven marcadores que indican los cambios enfrentados:

```{code-block} go
funcion := "saludar"
<<<<<<< HEAD
fmt.Println("Hola")
=======
fmt.Println("Hello")
>>>>>>> pruebas
```

La sección entre `<<<<<<< HEAD` y `=======` es el cambio en la rama actual. La sección entre `=======` y `>>>>>>> pruebas` es el cambio en la rama `pruebas`. Para resolver, hay que editar el archivo, quedarse con una de las versiones (o una combinación), eliminar los marcadores y luego:

```{code-block} console
~/ayp2-repo $ git add ejercicios.go

~/ayp2-repo $ git commit -m "Resuelve conflicto entre main y pruebas"
```

Git registra el *commit* de *merge* con la resolución.

### Clonando un repositorio existente

Si ya existe un repositorio en GitHub (o cualquier otro servidor), no hace falta crearlo desde cero con `git init`. Se puede obtener una copia local completa con `git clone`:

```{code-block} console
~ $ git clone https://github.com/usuario/repositorio.git

~ $ cd repositorio

~/repositorio $ git status
On branch main
nothing to commit, working tree clean
```

Esto descarga todo el historial del proyecto y deja el repo listo para trabajar.

### Configurando un repositorio remoto

Para compartir un repositorio local a través de GitHub, primero hay que asociarlo con un remoto:

```{code-block} console
~/ayp2-repo $ git remote add origin https://github.com/tuusuario/ayp2-repo.git
```

El nombre `origin` es una convención que identifica al remoto principal.

### Subiendo cambios

Una vez configurado el remoto, se pueden enviar los *commits* locales:

```{code-block} console
~/ayp2-repo $ git push -u origin main
```

El flag `-u` (o `--set-upstream`) vincula la rama local `main` con la remota, de modo que en adelante alcance con escribir solo `git push`.

### Descargando cambios

Para traer los últimos cambios del remoto al repositorio local:

```{code-block} console
~/ayp2-repo $ git pull
```

`git pull` combina dos operaciones: descarga los cambios del remoto (`git fetch`) y los integra en la rama actual (`git merge`). Es el comando que se usa para mantenerse al día con el trabajo de otros miembros del equipo.

## Flujo de trabajo típico

1. `git status` — ver el estado actual del repositorio
2. `git add <archivo>` — preparar los cambios para el *commit*
3. `git commit -m "<mensaje>"` — registrar los cambios
4. `git push` — enviar los *commits* al remoto (si existe)
5. `git pull` — traer los cambios del remoto (si se trabaja en equipo)

## Links recomendados

- [Git-Book](https://git-scm.com/book/es/v2)
