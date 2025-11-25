# filepath: src/chatbot.py

import streamlit as st
# Não precisamos de 'os'
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from src.loaders import carrega_site, carrega_pdf # Se loaders está em src/

# Removido o teste de inicialização, que pode causar erros quando importado.
# Removido o import 'os'

try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    # NOTA: st.stop() aqui impede que o app principal (streamlit_app.py) funcione
    # Vamos apenas parar a execução desta parte, se a chave for vital
    st.error("Chave 'GROQ_API_KEY' não encontrada.")
    raise

# INICIALIZAÇÃO CORRETA: Passa a chave API diretamente
chat = ChatGroq(
    groq_api_key=groq_api_key, # <-- ESSENCIAL: CHAVE PASSADA AQUI
    model='llama-3.3-70b-versatile'
)

# A função resposta_bot está OK, mas use 'groq_api_key' se precisar dela em outro lugar.
def resposta_bot(mensagens, document):
    message_system = '''Você é um assistente amigável chamado Asimo.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}'''
    
    # Adapta o histórico para o formato que a LangChain espera
    mensagens_modelo = [('system', message_system.format(informacoes=document))]
    
    # Corrige a forma de adicionar o histórico para garantir a compatibilidade de formato
    for role, content in mensagens:
        if role == 'user':
            mensagens_modelo.append(('human', content))
        elif role == 'assistant':
            mensagens_modelo.append(('ai', content))

    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    
    # A variável 'document' agora deve ser passada dentro de 'informacoes'
    return chain.invoke({}).content
2. 📄 loaders.py (Corrigido)
Obrigatório para remover o input()!

Python

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
