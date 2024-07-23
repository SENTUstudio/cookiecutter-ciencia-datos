.PHONY: tests docs

dependencies:
	@echo "Inicializando Git..."
	git init
	@echo "Instalación de dependencias..."
	poetry install --no-root
	poetry run pre-commit install

env: dependencies
	@echo "Activar el entorno virtual..."
	poetry shell

tests:
	pytest

docs:
	@echo Construyendo cache...
	mkdocs build
	@echo Ver API documentación...
	mkdocs serve
