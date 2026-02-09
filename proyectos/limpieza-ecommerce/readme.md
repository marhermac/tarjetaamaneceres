# 🧹 Data Cleaning Challenge: E-commerce Inventory

Este proyecto demuestra un proceso completo de **limpieza, normalización y transformación de datos** sobre un dataset simulado de **5.000 registros** y **más de 100 columnas**, utilizando **Python y Pandas**.

El objetivo es transformar datos crudos e inconsistentes en un dataset confiable, listo para análisis estadístico y visualización en herramientas como **Power BI** o **Tableau**.

---

## 📌 Escenario

Una empresa de Retail recolectó información de inventario desde múltiples sucursales en **Argentina** y **Estados Unidos**.  
Debido a la carga manual, los datos presentaban errores críticos que impedían cualquier análisis confiable.

---

## 🛠️ Problemas Detectados y Resueltos

El script de limpieza aborda los siguientes problemas reales:

- **Estandarización geográfica**  
  Unificación de variantes como `arg`, `arg.`, `EE.UU`, `usa` en nombres oficiales normalizados.

- **Limpieza de precios**  
  Conversión de strings con símbolos y separadores inconsistentes (ej: `$ 1.200,50`) a valores numéricos `float`.

- **Normalización de fechas**  
  Conversión de múltiples formatos (`DD/MM/YY`, `YYYY-MM-DD`, `May 1st`) al estándar ISO.

- **Tratamiento de nulos y duplicados**  
  Imputación de valores faltantes en categorías y eliminación de duplicados tras normalizar IDs.

---

## 📊 Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** – procesamiento y limpieza de datos
- **NumPy** – manejo de valores nulos
- **Regular Expressions (Regex)** – limpieza y normalización de texto

---

## 📁 Estructura del Proyecto

- `dirty_data_challenge.csv` → dataset original con errores
- `limpieza.py` → script de limpieza y transformación
- `clean_data_final.csv` → dataset final listo para análisis
- `imagenes/` → capturas del antes y después del proceso

## 🧠 Script principal: `limpieza.py`

El archivo `limpieza.py` contiene la lógica completa del proceso de limpieza de datos, incluyendo:

- Normalización de valores geográficos mediante diccionarios de mapeo  
- Conversión de precios desde texto a valores numéricos  
- Unificación de formatos de fecha heterogéneos  
- Limpieza de identificadores y categorías  
- Eliminación de duplicados y validación final del dataset  

El script fue diseñado para ser **claro, reproducible y fácilmente adaptable** a otros datasets similares.

---

## 🚀 Cómo ejecutarlo

1. Clonar el repositorio  
   ```bash
   git clone https://github.com/marhermac/mariomaciel.git
2. Instalar dependencias
   ```bash
   pip install pandas numpy
3. Ejecutar el script
   ```bash
   python limpieza.py
 
📊 Resultado del proceso de limpieza

Dataset original (datos sucios)
<p align="center"> <img src="imagenes/dirty_data_before.png" width="650"> </p>
Dataset final (datos limpios)
<p align="center"> <img src="imagenes/clear_data_after.png" width="650"> </p>




---

