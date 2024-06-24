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
        Farmer_Table
        Crop_Demand
        Crop_Table
        Offer_Table
    }

    class Water_Board {
        elegir_semana_y_abrir_embalse()
        organizar_tasas_por_semana()
        mostrar_cantidad_embalse()
    }

    class Canal_Administrator{
        obtener_tasas_reparto_ordenadas()
        generar_calendario_riego()
        calcular_reparto_Ag()
    }

    class Farmer_Agent {
        show_Agricultor_data()
        fusionar_datos()
        Ag_tasas_ordenadas()
        recibe_crop()
        organizar_info_crop()
        insumo_Ag()
        preparar_rx_Ag()
        organizar_datos()
        calcular_rx_Ag()
        organiza_accion_Ag()
        influencia_entorno()
    }

    class Crop {
        ordenar_Ag()
        ordenar_crop()
        calcular_crop()
        rx_crop()
    }

    class Decission {
        calcular_percepcion()
        decision_ag()
    }

    class Info_Mix {
        obtener_informacion()
    }

    class Infraestructure {
        canal_coat
        irrigation_tech
        reservoir
    }

    class Economic_changes {
        variacion_economica()
    }

    Water_Board --> Canal_Administrator: water_actions, stock_rates
    Canal_Administrator --> Farmer_Agent: board_name, table_rates
    MongoDB --> Water_Board: water board rates
    MongoDB --> Farmer_Agent: farmer data
    MongoDB --> Crop: Crop demand rates
    Farmer_Agent --> Crop: delivery_rates_ag
    Farmer_Agent --> Decission:hola 🥇
    Info_Mix-->Farmer_Agent
    Economic_changes-->Farmer_Agent
    Infraestructure-->Canal_Administrator
    Crop --> Farmer_Agent:rx_crop()
```



## Results

