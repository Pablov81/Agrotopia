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


### Flow Diagram

```mermaid
classDiagram
    class MongoDB {
    }

    class Water_Board {
        +string board_name
        +float water_actions
        +float max_reservoir
        +float reservoir_min
        +float table_rates
        +choose_week()
        +and_open_reservoir()
        +organise_rates_per_week()
        +show_amount_of_reservoir()
    }

    class Infrastructure {
        +canal_rev
        +irrigation_tech
        +reservoir
    }

    class Canal_Manager {
        +string canal_name
        +float channel_actions
        +string farmer_data
        +float stock_rates
        +float efficiency
        +get_ordered()
        +apportionment_rates()
        +calculate_split_Ag()
    }

    class Farmer_Agent {
        +string canal_name
        +list farmer_data
        +list farmer_rates
        +dict get_crop
        +show_data()
        +merge_data()
        +Ag_sort_rates()
        +receive_crop()
        +organize_info_crop()
        +input_Ag()
        +prepare_rx_Ag()
        +calculate_rx_Ag()
        +jump_counter_Ag()
    }

    class Decision {
        +Calculate_perception()
        +Farmer_decision()
    }

    class Crop {
        +list crop_data
        +list delivery_rates_ag
        +sort_Ag()
        +sort_crop()
        +calculate_crop()
        +rx_crop()
    }

    class Info_Mix {
        +Personality_list()
        +Priority_crop()
        +Efficiency()
        +Yield_crop()
        +Cost_Production()
        +Market_Value()
        ...
    }

    class Economic_Changes {
        +annual_dollar_value
        +annual_crop_yield_changes
        +consumer_price_index
    }

    MongoDB <--> Water_Board: water board rates
    MongoDB <--> Farmer_Agent: farmer data
    MongoDB <--> Info_Mix: Crop demand rates
    MongoDB <--> Economic_Changes
    Water_Board --> Canal_Manager: water_actions, stock_rates
    Water_Board --> Farmer_Agent: board_name, table_rates
    Water_Board --> Infrastructure: irrigation tech, canal rev, reservoir
    Canal_Manager --> Farmer_Agent: canal_name, farmer_data, efficiency
    Info_Mix --> Farmer_Agent: merge_data, input_Ag
    Farmer_Agent --> Crop: crop_data, delivery_rates_ag
    Economic_Changes --> Info_Mix: annual_dollar_value, market value
    Decision --> Farmer_Agent: Calculate_perception, Farmer_decision

```
### Results
