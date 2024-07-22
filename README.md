<p align="center">
  <a href="" rel="noopener">
 <img src="docs/assets/img/fondo.png" alt="Project logo"></a>
</p>
<h3 align="center">Project Title</h3>

<div align="center">

[![Hackathon](https://img.shields.io/badge/hackathon-name-orange.svg)](http://hackathon.url.com)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [Proyectos para SENTU.studio](#proyectos-para-sentustudio)
- [Estudiando el proyecto de @datasciencesimplifed](#estudiando-el-proyecto-de-datasciencesimplifed)
  - [Herramientas usadas en el proyecto](#herramientas-usadas-en-el-proyecto)
  - [Estructura del Proyecto](#estructura-del-proyecto)


Proyectos para SENTU.studio
===========================
----------------------------------------

La mejor forma de estructurar un proyecto de ciencia de datos para que sea manejable, mantenible y escalable

1. cookiecutter data science

- [ ] Revisar el proyecto de @datasciencesimplifed https://www.youtube.com/watch?v=TzvcPi3nsdw
- [ ] Proyecto de drivendata.org tiene buena estructura y un paquete final. Es bueno tomarlo como referencia https://cookiecutter-data-science.drivendata.org/

Estudiando el proyecto de @datasciencesimplifed
===============================================
----------------------------------------------------------------------


## Herramientas usadas en el proyecto
* Poetry: administrador de dependencia
* Hydra: administrador de configuración de archivos
* pre-commit plugins: Automatizar el formato de revisión de código
* DVC: Contro de versión de datos
* pdoc: Cree automáticamente una documentación API para su proyecto

## Estructura del Proyecto

```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   ├── raw                         # raw data
│   └── raw.dvc                     # DVC file of data/raw
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   └── train_model.py              # train model
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```

