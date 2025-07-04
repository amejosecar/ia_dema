# 🍕 Pizza Sales Dataset - Análisis y Visualización

---

## 📦 Acerca del Dataset

Este conjunto de datos de ventas de pizza contiene **12 variables clave** recopiladas durante un año completo, pensadas para facilitar el análisis de rendimiento y comportamiento de clientes en un restaurante:

### 🔑 Campos incluidos:

- `order_id`: Identificador único para cada pedido realizado por mesa.
- `order_details_id`: Identificador único para cada pizza incluida en el pedido.
- `pizza_id`: Identificador que conecta la pizza pedida con sus detalles (precio, tamaño).
- `quantity`: Cantidad pedida para cada tipo y tamaño de pizza.
- `order_date`: Fecha del pedido (previo a la cocción).
- `order_time`: Hora del pedido (previo a la cocción).
- `unit_price`: Precio unitario de la pizza en USD.
- `total_price`: Resultado de `unit_price × quantity`.
- `pizza_size`: Tamaño de la pizza (S, M, L, XL, XXL).
- `pizza_type`: Categoría de la pizza (clásica, pollo, vegetariana, etc.).
- `pizza_ingredients`: Ingredientes usados (todas llevan queso mozzarella y salsa de tomate a menos que se indique lo contrario).
- `pizza_name`: Nombre de la pizza tal como aparece en el menú.

---

## 🎯 El Desafío de Pizza 📊

Como parte del **Reto de Maven Pizza**, asumes el rol de **Consultor de BI** contratado por _Plato’s Pizza_, un restaurante de inspiración griega en Nueva Jersey.

### 📝 Nota del cliente:

> Bienvenido a bordo, ¡estamos encantados de que estés aquí para ayudar!
>
> Las cosas van bien en Plato’s, pero sabemos que hay margen de mejora.
>
> Llevamos un año recopilando datos transaccionales, pero no los hemos aprovechado.
>
> Necesitamos tu ayuda para responder preguntas como:
>
> - ¿Qué días y horas tenemos más actividad?
> - ¿Cuántas pizzas preparamos en los momentos pico?
> - ¿Cuáles son nuestras pizzas más y menos vendidas?
> - ¿Cuál es nuestro ticket medio por pedido?
> - ¿Estamos aprovechando bien nuestra capacidad? (15 mesas, 60 asientos)
>
> ¡Gracias de antemano!  
> **— Mario Maven, Gerente de Plato’s Pizza**

---

## 📥 Metodología de Recolección

Este dataset está disponible públicamente y fue consolidado para fines analíticos.

- 📎 **Link del reto**: [Kaggle - Pizza Sales Dataset](https://www.kaggle.com/datasets/shilongzhuang/pizza-sales/data)
- 📎 **Link del CSV original**:
  import
  kagglehub # Download latest version path = kagglehub.dataset_download("shilongzhuang/pizza-sales") print("Path to dataset files:", path)
  2da. pon en comentario para futuras consultas off-line C:\americo\ia_dema\z-ejercicios_kaggle\Pizza_Restaurant_Sales\data_real\Data Model - Pizza Sales.xlsx

> 📌 Para facilitar el análisis, el modelo de datos ha sido reorganizado en una sola tabla combinada que integra todas las relaciones relevantes.

---

## 💡 Mi Inspiración

El propósito de subir este dataset a Kaggle es preparar una fase de **análisis exploratorio (EDA)** utilizando **Pandas** y bibliotecas de visualización como **Matplotlib, Seaborn o Plotly**, con el objetivo de obtener insights que se traduzcan en:

- Un **panel visual interactivo** de una sola página.
- Un resumen **visual y analítico** del negocio.
- Propuestas para optimización de ventas y operación.

---
