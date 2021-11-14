## Agrotopia
 Mesa, Geo-Mesa, ABM for Agriculture
 basados en python
 
## Requisitos para instalacion y utilizacion

1) En mi caso utilizo [Anaconda](https://anaconda.org/) para generar los entornos virtuales y en [Hoja de comandos](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) se encuentra informacion util para su utilizacion.

2) Crear un ambiente virtual (ventana de comandos o terminal)
```shell
conda create --name nombre_elegido
```
3) Acceder al entorno creado
```shell
conda activate -- nombre_elegido
```
# Comandos utiles (dentro del entorno virtual)
revisamos si existen las librerias a instalar
```shell
conda list
```
# Instalar Mesa y mesa-geo
```shell
conda install fiona pyproj rtree shapely
pip install mesa
pip install mesa-geo
```
# Utilizacion
Una vez instaladas las librerias, debemos acceder al entorno virtual y mediante comandos navegar hasta donde estan los ejemplos abrir los con el siguiente comando:

```shell
"Mesa/examples/example_1/mesa runserver"
```

o mediante un editor de python como Spyder o Visual Studio en el archivo run.py
