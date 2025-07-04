# 🧠 Estrategia de Análisis y Modelado de Ventas de Pizza

---

## 1. ¿Cómo atacaría el problema?

Este reto combina **análisis exploratorio de datos (EDA)** con la posibilidad de aplicar técnicas de **machine learning**.

Algunas preguntas pueden resolverse con estadísticas simples y visualizaciones, pero otras —como "¿cómo prever ventas futuras?" o "¿cómo agrupar clientes por comportamiento?"— requieren enfoques más avanzados como regresión o clustering.

### 🔍 Enfoque general:

- **🎯 Entender los objetivos del negocio**  
  Responder las preguntas de Mario y proponer otras que ayuden a mejorar eficiencia y ventas.

- **🧼 Explorar los datos**  
  Ver qué tan limpios están, identificar valores nulos, duplicados o inconsistencias.

- **📈 Analizar y visualizar patrones de consumo**  
  Por hora, día de la semana, tipo de pizza, tamaño, etc.

- **🧠 Aplicar técnicas de IA**:
  - **Regresión**: para predecir ventas o el valor de los pedidos.
  - **Clasificación**: si hay etiquetas (ej. “pedido rentable” vs “no rentable”).
  - **Clustering**: para agrupar pizzas, clientes u horarios con comportamientos similares.

---

## 2. 🛠️ Plan paso a paso

Aquí tienes una ruta clara para abordar el proyecto:

### 📂 Preparación de los datos

- Cargar el dataset.
- Revisar valores nulos o duplicados.
- Convertir fechas y horas a formatos correctos.
- Crear columnas derivadas útiles (ej: día de la semana, hora del día, semana del año...).

### 📊 Análisis exploratorio

- Visualizar el volumen de pedidos por día y hora.
- Calcular cuántas pizzas se venden en horarios pico.
- Identificar las pizzas más y menos vendidas.
- Calcular el valor promedio de los pedidos.
- Analizar el uso de la capacidad del restaurante (15 mesas, 60 asientos).

---

## 3. 🧪 Modelos posibles

### 🔁 Regresión

Para predecir:

- Cantidad de ventas diarias.
- Valor total del pedido.
- Picos de demanda.

### 🧩 Clustering

Para segmentar:

- Tipos de pizza según ingredientes y demanda.
- Horarios según nivel de actividad (tranquilos vs pico).

### 🧭 Clasificación

Si definimos una etiqueta (por ejemplo: “venta alta” vs “venta baja”), se puede entrenar un modelo para predecir si un pedido será grande o rentable.

---

## 4. 💡 Ideas adicionales

- Estimar ingresos semanales o mensuales.
- Detectar combinaciones frecuentes de pizzas en los pedidos.
- Identificar pizzas con baja demanda → potencial para eliminar del menú.

---
