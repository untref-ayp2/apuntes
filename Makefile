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

## build: compila el libro ejecutando las celdas (HTML + PDF)
.PHONY: build
build: clean pdf
	cd contenidos && myst build --execute
	mkdir -p contenidos/_build/site/public/applets
	cp -r contenidos/_static/applets/. contenidos/_build/site/public/applets/

## pdf: genera PDF con pre-procesamiento (scripts/build_pdf.py)
.PHONY: pdf
pdf:
	python3 scripts/build_pdf.py

## clean: elimina todos los archivos generados por la compilación
.PHONY: clean
clean:
	cd contenidos && myst clean --all --yes

## start: construye el sitio y arranca el servidor de desarrollo
.PHONY: start
start:
	cd contenidos && myst build --execute
	mkdir -p contenidos/_build/site/public/applets
	cp -r contenidos/_static/applets/. contenidos/_build/site/public/applets/
	cd contenidos && myst start
