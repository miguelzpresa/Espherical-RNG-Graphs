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

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20patterns%202.jpg 'Fingerprints')

Freepik Company. (2010-2022). Detailed fingerprint icons. Retrieved from [Link page](https://www.freepik.es/vector-premium/iconos-detallados-huellas-dactilares-escaner-policia-pulgar-simbolos-vectoriales-identidad-persona-seguridad-id-pictogramos-dedo-identidad-tecnologia-biometric_4866225.htm)


# Introduction
Fingerprints Growth formation pattern is dictated by highly complex interactions of multiple initial conditions, listed  below. The main goal is to generate fongerprints based of the paper " fingerprint formation model published in the scientific journal EUROPHYSICS LETTERS, "DOI: 10.1209/epl/i2004-10161-2""
 
## What are fingerprints?
Fingerprints are skin patterns with friction ridges. Our fingers, palms and soles are characterized by ridges (hills) and valleys (furrows). Their formation occurs during fetal development, beginning at approximately the 10th week of gestation, being completed by the 17th week, and remaining throughout life.

## What are the patterns of fingerprints? 
There are three basic patterns of fingerprints: 
* Whorls (a): Most complex, and contain central pocket, double loop, and accidental 
* Loops (b): Radial or  ulnar, depending on whether direction of slope of pattern is towards inner arm bone (radius) or outer arm bone (ulna) 
* Arches (c): Can be plain or tented

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20pattern.jpg 'Types of patterns')

M. Kücken, A.C. Newell / Journal of Theoretical Biology 235 (2005) 71–83. Retrieved from page 80 Fig.11. [Link to the article](https://www.math.arizona.edu/~anewell/publications/Fingerprint_Formation.pdf)
______
# Justification

The biggest inspiration for this project comes from the work of Alan Turing's Patterns in Nature. Zebra stripes, cat coats, leopards and cheetahs are surprisingly unique, making stripes a tool to identify one animal from the rest, fingerprints are like our stripes.   


Turing’s theory was elegant and simple: any repeating natural pattern could be created by the interaction of two things — molecules, cells, whatever — with particular characteristics. Through a mathematical principle he called ‘reaction–diffusion’, these two components would spontaneously self-organise into spots, stripes, rings, swirls or dappled blobs.
"https://ideas.ted.com/how-the-zebra-got-its-stripes-with-alan-turing/"

# Constraints
Physics and mathematical theory of embryology deals with highly complex dynamics systems ,some of them non-linear,its important to mention that we do not pretend to model the actual physical process of ridges formation(fingerprints),However ,the paper that we are analyzing gives an alternative approach,it takes the principal properties ,that we will list below ,to replicate the fingerprint formation during embryological process through ,multivariable calculus tools ,vectors spaces,and numerical methods.

#  Goals
* Get a better understanding of embryological process of epidermial ridge formation
* Understand the problem domain 
* Implement the 3 Principal Patterns :Whorls,Loops.Archs
* Analize the different dynamics output from different initial conditions
* Simulate the closest thing to a fingerprint 


____
# Hipothesis
*
*
*
*

______
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

