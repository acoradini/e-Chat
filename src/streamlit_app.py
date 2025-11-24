import streamlit as st
from src.chatbot import resposta_bot, carrega_site, carrega_pdf

st.title("E-Chat")

st.write("Bem-vindo ao E-Chat! Escolha uma opção para carregar informações:")

option = st.selectbox(
    "Selecione uma fonte de informação:",
    ("Carregar de um site", "Carregar de um PDF")
)

if option == "Carregar de um site":
    url_site = st.text_input("Digite o URL do site:")
    if st.button("Carregar site"):
        if url_site:
            document = carrega_site(url_site)
            st.success("Site carregado com sucesso!")
        else:
            st.error("Por favor, insira um URL válido.")

elif option == "Carregar de um PDF":
    pdf_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
    if st.button("Carregar PDF"):
        if pdf_file:
            document = carrega_pdf(pdf_file)
            st.success("PDF carregado com sucesso!")
        else:
            st.error("Por favor, selecione um arquivo PDF.")

if 'document' in locals():
    st.write("Agora você pode fazer perguntas ao assistente.")
    mensagens = []
    while True:
        pergunta = st.text_input("Usuário:")
        if pergunta.lower() == 'x':
            break
        if pergunta:
            mensagens.append(('user', pergunta))
            resposta = resposta_bot(mensagens, document)
            mensagens.append({'role': 'assistant', 'content': resposta})
            st.write(f"Bot: {resposta}")

st.write("Muito obrigado por usar o E-Chat!")