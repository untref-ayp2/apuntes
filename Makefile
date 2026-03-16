## help: muestra este mensaje de ayuda
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## install: instala las dependencias necesarias
.PHONY: install
install:
	pip install --requirement requirements.txt

## fmt: formatea todo el contenido del libro y código
.PHONY: fmt
fmt:
	mdformat --number contenidos/**/*.md
	mdformat --number .opencode/**/*.md
	mdformat --number *.md
	black --line-length 120 .

## build: compila el libro en formato HTML
.PHONY: build
build: clean
	cd contenidos && myst build --html --execute

## pdf: compila el libro en formato PDF (requiere template disponible)
.PHONY: pdf
pdf:
	cd contenidos && myst build --pdf --execute

## clean: elimina todos los archivos generados por la compilación
.PHONY: clean
clean:
	cd contenidos && myst clean --all --yes

## start: inicia el servidor de desarrollo ejecutando las celdas
.PHONY: start
start:
	cd contenidos && myst start --execute
