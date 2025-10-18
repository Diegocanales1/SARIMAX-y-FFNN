# Modelo SARIMAX (Series de Tiempo)

El modelo **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous factors) fue implementado para capturar la estructura lineal de la serie de precios de cierre (Close) de AAPL.

### Selección de Órdenes y Estacionalidad

Se utilizó un enfoque estándar de la metodología Box-Jenkins:

| Parámetro | Orden Seleccionado | Justificación Metodológica |
| :--- | :--- | :--- |
| **Integración ($d$)** | **1** | La prueba de Dickey-Fuller Aumentada (ADF) sobre los precios de cierre mostró la necesidad de una **primera diferencia** para lograr la estacionariedad de la media (eliminación de la tendencia). |
| **AutoRegresivo ($p$)** | **5** | El análisis de la **Función de Autocorrelación Parcial (PACF)** de la serie diferenciada mostró picos significativos que se cortaron en el rezago 5, indicando que el precio actual depende significativamente de los últimos 5 días de *trading*. |
| **Media Móvil ($q$)** | **0** | La **Función de Autocorrelación (ACF)** de la serie diferenciada no mostró picos significativos después de los primeros rezagos, por lo que el componente de media móvil se fijó en cero. |
| **Estacionalidad ($P, D, Q)_s$** | **(0, 0, 0)$_0$** | La serie de precios diarios no presenta patrones de estacionalidad clara a largo plazo (e.g., anuales), lo cual fue corroborado por la **ACF en rezagos anuales (252 días)**. |

**Orden Final:** Se empleó el modelo **SARIMAX(5, 1, 0) $\times$ (0, 0, 0, 0)** sin variables exógenas.

### Criterios de Evaluación y Validación

El modelo fue entrenado con la minimización del **Criterio de Información de Akaike (AIC)**, que penaliza modelos complejos, buscando el mejor ajuste con la menor cantidad de parámetros.

* **Validación Histórica:** Para medir su rendimiento, se reservó un conjunto de prueba de **20 días** previos al pronóstico final.
* **Métricas:** El modelo SARIMAX demostró una gran capacidad de ajuste con un **MAPE (Error Porcentual Absoluto Medio)** de **3.30%** en el conjunto de prueba, indicando un error promedio muy bajo.