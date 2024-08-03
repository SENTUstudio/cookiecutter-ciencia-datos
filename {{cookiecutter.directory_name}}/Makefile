# Control de proyecto de Datos

.DEFAULT_GOAL := help

# Colores y formato
boldon := $(shell tput bold)
reset := $(shell tput sgr0)
yellowf := $(shell tput setaf 3)
bluef := $(shell tput setaf 4)

# Logo del proyecto
logo:
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

## Instalación de dependencias
dependencies: ## Inicializa Git y instala dependencias con Poetry
	@echo "Inicializando Git..."
	@git init
	@echo "Instalación de dependencias..."
	@poetry install --no-root
	@poetry run pre-commit install

## Activar el entorno virtual
env: dependencies ## Activa el entorno virtual con Poetry
	@echo "Activando el entorno virtual..."
	@poetry shell

## Ejecuta rutina de pruebas
tests: ## Ejecuta pruebas con pytest
	@echo "Ejecutando pruebas..."
	@poetry run pytest

## Construye y levanta la documentación en Mkdocs
docs: ## Construye y sirve la documentación con MkDocs
	@echo "Construyendo cache de la documentación..."
	@mkdocs build
	@echo "Sirviendo la documentación..."
	@mkdocs serve
