# Apuntes de Algoritmos y Programación II

## Instalación y configuración del entorno

Si deseas desarrollar y/o compilar el libro de Algoritmos y Programación II, debes:

1. Clonar este repositorio

2. Instalar las dependencias del proyecto.

   > [!TIP]
   > Se recomienda crear un entorno virtual de python para trabajar con este proyecto.

   Luego podemos ejecutar:

   ```sh
   pip install -r requirements.txt
   ```

   o bien,

   ```sh
   make install
   ```

   Una vez instaladas las dependencias de Python (principalmente `jupyter-book`), debemos instalar el kernel de Go para Jupyter: en nuestro caso utilizamos `gophernotes`.

   Ya que las instrucciones de instalación dependen de cada sistema operativo y entorno dejamos el link al repositorio del módulo Go que explica como instalar y probar ese kernel:

   <https://github.com/gopherdata/gophernotes>

3. (Opcional) Edita los archivos fuente del libro ubicados en el directorio `contenidos`

4. Para compilar el libre ejecutar:

   ```sh
   jupyter-book build contenidos
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
