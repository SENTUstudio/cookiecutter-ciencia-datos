<p align="center">
  <a href="" rel="noopener">
 <img src="docs/assets/img/fondo.png" alt="Project logo"></a>
</p>
<h3 align="center">aurora-ai</h3>

<div align="center">

[![Hackathon](https://img.shields.io/badge/hackathon-name-orange.svg)](http://hackathon.url.com)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Pocas líneas que describen su proyecto.
    <br> 
</p>

📝 Tabla de contenido

- [Herramientas utilizadas en este proyecto](#herramientas-utilizadas-en-este-proyecto)
- [Configurar el medio ambiente](#configurar-el-medio-ambiente)
- [Instalar dependencias](#instalar-dependencias)
- [Versión de sus datos](#versión-de-sus-datos)
- [Documentación de API de generación automática](#documentación-de-api-de-generación-automática)
- [Script de Gestión de Proyecto en Python](#script-de-gestión-de-proyecto-en-python)
  - [Explicación del Script](#explicación-del-script)
  - [Uso del Script](#uso-del-script)

## Herramientas utilizadas en este proyecto
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Gestión de dependencia - [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
* [hydra](https://hydra.cc/): Administrar archivos de configuración - [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [pre-commit plugins](https://pre-commit.com/): Automatizar el formato de revisión del código
* [DVC](https://dvc.org/): Control de la versión de datos - [article](https://mathdatasimplified.com/2023/02/20/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-2/)
* [pdoc](https://github.com/pdoc3/pdoc): Cree automáticamente una documentación de API para su proyecto

## Configurar el medio ambiente
1. Instalar [Poetry](https://python-poetry.org/docs/#installation)
2. Configurar el medio ambiente:
```bash
make env 
```

## Instalar dependencias
Para instalar todas las dependencias para este proyecto, ejecute:
```bash
poetry install
```

Para instalar un nuevo paquete, ejecute:
```bash
poetry add <package-name>
```

## Versión de sus datos
Para rastrear los cambios en el directorio de "datos", escriba:
```bash
dvc add data
```

Este comando creará el archivo "data.dvc", que contiene un identificador único y la ubicación del directorio de datos en el sistema de archivos.

Para realizar un seguimiento de los datos asociados con una versión en particular, confirme el archivo "data.dvc" a Git:
```bash
git add data.dvc
git commit -m "add data"
```

Para empujar los datos al almacenamiento remoto, escriba:
```bash
dvc push
```

## Documentación de API de generación automática

Para generar un documento API de generación automática para su proyecto, ejecute:

```bash
make docs
```

Voy a convertir tu `Makefile` en un script de gestión de proyecto en Python. Este script incluirá todas las funcionalidades del `Makefile`, como la inicialización de Git, la creación y activación del entorno Conda, la instalación de dependencias, la ejecución de pruebas, la construcción y el servicio de la documentación, y el manejo de la base de datos con Docker Compose.

## Script de Gestión de Proyecto en Python

### Explicación del Script

- **`run_command(command, capture_output=False)`**: Ejecuta un comando en el shell y captura la salida si es necesario.
- **`activate_conda()`**: Activa el entorno `conda`.
- **`install_pre_commit()`**: Instala `pre-commit`.
- **`init_git()`**: Inicializa un repositorio Git.
- **`create_conda_env()`**: Crea el entorno `conda` y activa `pre-commit`.
- **`show_logo()`**: Muestra el logo del proyecto.
- **`help()`**: Muestra la ayuda con los comandos disponibles.
- **`run_tests()`**: Ejecuta pruebas con `pytest`.
- **`build_docs()`**: Construye y sirve la documentación con `MkDocs`.
- **`db_up()`**: Levanta la base de datos PostgreSQL con Docker Compose.
- **`db_down()`**: Detiene la base de datos PostgreSQL.

### Uso del Script

1. **Haz ejecutable el script** (opcional, pero recomendado en sistemas Unix):

```sh
chmod +x manage.py
```

2. **Ejecuta el script con el comando deseado**:

```sh
python manage.py init
python manage.py env
python manage.py tests
python manage.py docs
python manage.py db-up
python manage.py db-down
python manage.py help
```
