## help: muestra este mensaje de ayuda
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## install: instala las dependencias necesarias
.PHONY: install
install:
	pip install --requirement requirements.txt

## build: compila el libro
.PHONY: build
build:
	jupyter-book build contenidos

## clean: elimina los archivos generados
.PHONY: clean
clean:
	jupyter-book clean contenidos

# Puerto por defecto para levantar el servidor http
PORT ?= 8080

## server: levanta un servidor http para visualizar el libro
.PHONY: server
server: build
	python -m http.server $(PORT) --directory contenidos/_build/html
