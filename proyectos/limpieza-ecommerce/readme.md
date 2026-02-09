
markdown
# 🧹 Data Cleaning Challenge: E-commerce Inventory

Este proyecto demuestra la limpieza, normalización y transformación de un dataset de **5,000 registros** con **100 columnas** (simulado) utilizando Python y la librería Pandas. 

## 📌 Escenario
Una empresa de Retail recolectó datos de sucursales en Argentina y USA. Los datos llegaron con errores críticos de carga manual que impedían cualquier análisis estadístico o visualización en Power BI/Tableau.

## 🛠️ Problemas Detectados y Resueltos
En este repositorio encontrarás el script de limpieza que soluciona:

- **Estandarización Geográfica:** Uso de diccionarios de mapeo para unificar variantes como `arg`, `Arg.`, `EE.UU`, `usa` en nombres oficiales.
- **Limpieza de Precios (Regex):** Transformación de strings con formatos de moneda inconsistentes (ej: `$ 1.200,50`) a formato `float` numérico.
- **Normalización de Fechas:** Conversión de múltiples formatos (`DD/MM/YY`, `YYYY-MM-DD`, etc.) al estándar ISO.
- **Tratamiento de Nulos y Duplicados:** Imputación inteligente de datos faltantes en categorías y eliminación de duplicados basados en IDs normalizados.

## 📊 Tecnologías Utilizadas
- **Python 3.x**
- **Pandas** (Procesamiento de datos)
- **NumPy** (Manejo de valores nulos)
- **Regular Expressions (Re)** (Extracción de patrones de texto)

## 📁 Estructura del Proyecto
- `dirty_data_challenge.csv`: El dataset original con errores.
- `data_cleaning_script.ipynb`: Notebook con el paso a paso detallado y comentado.
- `clean_data_final.xlsx`: El resultado final listo para el cliente.

## 🚀 Cómo ejecutarlo
1. Clona el repositorio: `git clone https://github.com`
2. Instala las dependencias: `pip install pandas openpyxl`
3. Ejecuta el notebook o el script `.py`.

## 📊 Resultado del proceso de limpieza

<p align="center">
  <img src="https://github.com/marhermac/mariomaciel/blob/main/proyectos/limpieza-ecommerce/imagenes/dirty_data_before.png" width="600">
</p>



[Vista previa del dataset Sucio](imagenes/dirty_data_before.png)

<p align="center">
  <img src="https://github.com/marhermac/mariomaciel/blob/main/proyectos/limpieza-ecommerce/imagenes/clear_data_after.png" width="600">
</p>



[Vista previa del dataset limpio](imagenes/clear_data_after.png)






---

