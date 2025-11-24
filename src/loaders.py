from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

def carrega_site():
    url_site = input('Digite um site: ')
    loader = WebBaseLoader(url_site)
    lista_documents = loader.load()
    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document

def carrega_pdf():
    caminho = input('Digite o caminho do PDF: ')
    loader = PyPDFLoader(caminho)
    lista_documents = loader.load()
    document = ''
    for doc in lista_documents:
        document += doc.page_content
    return document