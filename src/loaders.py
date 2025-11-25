# filepath: src/loaders.py

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

# Deve receber a URL como argumento, não usar input()
def carrega_site(url_site: str): 
    if not url_site:
        return ""
    loader = WebBaseLoader(url_site)
    lista_documents = loader.load()
    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document

# Deve receber o objeto UploadedFile, não um caminho de input()
# NOTA: O tratamento de PDF no Streamlit é complexo. 
# Para simplificar, o Loader deve ler o arquivo temporariamente.
def carrega_pdf(uploaded_file):
    if not uploaded_file:
        return ""
        
    # Salva o arquivo temporariamente (necessário para PyPDFLoader)
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = PyPDFLoader(tmp_file_path)
    lista_documents = loader.load()
    
    # Limpeza: Deleta o arquivo temporário
    os.remove(tmp_file_path)

    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document
