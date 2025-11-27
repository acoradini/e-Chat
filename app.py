"""
Ponto de entrada principal da aplicação Streamlit.
Este arquivo deve estar na raiz do projeto para que o Streamlit o encontre.
"""

import sys
from pathlib import Path

# Adiciona o diretório 'src' ao path para que os imports funcionem
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Importa e executa a aplicação principal
from streamlit_app import *
