# Modelo SARIMAX

## Resumen
- Modelo: SARIMAX (ARIMA estacional con regresores exógenos si aplica).
- Objetivo: predecir el **precio de cierre** de la acción a horizonte diario.

## Procedimiento
1. Limpieza y partición de datos (train/test).
2. Identificación de órdenes (p,d,q) y estacionalidad (P,D,Q,s).
3. Ajuste por máxima verosimilitud y diagnóstico de residuales (normalidad, autocorrelación).
4. Validación con ventana deslizante y métrica (MAE/MAPE/RMSE).
5. Generación de pronósticos puntuales y bandas de confianza.

## Comentarios
Incluye supuestos de estacionariedad y linealidad local. Sensible a drift/ruido estructural.
