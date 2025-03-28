# Apuntes de Algoritmos y Programación II

## Instalación y configuración del entorno

Si deseas desarrollar y/o compilar el libro de Algoritmos y Programación II, debes:

> [!TIP]
> Para esta guía se asume que Python y Go instalados en el sistema.
>
> Se recomienda crear un entorno virtual de Python para trabajar con este proyecto.

1. Clonar este repositorio

2. Instalar las dependencias del proyecto.

   ```sh
   pip install -r requirements.txt
   ```

   - Una vez instaladas las dependencias de Python (principalmente `jupyter-book`), debemos instalar el kernel de Go para Jupyter: en nuestro caso utilizamos `gophernotes`.

     Ya que las instrucciones de instalación dependen de cada sistema operativo y entorno dejamos el link al repositorio del módulo Go que explica como instalar y probar ese kernel:

     <https://github.com/gopherdata/gophernotes>

3. (Opcional) Edita los archivos fuente del libro ubicados en el directorio `contenidos`

4. Para compilar el libre ejecutar:

   ```sh
   jupyter-book build contenidos
   ```

   Una versión HTML completamente renderizada del libro se construirá en `contenidos/_build/html`.

5. (Opcional) Se puede servir este HTML utilizando el siguiente comando de Python:

   ```sh
   python -m http.server --directory contenidos/_build/html
   ```

### Ejecutando comando con `make`

`make` es una herramienta de automatización de tareas muy útil. En este proyecto se utiliza para instalar las dependencias, compilar el libro y servirlo en un servidor web local.

En el apartado anterior hemos explicado como se instalan las dependencies de este proyecto y como "construir" el libro. A continuación se detallan los comandos que se pueden ejecutar con `make`.

Primero debemos asegurarnos de que tenemos `make` disponible en nuestro sistema. En sistemas Unix (como Linux o MacOS) es probable que ya lo tengamos instalado. En Windows, se puede instalar con [`winget`](https://docs.microsoft.com/en-us/windows/package-manager/winget/).

```sh
winget install -e --id GnuWin32.Make
```

Una vez que tenemos `make` disponible, podemos ejecutar los siguientes comandos:

- `make install`: Instala las dependencias del proyecto.
- `make build`: Compila el libro.
- `make server`: Sirve el libro en un servidor web local.

Esto simplifica el proceso de desarrollo y permite que cualquier persona pueda compilar y servir el libro sin tener que recordar los comandos de Python o Jupyter Book.
