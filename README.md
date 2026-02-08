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

---
<<<<<<< HEAD

## 🌍 ¿Cuál es el problema?

En Argentina y Latinoamérica, muchas personas se enfrentan a:

- Altos niveles de obesidad y enfermedades metabólicas
- Información nutricional fragmentada, técnica o difícil de interpretar
- Herramientas privadas con intereses comerciales o barreras de acceso

Actualmente no existen herramientas públicas, simples y gratuitas que permitan
comparar alimentos cotidianos según su impacto glucémico de forma comprensible.

---

## 🎯 ¿Qué propone RIGA?

RIGA propone un **ranking visual de alimentos** basado en:

- Cantidad de carbohidratos por porción
- Índice glucémico (cuando la información está disponible)
- Tamaños de porción estandarizados

El resultado se presenta mediante un sistema tipo semáforo:

- 🟢 **Verde**: mejor opción
- 🟡 **Amarillo**: consumo moderado
- 🔴 **Rojo**: consumo ocasional

RIGA **no prescribe dietas** ni reemplaza el asesoramiento profesional.
Su objetivo es **informar y orientar**.

---

## 🔬 Porciones alimentarias

Para estimar el impacto glucémico real, RIGA utiliza **porciones estándar**.

Las porciones se obtienen a partir de:

- Bases de datos públicas (USDA FoodData Central)
- Tablas de referencia abiertas
- Definiciones conservadoras cuando no existe un dato específico

Cuando no se encuentra una porción adecuada:

- Se aplica una porción por defecto documentada
- Se deja trazabilidad del origen del dato

Esto garantiza:

- Transparencia
- Reproducibilidad
- Claridad metodológica

---

## 🔐 Uso de API

La integración con fuentes externas (como USDA FoodData Central) se realiza
mediante API pública.

La clave de acceso **no se incluye en el repositorio** y debe configurarse
localmente mediante variables de entorno.

---

## 👥 ¿A quién está dirigido?

- Personas con obesidad o sobrepeso
- Personas con diabetes o resistencia a la insulina
- Familias y cuidadores
- Docentes y estudiantes
- Programas de salud pública y organizaciones comunitarias

---

## 🧱 ¿Cómo funciona?

- Web estática (HTML, CSS y JavaScript)
- Datos abiertos en formato CSV / JSON
- Procesamiento de datos mediante scripts en Python
- Hosting gratuito en GitHub Pages
- Sin registro, sin login, sin recolección de datos personales

Esto garantiza **bajo costo, transparencia y escalabilidad**.

---

## 🗄️ Fuentes de datos

Los datos nutricionales se generan automáticamente a partir de fuentes abiertas:

- **Argenfood** – Tabla de Composición de Alimentos  
  (Universidad Nacional de Luján)

Los archivos de datos **no se editan manualmente**.
Se generan mediante scripts en Python ubicados en la carpeta `/script`.

Fuente oficial:
https://www.argenfood.unlu.edu.ar/

---

## 💰 Sostenibilidad

El proyecto se sostiene mediante **publicidad contextual de bajo impacto (CMP)**,
sin suscripciones, sin muros de pago y sin manipulación de resultados.

---

## ⚖️ Ética y responsabilidad

RIGA es una herramienta informativa y educativa.
No reemplaza el asesoramiento médico ni nutricional.

---

## 👤 Autor

Proyecto desarrollado por  
**Mario Maciel**  
Analista de datos / desarrollador independiente
=======
**¿Necesitás limpiar una base de datos similar?**  
Podés contactarme a través de [LinkedIn](TU-LINK-AQUI) o enviarme propuesta en [Workana](TU-LINK-WORKANA).
>>>>>>> 2d484355c0c3d43d7551286d8d4b4935d05a7665
