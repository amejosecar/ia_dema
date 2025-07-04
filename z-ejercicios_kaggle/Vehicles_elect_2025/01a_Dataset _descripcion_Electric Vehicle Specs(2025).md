## 🚗🔋 Conjunto de Datos de Vehículos Eléctricos

### 📄 Descripción

Este conjunto de datos proporciona una colección detallada de especificaciones y métricas de rendimiento de vehículos eléctricos modernos (EVs). Está diseñado para ayudar a investigadores, analistas, estudiantes y desarrolladores en:

- 📊 Ciencia de Datos y Aprendizaje Automático
- 🚘 Investigación del Mercado Automotriz
- 🌱 Estudios de Sostenibilidad
- ⚡ Análisis de Adopción de Vehículos Eléctricos

Cada fila del conjunto de datos representa un modelo específico de vehículo eléctrico con un conjunto rico de atributos.

---

### 🔑 Atributos Principales

- 🏭 **Marca y Modelo**: Fabricante y nombre específico del EV.
- 🚙 **Tipo de Carrocería**: Clasificación como hatchback, SUV, sedán, etc.
- 📏 **Segmento**: Segmento del vehículo (ej. compacto, mediano, ejecutivo).

### 🔋 Batería y Autonomía

- ⚡ **Capacidad de Batería (kWh)**: Capacidad total de energía de la batería.
- 🔩 **Número de Celdas y Tipo de Batería**: Información técnica de la batería, cuando esté disponible.
- 🔥 **Eficiencia (Wh/km)**: Tasa de consumo de energía del vehículo.
- 🚗 **Autonomía (km)**: Rango estimado de conducción con carga completa.

### ⚡ Detalles de Carga

- ⚡ **Potencia de Carga Rápida (kW)**: Potencia máxima admitida para carga rápida DC.
- 🔌 **Tipo de Puerto de Carga Rápida**: Estándar de conector (ej. CCS, CHAdeMO).

### 🏎️ Rendimiento

- 🚀 **Velocidad Máxima (km/h)**: Velocidad máxima del vehículo.
- ⏱️ **Aceleración 0–100 km/h (s)**: Tiempo para alcanzar 100 km/h desde parado.
- 🔄 **Torque (Nm)**: Salida máxima de torque, cuando esté disponible.

### 📦 Especificaciones Prácticas

- 🚚 **Capacidad de Remolque (kg)**: Capacidad de carga, cuando aplique.
- 🎒 **Volumen de Carga (L)**: Espacio de equipaje, a veces aproximado o expresado en unidades alternativas.
- 🪑 **Asientos**: Capacidad total de asientos.

### 📏 Dimensiones

- 📐 **Longitud, Anchura, Altura (mm)**: Tamaño físico del vehículo.

### ⚙️ Información Técnica

- 🔄 **Tracción**: Configuración del tren motriz (ej. AWD, RWD, FWD).
- 🔗 **URL de Fuente**: Enlace de referencia para cada vehículo (usado en scraping).

---

### 🛠️ Calidad y Limpieza de Datos

- ✅ Todos los campos numéricos han sido limpiados y convertidos a tipos de datos apropiados (`float`, `int`).
- ❌ Algunos valores faltantes permanecen en atributos técnicos como capacidad de remolque y número de celdas de batería donde los datos no pudieron ser extraídos de manera confiable.

### 📌 Casos de Uso

- 📈 Análisis y visualización de tendencias de EV
- 🔍 Herramientas de comparación de mercado
- 🤖 Ingeniería de características para modelos de ML
- 🚗 Predicción de rendimiento de vehículos
- 🌍 Perspectivas sobre adopción de energía limpia
