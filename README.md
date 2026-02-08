# RIGA – Ranking de Impacto Glucémico de Alimentos

RIGA es una herramienta web gratuita y abierta que permite buscar alimentos
y conocer su impacto glucémico estimado de forma clara, visual y accesible.

El proyecto está orientado a salud pública, educación alimentaria y
acompañamiento en contextos de obesidad, diabetes y enfermedades metabólicas.

---

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
