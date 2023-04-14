RNGs
==============================

Numerical & Statistical Analysis about RNGs(Relative Neighbor Graphs) living on a spherical surface
"Final Project",UNAM (https://www.unam.mx/) -TICs-Statistics 2023-1 class,taught by Dr. María del Río Franco 


____
## Table of Contents

* [License](#License)
* [Project Overview](#Project_Overview)
* [Introduction](#Introduction)
* [Justification](#Justification)
* [Goals](#Goals)
* [Hypothesis](#Hypothesis)
* [Metodology](#Metodology)
* [Libreries](#Libreries)
* [Packages](#Packages)
* [Results](#Results)
* [Conclusions](#Conclusions)
* [References](#References)


____
# License
Copyright © 2023 <mikezpresa@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

____
# Project_Overview
This project aims to develop numerical & statistical insights about the hidden geometric properties that exists in the presence of graphs generated on the surface of a sphere. 



# Introduction
This project aims to understand, explore, and characterize the different numerical, geometric, and algebraic properties and relationships that exist when computationally constructing a family of RNG graphs on the surface of a sphere. As the first step in a series of reports, we analyzed the data from the results obtained by Dr. Daniele Colosi, who designed and generated a series of computational experiments where $10^5$ RNG graphs were generated. The results are presented in the paper titled "Relative Neighbourhood Graphs on the sphere", which provides the record of the relative frequencies representing the probability that the length of an edge generated in an RNG graph falls within a range of values (it is a range and not specific values because it is working in the continuous and in continuous probability, intervals are used). These distances are then grouped into specific intervals within a range of 0 to pi, divided into 400 equal-sized intervals. The results indicated a non-uniform distribution of edges along the sphere and a relationship between the geodesic distance and the relative frequency of edge occurrence. In general, this study (report) presents the results obtained from the descriptive statistical analysis conducted on the geometric structure of the graphs on the surface of a sphere when they are randomly generated with a uniform distribution of points along with a criterion that we will explain later, which determines whether there is a connection link between two nodes.


______
# Justification



# Constraints

#  Goals



____
# Hipothesis
*
*
*
*

______
# Dataset Specifications
### Overview
This dataset contains information about different graphs. For each graph, its unique identifier, list of nodes and list of edges, as well as descriptive statistics and details about each node and edge, are recorded.

### Data Sources
The data was obtained through a graph generation simulation.

### Dataset Size
The dataset contains information on 1000 different graphs.  

### Dataset Atributes
grafo.id: Identificador único del grafo (int).
grafo.lista_nodos: Lista de identificadores únicos de los nodos que conforman el grafo (list).
grafo.lista_aristas: Lista de identificadores únicos de las aristas que conforman el grafo (list).
grafo.estadisticas.num_nodos: Número de nodos que conforman el grafo (int).
grafo.estadisticas.num_aristas: Número de aristas que conforman el grafo (int).
grafo.estadisticas.grado_maximo: Grado máximo de los nodos del grafo (int).
grafo.estadisticas.grado_minimo: Grado mínimo de los nodos del grafo (int).
grafo.estadisticas.grado_promedio: Grado promedio de los nodos del grafo (float).
grafo.estadisticas.densidad: Densidad del grafo (float).
nodos.id: Identificador único del nodo (int).
nodos.coordenada_x: Coordenada en el eje X del nodo (float).
nodos.coordenada_y: Coordenada en el eje Y del nodo (float).
aristas.id: Identificador único de la arista (int).
aristas.nodo_inicial: Identificador único del nodo inicial de la arista (int).
aristas.nodo_final: Identificador único del nodo final de la arista (int).
aristas.distancia: Distancia entre los nodos inicial y final de la arista (float).
aristas.angulo_1: Ángulo de la arista respecto al eje X (float o null).
aristas.angulo_2: Ángulo de la arista respecto al eje Y (float o null).


### Tipo de datos
grafo.id: int
grafo.lista_nodos: list
grafo.lista_aristas: list
grafo.estadisticas.num_nodos: int
grafo.estadisticas.num_aristas: int
grafo.estadisticas.grado_maximo: int
grafo.estadisticas.grado_minimo: int
grafo.estadisticas.grado_promedio: float
grafo.estadisticas.densidad: float
nodos.id: int
nodos.coordenada_x: float
nodos.coordenada_y: float
aristas.id: int
aristas.nodo_inicial: int
aristas.nodo_final: int
aristas.distancia: float
aristas.angulo_1: float o null
aristas.angulo_2: float o null  
### NUll values
Los valores faltantes en el dataset se indicarán con el valor NaN para las columnas numéricas





---
# Methodology









___

# Packages<br>
* [Pandas    version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy      version 1.21.5](https://numpy.org/)  
* 
* Jupyter lab     3.2.9
___
# Results


____
# Conclusions



___
# References


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

