# 🔍 Análisis de un Diagrama de Dispersión con Variables de Vehículos Eléctricos

## 📄 Introducción

Un **diagrama de dispersión** es una herramienta visual que nos permite analizar la relación entre dos variables numéricas. Con las variables que mencionas, podemos obtener información clave sobre **rendimiento, eficiencia y tamaño** de los vehículos eléctricos.

---

## 🚗 Posibles análisis según las combinaciones de variables

### 1️⃣ Relación entre velocidad y batería

📊 **Variables:** `top_speed_kmh` vs. `battery_capacity_kWh`  
✅ **Análisis:**

- ¿Los autos con baterías más grandes tienen mayor velocidad máxima?
- Podría haber una correlación positiva, pero también dependerá del diseño aerodinámico y la eficiencia del motor.

---

### 2️⃣ Eficiencia vs. autonomía

📊 **Variables:** `efficiency_wh_per_km` vs. `range_km`  
✅ **Análisis:**

- ¿Los autos más eficientes tienen mayor autonomía?
- En teoría, sí. Un menor consumo de energía por kilómetro debería traducirse en una mayor autonomía.
- Sin embargo, otros factores como el peso y la aerodinámica pueden influir.

---

### 3️⃣ Aceleración vs. torque

📊 **Variables:** `acceleration_0_100_s` vs. `torque_nm`  
✅ **Análisis:**

- ¿Los autos con más torque aceleran más rápido?
- Normalmente, sí. Un mayor torque permite una mejor respuesta en aceleración.
- Sin embargo, el peso del vehículo y la distribución de potencia también juegan un papel clave.

---

### 4️⃣ Carga rápida vs. capacidad de batería

📊 **Variables:** `fast_charging_power_kw_dc` vs. `battery_capacity_kWh`  
✅ **Análisis:**

- ¿Los autos con baterías más grandes admiten mayor potencia de carga rápida?
- Puede haber una correlación positiva, ya que los vehículos con baterías grandes suelen admitir cargas más rápidas.
- Sin embargo, algunos modelos limitan la potencia de carga para proteger la batería.

---

### 5️⃣ Dimensiones vs. número de asientos

📊 **Variables:** `length_mm`, `width_mm`, `height_mm` vs. `seats`  
✅ **Análisis:**

- ¿Los autos más grandes tienen más asientos?
- En general, sí. Los vehículos más largos y anchos suelen ofrecer más capacidad de pasajeros.
- Sin embargo, algunos autos deportivos pueden ser grandes pero solo tener dos asientos.

---

## 📌 Conclusión

Un **diagrama de dispersión** con estas variables nos permitiría:  
✅ **Identificar correlaciones** entre rendimiento, eficiencia y tamaño.  
✅ **Detectar patrones** en el mercado de vehículos eléctricos.  
✅ **Encontrar outliers** (autos con características atípicas).
