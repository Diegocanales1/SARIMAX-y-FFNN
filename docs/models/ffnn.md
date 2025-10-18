# Modelo FFNN (Feedforward Neural Network)

El modelo **FFNN** (Red Neuronal de Propagación Directa) se utilizó para capturar patrones no lineales en la serie de tiempo. Este enfoque se basa en el aprendizaje supervisado de ventanas de tiempo pasadas (lags).

### Preprocesamiento y Hiperparámetros

| Etapa | Detalle | Justificación |
| :--- | :--- | :--- |
| **Escalado** | **MinMax (0, 1)** | Necesario para normalizar los datos, asegurando que todas las entradas se procesen sin sesgos, lo cual es fundamental para el entrenamiento de redes neuronales. |
| **Entradas ($N_{LAG}$)** | **20 *lags*** | Se utilizaron los precios de cierre de los 20 días anteriores como entradas para predecir el siguiente precio, proporcionando a la red un contexto de casi un mes de *trading*. |
| **Capas/Neuronas** | 2 capas ocultas (64 y 32) | Arquitectura simple pero efectiva: la primera capa densa (64 neuronas) extrae características y la segunda (32 neuronas) refina la información antes de la salida. |
| **Función de Activación** | **ReLU** (Rectified Linear Unit) | Se utiliza en las capas ocultas por su eficiencia computacional y para prevenir el problema de *vanishing gradients*. |
| **Optimización** | **Adam** | Optimizador estándar y eficiente para el descenso de gradiente; la función de pérdida utilizada fue el **Error Cuadrático Medio (MSE)**. |

### Esquema de Walk-Forward y Validación

Debido a que el modelo FFNN predice solo un paso de tiempo a la vez, se empleó un esquema de **simulación Walk-Forward** para el pronóstico de 5 días:

1.  Se predice el Día 1 (2025-10-20) utilizando la ventana de 20 *lags* finales del historial de entrenamiento.
2.  La predicción del Día 1 se añade a la ventana de *lags* (eliminando el dato más antiguo).
3.  Se predice el Día 2 utilizando esta nueva ventana "avanzada", y el proceso se repite hasta completar los 5 días de la ventana de pronóstico.

* **Validación Histórica:** El modelo FFNN se entrenó sobre el *subset* de validación histórica y se probó en los mismos **20 días** que SARIMAX.
* **Métricas:** El FFNN arrojó un **MAPE** de **2.96%**, validando que, si bien es más alto que SARIMAX, sigue siendo un error aceptable para un modelo no lineal de pronóstico de precios.