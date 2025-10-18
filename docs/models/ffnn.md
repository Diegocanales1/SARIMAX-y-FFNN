# Modelo FFNN

## Resumen
- Modelo: red neuronal feed-forward (capas densas).
- Entradas: características a partir de rezagos, variables técnicas y/o exógenas.
- Salida: precio de cierre del día siguiente.

## Procedimiento
1. Escalado de variables.
2. Diseño de arquitectura (capas, neuronas, activaciones, regularización).
3. Entrenamiento con early stopping.
4. Validación temporal y selección de hiperparámetros.
5. Pronóstico diario y actualización.

## Comentarios
Captura relaciones no lineales; requiere control de sobreajuste y drift.
