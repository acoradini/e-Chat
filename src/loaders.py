from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

# Aceita a URL como argumento, em vez de pedir input()
def carrega_site(url_site: str): 
    # Certifique-se de que a URL não está vazia antes de carregar
    if not url_site:
        return ""
        
    loader = WebBaseLoader(url_site)
    lista_documents = loader.load()
    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document

# Aceita o caminho do arquivo como argumento, em vez de pedir input()
def carrega_pdf(caminho: str):
    # Certifique-se de que o caminho não está vazio
    if not caminho:
        return ""

    loader = PyPDFLoader(caminho)
    lista_documents = loader.load()
    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document
