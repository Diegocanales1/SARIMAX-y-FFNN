# Pronóstico de Cierre de Acción


Bienvenidos al sitio del proyecto **Modelos no lineales para pronósticos**.  
Aquí documentamos dos enfoques para predecir el precio de cierre diario de una acción: **SARIMAX** y **FFNN**.

### Motivación del Activo: Apple Inc. (AAPL)

Elegimos Apple Inc. (AAPL) por su alta liquidez y su relevancia como indicador del mercado tecnológico global. La acción de Apple, listada en el NASDAQ, se caracteriza por ser una de las más negociadas del mundo, lo que garantiza una serie de tiempo con datos consistentes y de alta frecuencia. Pronosticar AAPL no solo es un ejercicio técnico, sino una forma de validar la capacidad de nuestros modelos (SARIMAX y FFNN) para predecir movimientos en un activo altamente volátil e influenciado por factores externos.

Apple Inc. es una empresa tecnológica multinacional con sede en Cupertino, California, fundada por Steve Jobs, Steve Wozniak y Ronald Wayne. Es reconocida por diseñar, fabricar y comercializar teléfonos inteligentes, ordenadores personales, tabletas, wearables y servicios relacionados. Su principal fuente de ingresos proviene del iPhone, pero su segmento de Servicios (App Store, iCloud, Apple Music) ha sido el motor de crecimiento más estable en los últimos años, lo que la convierte en una empresa híbrida de hardware y software.

### Hitos Principales (Factores de Impacto en el Precio)

El precio de AAPL reacciona dramáticamente a eventos corporativos. Algunos de los hitos principales que causan picos y valles en su serie de tiempo incluyen:

- Lanzamientos Clave de Productos: La revelación anual del nuevo modelo de iPhone (generalmente en septiembre) genera grandes movimientos de volatilidad. Otros lanzamientos, como las Mac con Apple Silicon (M1/M2/M3) o el Vision Pro, también marcan hitos importantes.

- Adquisiciones Estratégicas: La adquisición de Beats Electronics (2014) o las inversiones en tecnología de realidad aumentada han influido en las expectativas de crecimiento futuro.

- Cambios de CEO: La transición del liderazgo de Steve Jobs a Tim Cook (2011) fue un hito crucial que marcó el cambio de Apple de una empresa impulsada por la innovación de producto a una potencia global enfocada en la cadena de suministro y los servicios.

- Divisiones de Acciones (Stock Splits): Apple ha realizado varias divisiones de acciones (la más reciente en 2020 con 4 por 1), aumentando la liquidez y accesibilidad, lo cual se refleja en ajustes repentinos de la serie de tiempo.

- Inclusión/Exclusión de Índices: Su inclusión en el Dow Jones Industrial Average (DJIA) en 2015 consolidó su estatus como una de las empresas más importantes de la economía estadounidense.

```{toctree}
:maxdepth: 2
:caption: Contenido

docs/models/sarimax.md
docs/models/ffnn.md
docs/Results/predicciones.md
