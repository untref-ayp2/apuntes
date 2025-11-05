---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
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
Imaginemos que Git es una cámara de fotos. En este caso, la analogía es muy buena, ya que Git es la herramienta, y no "la cosa" que haremos.
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

```{hint} ¡Consejo!
Es muy importante siempre prestar atención a los mensajes que los distintos comandos de Git nos devuelven. En este caso, nos dice que no hay nada para hacer, ya que no hemos creado nada aún.

En general, son comentarios útiles y nos ayudan a saber que posibilidades tenemos desde donde estamos parados.
```

Ahora podemos empezar a trabajar en nuestro proyecto. Cuando hayamos creado una porción de códido que consideramos suficiente, debemos indicar cuales de esos cambios queremos dejar asentados en el registro de cambios de nuestro repo.

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

Podemos ver que Git no solo nos cuenta cual es el estado de nuestros cambios, sino que también nos dice que comando deberiamos usar para agregar el archivo al registro de cambios, entonces hagamos eso mismo:

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

Ahora nuestro archivo paso del grupo de los _Untracked files_ a _Changes to be committed_. Esto significa que ya está preparado para ser registrado en el repo.

Estamos listos para dejar registro de nuestro primer cambio. Como lo que hacemos es registrar la historia de como nuestro código va evolucionando, debemos llevar una bitácora que nos servirá de guía para saber qué hicimos en cada momento. En este caso, la bitácora es un mensaje que describe el cambio que estamos haciendo.

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

```{note} En resumen
Desde aquí en adelante, cada vez que hagamos un cambio en el repo, debemos seguir los mismos pasos:

1. Editar el archivo
2. Agregarlo al registro de cambios: `git add <archivo>`
3. Registrar el cambio con un mensaje: `git commit -m "<mensaje>"`

... volver al principio.
```

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

Si quisiéramos incorporar la _branch_ `prueba` que creamos anteriormente, debemos utilizar el comando `git merge`.

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

Si hubiera cambios similares en dos ramas que vamos a integrar, pueden suceder que haya cambios sobre las mismas porciones de código y que Git no pueda decidir como mezclarlas. En esos casos, Git nos nos preguntará qué cambio deseamos conservar y luego podremos completar la integración.

La resolución de conflictos "de merge" es una tarea que puede asustar, pero es simple si se trabaja en forma ordenada.

### Compartiendo nuestro repo

Para subir nuestro contenido a un repo remoto, debemos…

```{code-block} console
~/ayp2-repo $ git push
```

Y si en cambio, queremos recibir la última versión disponible, debemos…

```{code-block} console
~/ayp2-repo $ git pull
```

<center>
  <iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/yEs0E3PnGuI?si=fXWPaE19xyzX9Gug"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</center>

## Links recomendados

- [Git-Book](https://git-scm.com/book/es/v2){target="\_blank"}
