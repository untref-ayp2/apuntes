## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## install: install all required dependencies
.PHONY: install
install:
	pip install --requirement requirements.txt

## fmt: format Python and Jupyter files
.PHONY: fmt
fmt:
	find ./contenidos -name "*.ipynb" -not -path "*.ipynb_checkpoints*" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace {} ';'

## build: build the book
.PHONY: build
build:
	jupyter-book build .

## clean: clean the book
.PHONY: clean
clean:
	jupyter-book clean .

## Puerto por defecto para levantar el servidor http
PORT ?= 8080

## server: start a HTTP server to read the book
.PHONY: server
server: build
	python -m http.server $(PORT)  --directory _build/html
