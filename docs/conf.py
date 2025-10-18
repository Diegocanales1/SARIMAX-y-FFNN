import os
import sys
sys.path.insert(0, os.path.abspath('..'))


project = 'SARIMAX y FFNN para Predicción de Acciones'
copyright = '2025, Max Aguayo, Diego Canales, David Gutierrez'
author = 'Max Aguayo, Diego Canales, David Gutierrez'


extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'sphinx_rtd_theme',    
    'myst_parser',       
]

source_suffix = ['.rst', '.md'] 

master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
