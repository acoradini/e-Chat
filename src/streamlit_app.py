import streamlit as st
# Assumindo que chatbot.py e loaders.py estão em 'src/'
from src.chatbot import resposta_bot
from src.loaders import carrega_site, carrega_pdf

# --- 1. Inicialização do Estado da Sessão ---
# O Streamlit esquece variáveis a cada interação, session_state armazena o estado.
if 'document' not in st.session_state:
    st.session_state['document'] = None
if 'mensagens' not in st.session_state:
    # O histórico deve ser uma lista de tuplas ou dicionários
    st.session_state['mensagens'] = []

st.title("🤖 E-Chat")
st.write("Bem-vindo ao E-Chat! Escolha uma opção para carregar informações:")

# --- 2. Interface de Carregamento de Documentos ---
with st.sidebar:
    st.header("Fontes de Informação")
    option = st.selectbox(
        "Selecione uma fonte de informação:",
        ("Nenhuma", "Carregar de um site", "Carregar de um PDF")
    )

    if option == "Carregar de um site":
        url_site = st.text_input("Digite o URL do site:")
        if st.button("Carregar Site"):
            if url_site:
                with st.spinner('Carregando conteúdo do site...'):
                    # Chama a função corrigida do loaders.py
                    st.session_state['document'] = carrega_site(url_site)
                st.success("✅ Site carregado com sucesso!")
            else:
                st.error("Por favor, insira um URL válido.")

    elif option == "Carregar de um PDF":
        pdf_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
        if st.button("Carregar PDF"):
            if pdf_file:
                # Nota: A função carrega_pdf em loaders.py precisa ser alterada
                # para receber o objeto UploadedFile (pdf_file) e processá-lo.
                # Se não estiver adaptada, causará erro aqui.
                with st.spinner('Processando PDF...'):
                    st.session_state['document'] = carrega_pdf(pdf_file)
                st.success("✅ PDF carregado com sucesso!")
            else:
                st.error("Por favor, selecione um arquivo PDF.")


# --- 3. Interface de Chat (Se o Documento foi Carregado) ---

# Verifica se o documento foi carregado para habilitar o chat
if st.session_state['document']:
    st.success("Documento pronto! Você pode começar a perguntar ao Asimo.")

    # Exibe o histórico de mensagens
    for role, content in st.session_state['mensagens']:
        with st.chat_message(role):
            st.markdown(content)
            
    # Usa o widget de entrada de chat, que dispara um rerun ao ser usado
    if pergunta := st.chat_input("Pergunte ao Asimo:"):
        
        # Adiciona a mensagem do usuário ao histórico e exibe
        st.session_state['mensagens'].append(('user', pergunta))
        with st.chat_message("user"):
            st.markdown(pergunta)
            
        # Gera a resposta do bot
        with st.chat_message("assistant"):
            with st.spinner("Asimo está pensando..."):
                # Chama a função de resposta com o histórico e o documento carregado
                resposta = resposta_bot(st.session_state['mensagens'], st.session_state['document'])
                st.markdown(resposta)
        
        # Adiciona a resposta do bot ao histórico
        st.session_state['mensagens'].append(('assistant', resposta))

else:
    st.info("Por favor, carregue uma fonte de informação (Site ou PDF) na barra lateral para começar o chat.")

st.write("Muito obrigado por usar o E-Chat!")
