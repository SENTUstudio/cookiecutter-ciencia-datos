<p align="center">
  <a href="" rel="noopener">
 <img src="docs/assets/img/repository-open-graph-template.png" alt="Project logo"></a>
</p>
<h3 align="center">Cookie Cutter para Ciencia de Datos e Ingeniería de Datos</h3>

<div align="center">

[![Hackathon](https://img.shields.io/badge/cookie_cutter_ciencia_datos-web-orange.svg)](https://sentustudio.github.io/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/SENTUstudio/cookiecutter-ciencia-datos.svg)](https://github.com/SENTUstudio/cookiecutter-ciencia-datos/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/SENTUstudio/cookiecutter-ciencia-datos.svg)](https://github.com/SENTUstudio/cookiecutter-ciencia-datos/pulls)
[![License](https://img.shields.io/github/license/SENTUstudio/cookiecutter-ciencia-datos.svg)](LICENSE.md)

</div>

📝 Tabla de contenido

- [¿Por qué?](#por-qué)
- [Herramientas usadas en el proyecto](#herramientas-usadas-en-el-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo usar este proyecto](#cómo-usar-este-proyecto)

## ¿Por qué?

Es importante estructurar su proyecto de ciencia de datos en función de un cierto estándar para que sus compañeros de equipo puedan mantener y modificar fácilmente su proyecto.

Este repositorio proporciona una plantilla que incorpora las mejores prácticas para crear un proyecto de ciencia de datos mantenible y reproducible.


## Herramientas usadas en el proyecto
* [Poetry](https://python-poetry.org/): administrador de dependencia
* [Hydra](https://hydra.cc/): administrador de configuración de archivos
* [pre-commit plugins](https://pre-commit.com/): Automatizar el formato de revisión de código
* [DVC](https://dvc.org/): Contro de versión de datos
* [mkdocs-material](https://squidfunk.github.io/mkdocs-material/): Cree automáticamente una documentación API para su proyecto

## Estructura del Proyecto

```bash
.
├── config                    # Configuración del proyecto
│   ├── main.yaml             # Archivo principal de configuración
│   ├── model                 # Configuraciones de los modelos
│   │   ├── model1.yaml       # Configuración del modelo 1
│   │   └── model2.yaml       # Configuración del modelo 2
│   └── process               # Configuraciones de los procesos
│       ├── process1.yaml     # Configuración del proceso 1
│       └── process2.yaml     # Configuración del proceso 2
├── data                      # Datos del proyecto
│   ├── external              # Datos externos
│   ├── final                 # Datos finales listos para análisis
│   ├── processed             # Datos procesados
│   ├── raw                   # Datos crudos sin procesar
│   └── raw.dvc               # Archivo DVC para gestionar datos crudos
├── docs                      # Documentación del proyecto
│   ├── assets                # Recursos de la documentación
│   │   └── img               # Imágenes para la documentación
│   └── index.md              # Índice de la documentación
├── Makefile                  # Script de automatización de tareas
├── mkdocs.yml                # Configuración de MkDocs para la documentación
├── models                    # Modelos entrenados
├── notebooks                 # Notebooks de Jupyter para análisis y desarrollo
├── pyproject.toml            # Configuración del proyecto en formato TOML
├── README.md                 # Archivo README con la descripción del proyecto
├── references                # Referencias y recursos adicionales
├── reports                   # Reportes generados del análisis
│   └── figures               # Figuras y gráficos de los reportes
├── src                       # Código fuente del proyecto
│   ├── __init__.py           # Inicialización del paquete src
│   ├── process.py            # Script para procesamiento de datos
│   └── train_model.py        # Script para entrenar modelos
└── tests                     # Pruebas del código fuente
    ├── __init__.py           # Inicialización del paquete tests
    ├── test_process.py       # Pruebas para el script de procesamiento
    └── test_train_model.py   # Pruebas para el script de entrenamiento de modelos

```

## Cómo usar este proyecto

Instalar Cookiecutter:

```shell
pip install cookiecutter
```

Crear un proyecto basado en la plantilla:

```shell
cookiecutter https://github.com/SENTUstudio/cookiecutter-ciencia-datos --checkout main
```
