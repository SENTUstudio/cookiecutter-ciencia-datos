# Control de proyecto de Datos

.DEFAULT_GOAL := help

# Colores y formato
boldon := $(shell tput bold)
reset := $(shell tput sgr0)
yellowf := $(shell tput setaf 3)
bluef := $(shell tput setaf 4)

# Logo del proyecto
logo:
	clear
	@printf "\n"
	@printf " ${boldon}${yellowf}█▀ █▀▀ █▄░█ ▀█▀ █░█${reset}  ┎┤ Ciencia de Datos          ├┒\n"
	@printf " ${boldon}${yellowf}▄█ ██▄ █░▀█ ░█░ █▄█${reset}  ┖┤ con ${boldon}Python${reset} en ${boldon}${reset} Archlinux ├┚\n"
	@printf "             .studio\n"

## Muestra la ayuda en pantalla
help: logo
	@echo -e "\n\033[1mComandos disponibles:\033[0m"
	@awk '/^##.*$$/,/^[~\/\.0-9a-zA-Z_-]+:/' $(MAKEFILE_LIST) | \
	awk '!(NR%2){print $$0p}{p=$$0}' | \
	awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | \
	sort

## Inicializa Git y instala dependencias con Poetry
dependencies: logo
	@echo "Inicializando Git..."
	git init
	@echo "Instalación de dependencias..."
	conda env create -f environment.yml
	conda activate {{ cookiecutter.directory_name }}
	pre-commit install

## Activa el entorno virtual con Poetry
env: logo dependencies
	@echo "Activando el entorno virtual..."

## Ejecuta pruebas con pytest
tests: logo
	@echo "Ejecutando pruebas..."
	pytest

## Construye y sirve la documentación con MkDocs
docs: logo
	@echo "Construyendo cache de la documentación..."
	mkdocs build
	@echo "Sirviendo la documentación..."
	mkdocs serve
