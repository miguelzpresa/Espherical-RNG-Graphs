RNGs
==============================
![image](https://github.com/miguelzpresa/Espherical-RNG-Graphs/assets/49998408/3130c8c2-712e-498b-9f96-37f920dd856d)

Numerical & Statistical Analysis about RNGs(Relative Neighbor Graphs) living on a spherical surface


____
## Table of Contents

* [Project Overview---Poster](https://github.com/miguelzpresa/Espherical-RNG-Graphs/files/15343433/Poster_RNG-11.pdf)
* [Thesis](#protocolo2024.pdf)

* [Libreries](#Libreries)
* [Packages](#Packages)


[Poster_RNG-11.pdf](https://github.com/miguelzpresa/Espherical-RNG-Graphs/files/15343433/Poster_RNG-11.pdf)





![Poster_RNG-11](https://github.com/miguelzpresa/Espherical-RNG-Graphs/assets/49998408/c8fba599-ac7f-4456-8eeb-5f4cc8290d7b)










# Introduction
This project aims to understand, explore, and characterize the different numerical, geometric, and algebraic properties and relationships that exist when computationally constructing a family of RNG graphs on the surface of a sphere.





___

# Packages<br>
* [Pandas    version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy      version 1.21.5](https://numpy.org/)  
* [Numba_____version_0.58.1](https://numba.org)
* [Scipy_____version_1.11.4](https://scipy.org)
* itertools
* time
* copy
* Jupyter lab     3.2.9
___
# Results
![image](https://github.com/miguelzpresa/Espherical-RNG-Graphs/assets/49998408/fe0e1289-71e0-42aa-a97b-c2330dc66783)

![image](https://github.com/miguelzpresa/Espherical-RNG-Graphs/assets/49998408/8c1ad89e-eb9a-4c87-8840-55b57ea416a0)

![image](https://github.com/miguelzpresa/Espherical-RNG-Graphs/assets/49998408/4a34926e-6796-4b52-96bb-b328a65ed46a)



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

### Example(json format)  
{  
"grafo": {  
"id": 1,  
"lista_nodos": [1, 2, 3, 4, 5],  
"lista_aristas": [1, 2, 3, 4],  
"estadisticas": {  
"num_nodos": 5,  
"num_aristas": 4,  
"grado_maximo": 2,  
"grado_minimo": 1,  
"grado_promedio": 1.6,  
"densidad": 0.4  
}  
},  
"nodos": [  
{   
"id": 1,  
"coordenada_x": 0.0,  
"coordenada_y": 1.0  
},  
{  
"id": 2,  
"coordenada_x": 1.0,  
"coordenada_y": 0.0  
},  
{  
"id": 3,  
"coordenada_x": -1.0,  
"coordenada_y": 0.0  
},  
{  
"id": 4,  
"coordenada_x": 0.0,  
"coordenada_y": -1.0  
},  
{  
"id": 5,  
"coordenada_x": 0.5,  
"coordenada_y": 0.5  
}  
],  
"aristas": [  
{  
"id": 1,  
"nodo_inicial": 1,  
"nodo_final": 2,  
"distancia": 1.41421356,  
"angulo_1": null,  
"angulo_2": null  
},  
{  
"id": 2,  
"nodo_inicial": 1,  
"nodo_final": 3,  
"distancia": 1.41421356,  
"angulo_1": null,  
"angulo_2": null  
},  
{  
"id": 3,  
"nodo_inicial": 1,  
"nodo_final": 5,  
"distancia": 1.11803399,  
"angulo_1": null,  
"angulo_2": null  
},  
{  
"id": 4,  
"nodo_inicial": 2,  
"nodo_final": 3,  
"distancia": 2.0,  
"angulo_1": null,  
"angulo_2": null  
}  
]  
}  






