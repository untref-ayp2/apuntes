# Instalación y configuración del entorno

Si deseas desarrollar y/o compilar el libro de Algoritmos y Programación II, debes:

1. Clona este repositorio

2. Instalar las dependencias del proyecto.

    Se recomiendo crear un entorno virtual de python para trabajar con este proyecto.

    Luego podemos ejecutar:

    ```sh
    pip install -r requirements.txt
    ```

    o bien,

    ```sh
    make install
    ```

    Una vez instaladas las dependencias de Python (principalmente `jupyterlab` y `jupyter-book`), debemos instalar el kernel de Go para Jupyter: en nuestro caso utilizamos `gophernotes`.

    Ya que las instrucciones de instalación dependen de cada sistema operativo y entorno dejamos el link al repositorio del módulo Go que explica como instalar y probar ese kernel:

    <https://github.com/gopherdata/gophernotes>

3. (Opcional) Edita los archivos fuente del libro ubicados en el directorio `algoritmos_y_programación_2/`

4. Para compilar el libre ejecutar:

    ```sh
    jupyter-book build .
    ```

    o bien,

    ```sh
    make build
    ```

    Una versión HTML completamente renderizada del libro se construirá en `_build/html/`.

5. (Opcional) Se puede servir este HTML utilizando el siguiente comando de Python:

    ```sh
    python -m http.server --directory _build/html
    ```

    o bien,

    ```sh
    make server
    ```

## Recomendaciones

Antes de commitear los cambios en el contenido es recomendable formatear las notebooks, para estandarizar el formato. Simplemente corriendo:

```sh
make fmt
```

Todo el código en los documentos Jupyter quedará perfectamente formateado, incluso se eliminan las salidas y la metadata propia de cada entorno en que dichas notebooks se ejecutan.
