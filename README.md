# Agrotopia - (PhD Thesis)
## About this Repository
Este repositorio fue realizado en el marco de la investigacion doctoral de Pablo Velásquez Cisterna, Methodology for the Development of Potential Scenarios for the Integrated Management of Watershed Water Resources durante los años 2019-2024. La cual fue supervisada por el Dr. Mario Lillo Saavedra

En Universidad de Concepción, programa de Doctorado Recursos hidricos para la agricultura
## Abstract




## Contexto
La implementación de esta herramienta consta de dos partes principales recopilacion de la informacion de demanda diaria de los cultivos
la cuao esta en mm dia y es transformada a litros por segundos, se transforma a las a litros por segundo para ser ultilizada con lo referente a la oferta
de agua en litros por segundo. los datos restantes se obtienen de sgun lo corresponda a cada cultivo rendidmiento, valor de mercado y otros lo cual es almancenado
en la base de datos MongoDB llamada *AgroDB*
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

Area de Estudio,
![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/primera_plot.png?raw=true)

Area especifica,
![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/plot_wuos_map.png?raw=true)


## Data
La informacion utilizada en la base de datos MongoDb (AgroDB) está en la carpeta Data del proyecto, es la necesaria para las cuatro colecciones en MongoDb, Farmer_Table, Crop_Demand, Crop_Table y Offer_Table.

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/AgroDb.png?raw=true)






## Requirements

## Package Instalation


```python
import pandas as pd
hola= pd.csv_read('Path\file', sep='')
```
## Use


## Agrotopia Diagram

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

    Water_Board --> Canal_Administrator: wb_rates
    Canal_Administrator --> Farmer_Agent: wb_rates
    MongoDB --> Water_Board: wb_rates
    MongoDB --> Farmer_Agent: farmer_data
    MongoDB --> Crop: crop_rates
    Farmer_Agent --> Crop: farmer_rates
    Farmer_Agent --> Decission
    Info_Mix-->Farmer_Agent
    Economic_changes-->Farmer_Agent
    Infraestructure-->Canal_Administrator
    Crop --> Farmer_Agent:rx_crop()
```



## Results
La informacion utilizada en la base de datos MongoDb (AgroDB) está en la carpeta Data del proyecto, es la necesaria para las cuatro colecciones en MongoDb, Farmer_Table, Crop_Demand, Crop_Table y Offer_Table.

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/yearly_density_map.png?raw=true)


La informacion utilizada en la base de datos MongoDb (AgroDB) está en la carpeta Data del proyecto, es la necesaria para las cuatro colecciones en MongoDb, Farmer_Table, Crop_Demand, Crop_Table y Offer_Table.

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/influence_nodes.png?raw=true)




