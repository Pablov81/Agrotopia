# Agrotopia - (PhD Thesis)
## About this Repository
Este repositorio fue realizada en el marco de la investigacion doctoral de Pablo Velásquez Cisterna, Methodology for the Development of Potential Scenarios for the Integrated Management of Watershed Water Resources durante los años 2019-2024. La cual fue supervisada por el Dr. Mario Lillo Saavedra

En Universwidad de concepcion, programa de 
## Abstract




## Contexto
PRueba de texto
<details>
  <summary>Title 1</summary>
  <p>Some hidden content goes here</p>
  Here is some more without a paragraph tag
</details>
<details>
  <summary>Title 2</summary>
  <p>Same stuff here</p>
</details>

## Data

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/AgroDb.png?raw=true)






## Requirements

## Package Instalation


```python
import pandas as pd
hola= pd.csv_read('Path\file', sep='')
```
## Use


## Agrotopia Flow Diagram

```mermaid
classDiagram
    class MongoDB {
    }

    class Water_Board {
        +string board_name
    }

    class Canal_Administrator{
        +string canal_name
        +float channel_actions
    }

    class Farmer_Agent {
        +Valor()
    }

    class Crop {
        +list crop_data
    }

    class Decission {
        +hola
    }


    Water_Board --> Canal_Administrator: water_actions, stock_rates
    Canal_Administrator --> Farmer_Agent: board_name, table_rates
    MongoDB --> Water_Board: water board rates
    MongoDB --> Farmer_Agent: farmer data
    MongoDB --> Crop: Crop demand rates
    Farmer_Agent --> Crop: crop_data, delivery_rates_ag
    Farmer_Agent <--> Decission:hola 🥇
    Crop --> Farmer_Agent
```
```mermaid
graph TD
    A[Aplicación] --> B
    style B fill:#f9f,stroke:#333,stroke-width:4px;
    class B className;
    classDef className style fill:#f9f,stroke:#333,stroke-width:4px,shape:cylinder;
```
## Results

