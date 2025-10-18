# -- Path setup --------------------------------------------------------------

import os
import sys
# Asegúrate de que Sphinx pueda encontrar tu script de Python (prediccion_acciones.py)
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'SARIMAX y FFNN para Predicción de Acciones'
copyright = '2025, Max Aguayo, Diego Canales, David Gutierrez'
author = 'Max Aguayo, Diego Canales, David Gutierrez'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Para documentar código Python automáticamente
    'sphinx.ext.napoleon', # Para soportar docstrings de NumPy/Google
    'sphinx_rtd_theme',    # Tema Read the Docs
    'myst_parser',         # Para que Sphinx pueda leer archivos Markdown (.md)
]

# Fuentes de la documentación
# Usamos solo '.md' y lo mapeamos a 'markdown'
source_suffix = ['.rst', '.md'] 

# La raíz de la documentación
# Sphinx busca 'index' y encontrará index.md porque está en source_suffix
master_doc = 'index'

# Lista de patrones para ignorar
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
