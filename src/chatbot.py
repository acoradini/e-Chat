# filepath: e-chat-streamlit/e-chat-streamlit/src/chatbot.py

import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from loaders import carrega_site, carrega_pdf

try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("Chave 'GROQ_API_KEY' não encontrada nos segredos do Streamlit. Verifique a ortografia.")
    st.stop()

api_key = st.secrets['GROQ_API_KEY']

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens, document):
    message_system = '''Você é um assistente amigável chamado Asimo.
    Você utiliza as seguintes informações para formular as suas respostas: {informacoes}'''
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado Asimo')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': document}).content
