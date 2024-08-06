# Control de proyecto de Datos

.DEFAULT_GOAL := help
PROJECT_DIR := $(CURDIR)
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

## Inicializa Git y instala dependencias con Anaconda
ini: logo
	@echo "Inicializando Git..."
	git init
	git branch -m main
	@echo "Instalación de dependencias..."
	conda env create --prefix ./env --file environment.yml
	conda activate "$(PROJECT_DIR)/env"
	pre-commit install

## Activa el entorno virtual con Anaconda
env: logo
	@echo "Activando el entorno virtual..."
	conda activate ./env

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

## Levanta la base de dato postgres con docker compose
db-up: logo
	@echo "Levanta la base de dato postgres con docker compose"
	docker compose up -d

## Detiene la base de datos postgres
db-down: logo
	@echo "Detiene la base de datos"
	docker compose down