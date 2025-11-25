import os

# Configura USER_AGENT para requisições HTTP (defina antes de importar loaders que possam ler essa variável)
os.environ["USER_AGENT"] = os.environ.get(
    "USER_AGENT",
    "e-Chat/0.1 (+https://github.com/acoradini/e-Chat; contact: dev@yourdomain.com)",
)

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

# Deve receber a URL como argumento, não usar input()
def carrega_site(url_site: str):
    if not url_site:
        return ""

    # Prefira passar o header explicitamente para garantir que o User-Agent será usado
    ua = os.environ.get(
        "USER_AGENT", "e-Chat/0.1 (+https://github.com/acoradini/e-Chat)"
    )

    # Passa o header via requests_kwargs para garantir que o User-Agent seja aplicado
    loader = WebBaseLoader(url_site, requests_kwargs={"headers": {"User-Agent": ua}})
    lista_documents = loader.load()
    document = ""
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

    tmp_file_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        loader = PyPDFLoader(tmp_file_path)
        lista_documents = loader.load()

        document = ""
        for doc in lista_documents:
            document += doc.page_content
        return document
    finally:
        # Limpeza: Deleta o arquivo temporário se foi criado
        if tmp_file_path and os.path.exists(tmp_file_path):
            try:
                os.remove(tmp_file_path)
            except Exception:
                # não quebrar a aplicação por falha na limpeza
                pass
