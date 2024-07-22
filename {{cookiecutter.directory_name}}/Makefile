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
	@echo Guardar documentación en documentos...
	pdoc src -o docs --force
	@echo View API documentation...
	pdoc src --http localhost:8080
