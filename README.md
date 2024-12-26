# 🌱 **Metodología para el Desarrollo de Escenarios Potenciales para la Gestión Integrada de Recursos Hídricos de Cuencas**

### 📄 **Sobre este Repositorio**
Este repositorio fue creado como parte de la investigación doctoral de **Pablo Velásquez Cisterna**, titulada **"Metodología para el Desarrollo de Escenarios Potenciales para la Gestión Integrada de Recursos Hídricos de Cuencas"**, llevada a cabo entre los años 2019 y 2024. La investigación fue supervisada por el **Dr. Mario Lillo Saavedra** en la **Universidad de Concepción**, dentro del **Programa de Doctorado en Recursos Hídricos y Energía para la Agricultura**.

---

### 📚 **Resumen de la Investigación**

La investigación desarrolla una metodología para identificar y gestionar conflictos en la gestión de recursos hídricos a escala de cuenca, con un enfoque particular en la **cuenca del río Longaví**, en la región del Maule, Chile. Esta área enfrenta importantes desafíos debido a la fragmentación de la tierra y la variabilidad hídrica, agravados por el cambio climático.  

Para abordar estos problemas, el estudio integra la **Socio-Hidrología** con **Modelos Basados en Agentes (ABM)** (SHABM), permitiendo un análisis detallado de las interacciones entre los usuarios del agua bajo distintos escenarios ambientales y normativos.  

#### **Marco Tecnológico**
La herramienta de simulación desarrollada utiliza:
- **Python** y **MongoDB** como tecnologías principales.
- **Datos clave** como:
  - Uso del suelo.
  - Demanda hídrica específica para cada cultivo.
  - Factores económicos, incluyendo análisis del valor de mercado y resiliencia de los cultivos ante la sequía.
  - Informes sociales sobre preferencias de cultivos basados en la disponibilidad hídrica.
- Integración de información geoespacial para modelar la dinámica de las parcelas dentro de la cuenca.

Los datos recolectados mediante entrevistas, observaciones y encuestas alimentan los modelos, permitiendo analizar patrones de comportamiento de usuarios del agua aleatoriamente clasificados como:
- **Egoístas** (priorizan su beneficio individual).
- **Neutrales** (toman decisiones balanceadas).
- **Colaboradores** (actúan en pro del bien común).

---

### 📈 **Resultados y Publicaciones**

#### **Resultados Clave de la Investigación**
- **Patrones de Decisión:** Los resultados revelan diferencias significativas en las decisiones de los agentes. Los agentes egoístas tienden a ignorar las reglas bajo condiciones de baja supervisión, mientras que los agentes colaboradores respetan las reglas consistentemente, incluso bajo estrés hídrico.
- **Gestión Adaptativa:** La implementación de niveles de supervisión altos (90%) reduce considerablemente los conflictos, identificando áreas críticas que requieren atención prioritaria.
- **Identificación de Conflictos:** Los análisis permiten identificar zonas de alto riesgo de conflicto en escenarios de baja disponibilidad hídrica.

#### **Publicaciones Científicas**
1. **Artículo 1:**  
   - **Título:** *Socio-Hydrological Agent-Based Modeling as a Framework for Analyzing Conflicts Within Water User Organizations*  
   - **DOI:** [https://doi.org/10.3390/w16223321](https://doi.org/10.3390/w16223321)  
   - **Resumen:** Este artículo describe el desarrollo de un modelo socio-hidrológico basado en agentes (SHABM) aplicado a la cuenca del río Longaví, evaluando cómo la supervisión y disponibilidad de agua afectan los patrones de comportamiento y los conflictos en sistemas agrícolas.  

2. **Artículo 2:**  
   - **Título:** *Dataset for Reproducible Interaction in a Socio-Hydrological Model with ABM*  
   - **DOI:** Publicación en progreso, enlace pendiente.  
   - **Resumen:** Este trabajo introduce un conjunto de datos estructurados y documentados para analizar interacciones socio-hidrológicas reproducibles, evaluando estrategias de manejo hídrico y su impacto en el comportamiento de los usuarios.


### 📊 **Componentes Clave del Modelo**
#### **1. Datos en MongoDB (AgroDB)**
Estructura:
- **Farmer_Table:** Información básica de agricultores.  
- **Crop_Demand:** Demanda hídrica por cultivo.  
- **Crop_Table:** Detalles técnicos y económicos de cultivos.  
- **Offer_Table:** Disponibilidad semanal de agua.  

#### **2. Integración Geoespacial**
Se utiliza información geográfica (shapefiles) para modelar turnos de riego y la distribución de parcelas.

---



### **🌍 Área de Estudio**  

#### **Área General cambiar el mapa**  
![Cuenca del Río Longaví](https://github.com/Pablov81/Agrotopia/blob/main/images/primera_plot.png?raw=true)  

#### **Área Específica**  
![Mapa de WUOs](https://github.com/Pablov81/Agrotopia/blob/main/images/plot_wuos_map.png?raw=true)  

---

### **📊 Datos**  
La información almacenada en la base de datos **MongoDB (AgroDB)** se encuentra en la carpeta `Data` del proyecto. Incluye las siguientes colecciones:  

- **Farmer_Table:** Información de los agricultores.  
- **Crop_Demand:** Demanda de agua de los cultivos.  
- **Crop_Table:** Detalles de los cultivos.  
- **Offer_Table:** Oferta de agua disponible.  

![Estructura de AgroDB](https://github.com/Pablov81/Agrotopia/blob/main/images/AgroDb.png?raw=true)  

---


---

### **📦 Requisitos**  
- **Python 3.x**  
- **MongoDB**  
- **Conda**  

---

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


# 🚀 **Ejecución del Programa**

### ✍️ **Notas del Autor**
El proyecto tiene dos versiones:
  - Español (SP)
  - Inglés (ENG).

crear el ambiente donde dejar el programa
   ```bash
   conda create --name agrotopia_env python=3.9
   conda activate agrotopia_env

```


```python
   streamlit run interfaz.py
```
Se ejecutra el servidor web local con las opciones para generar los dataset







## **📁 Tratamiento de Archivos CSV**  

🔄 **Procesamiento de datos**  
El proyecto utiliza archivos CSV para almacenar y procesar información como demanda hídrica, datos económicos y detalles de cultivos.  

### Ejemplo: Filtrado de datos  
```python
import pandas as pd

# Leer archivo CSV
data = pd.read_csv("data/cultivos.csv")

# Filtrar por año y cultivo
filtro = data[(data["Año"] == 2020) & (data["Cultivo"] == "Maíz")]

# Guardar resultados filtrados
filtro.to_csv("output/filtered_data.csv", index=False)

print("Filtrado completado. Archivo guardado en 'output/filtered_data.csv'")

## Results
La informacion utilizada en la base de datos MongoDb (AgroDB) está en la carpeta Data del proyecto, es la necesaria para las cuatro colecciones en MongoDb, Farmer_Table, Crop_Demand, Crop_Table y Offer_Table.

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/yearly_density_map.png?raw=true)


La informacion utilizada en la base de datos MongoDb (AgroDB) está en la carpeta Data del proyecto, es la necesaria para las cuatro colecciones en MongoDb, Farmer_Table, Crop_Demand, Crop_Table y Offer_Table.

![alt text](https://github.com/Pablov81/Agrotopia/blob/main/images/influence_nodes.png?raw=true)

```
### 📊 **Visualizacións**
Los gráficos generados muestran tendencias claras:  
- 📈 Incrementos en la eficiencia hídrica.
- 🔍 Análisis detallados de los conflictos entre agentes.