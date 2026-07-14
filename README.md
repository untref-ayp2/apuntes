# Apuntes de Algoritmos y Programación II

## Instalación y configuración del entorno

Si deseas desarrollar y/o compilar el apunte de Algoritmos y Programación II, necesitás:

> [!TIP]
> Se recomienda crear un entorno virtual de Python para trabajar con este proyecto.

1. **Clonar** este repositorio.

2. **Instalar dependencias Python**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Instalar dependencias del sistema**:

   - **Typst** (compilador de PDF):

     - **Arch / CachyOS**: `sudo pacman -S typst`
     - **Debian / Ubuntu**: `sudo apt install typst`
     - **macOS**: `brew install typst`
     - O descargar desde <https://github.com/typst/typst/releases>

   - **MyST** (build system):

     ```sh
     npm install -g mystmd
     ```

   - **Fuente Roboto** (necesaria para el PDF):

     - **Arch / CachyOS**: `sudo pacman -S ttf-roboto`
     - **Debian / Ubuntu**: `sudo apt install fonts-roboto`
     - **Fedora**: `sudo dnf install google-roboto-fonts`
     - **macOS**: `brew install --cask font-roboto`

4. **Instalar `make`** (opcional, pero facilita los comandos):

   - En sistemas Unix ya suele estar instalado.
   - En Windows: `winget install -e --id GnuWin32.Make`

## Compilar el libro

### Con `make` (recomendado)

| Comando        | Qué hace                                          |
| -------------- | ------------------------------------------------- |
| `make build`   | Compila HTML + PDF (limpia y reconstruye todo)    |
| `make pdf`     | Genera solo el PDF (vía `scripts/build_pdf.py`)   |
| `make start`   | Inicia servidor de desarrollo con recarga en vivo |
| `make clean`   | Elimina archivos generados por la compilación     |
| `make fmt`     | Formatea Markdown y Python                        |
| `make install` | Instala dependencias Python                       |
| `make help`    | Muestra todos los comandos disponibles            |

### Sin `make`

- **HTML**: `cd contenidos && myst build --execute`
- **PDF**: `python3 scripts/build_pdf.py`
- **Servidor de desarrollo**: `cd contenidos && myst start --execute`

El HTML generado queda en `contenidos/_build/html` y el PDF en `contenidos/exports/apunte-ayp2.pdf`.

### Despliegue automático

Al hacer push a `main`, un workflow de GitHub Actions compila el HTML y lo despliega en GitHub Pages. La configuración está en `.github/workflows/deploy.yml`.

## Estructura del proyecto

```text
├── AGENTS.md                  # Directivas para asistentes IA
├── ESTILOS.md                 # Guía de estilo canónica
├── Makefile                   # Automatización de tareas
├── requirements.txt           # Dependencias Python
├── scripts/build_pdf.py       # Generación del PDF (pre-procesamiento + Typst)
├── .github/workflows/
│   └── deploy.yml             # CI/CD: build + deploy a GitHub Pages
├── contenidos/
│   ├── myst.yml               # Configuración de MyST
│   ├── introduccion.md
│   ├── references.bib
│   ├── _static/
│   │   ├── applets/           # Applets HTML/JS interactivos
│   │   ├── figures/           # Imágenes SVG (con pares light/dark)
│   │   ├── code/              # Código fuente Go
│   │   ├── css/custom.css     # Estilos personalizados
│   │   └── js/                # JavaScript auxiliar
│   ├── templates/
│   │   └── plain_typst_book_ayp2/  # Template Typst para PDF
│   ├── exports/
│   │   └── apunte-ayp2.pdf    # PDF generado
│   ├── 1-presentacion/
│   ├── 2-taller-de-go/
│   ├── 3-estructuras-de-datos/
│   ├── 4-diseno-de-algoritmos/
│   └── 5-anexos/
```
