import os
import sys
from unittest.mock import Mock
sys.path.insert(0, os.path.abspath('.'))

MOCK_MODULES = [
    'numpy', 'pandas', 'yfinance', 
    'matplotlib', 'matplotlib.pyplot', 
    'plotly', 'plotly.graph_objs', 'plotly.express', 
    'statsmodels', 'statsmodels.tsa', 'statsmodels.tsa.statespace',
    'statsmodels.tsa.statespace.sarimax', 
    'sklearn', 'sklearn.preprocessing', 
    'tensorflow', 'tensorflow.keras', 'tensorflow.keras.models', 
    'tensorflow.keras.layers', 'tensorflow.keras.callbacks'
]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()


project = 'SARIMAX y FFNN para Predicción de Acciones'
copyright = '2025, Max Aguayo, Diego Canales, David Gutierrez'
author = 'Max Aguayo, Diego Canales, David Gutierrez'

master_doc = 'index'
source_suffix = ['.rst', '.md']

def conf_general(app, config):
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(config.extensions['myst_parser'])


html_theme = 'sphinx_rtd_theme'
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'sphinx.ext.linkcode', 
    'myst_parser' # Extensión moderna para procesar archivos .md
]

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info.get('module') or not info.get('fullname'):
        return None
    return None 

html_static_path = ['_static']

autodoc_member_order = 'bysource'
napoleon_google_docstring = True
napoleon_numpy_docstring = True

html_show_sourcelink = False # Ocultar enlace a fuente
html_show_sphinx = False # Ocultar footer de Sphinx

html_context = {
    "display_github": True,
    "github_user": "DiegoCanales1", 
    "github_repo": "SARIMAX-y-FFNN",
    "github_version": "main", # o master
    "conf_py_path": "/",
}
