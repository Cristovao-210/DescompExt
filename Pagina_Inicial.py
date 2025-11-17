import streamlit as st
import time
from actions import formatar_dados, backgroun

st.session_state.sidebar_open = False
st.set_page_config(page_title="DescompExt", page_icon="📂")


# Detecta se o usuário veio de outra página
if "from_back" in st.session_state and st.session_state["from_back"]:
    # limpa tudo
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    # reseta o controle
    st.session_state["from_back"] = False
    backgroun.reset_app()

st.subheader("📂 DescompExt")
st.text("Descompactador de Arquivos oriundos do Extrator de Dados do SIAPE (HOD-3270)")
# Informando procedimento ao usuário 
st.markdown("""<hr><p style="font-weight: bold; text-align: center;">Carrege os arquivos obtidos na extração feita no SIAPE.
            O arquivo com layout das colunas (nome_arquivo.REF.gz) e o arquivo com os dados (nome_arquivo.TXT.gz)</p><hr>""", unsafe_allow_html=True)

# Componente para carregar os arquivos
arquivos = st.file_uploader(
    "Escolha exatamente 2 arquivos (.REF.gz e .TXT.gz)",
    type=["gz"],
    accept_multiple_files=True,
    key="upload_arquivos"
)
# Ações de validação após o carregamento do arquivo
if arquivos:
    # Validar quantidade
    if len(arquivos) != 2:
        st.error("❌ Você deve carregar **exatamente 2 arquivos**: um .REF.gz e um .TXT.gz.")
    else:
        # Identificar arquivos
        arquivo_layout = None
        arquivo_dados = None

        for arquivo in arquivos:
            nome = arquivo.name.upper()

            if nome.endswith("REF.GZ"):
                arquivo_layout = arquivo
            elif nome.endswith("TXT.GZ"):
                arquivo_dados = arquivo

        # Verificar se ambos foram encontrados
        if arquivo_layout is None or arquivo_dados is None:
            st.error("""
            ❌ Arquivos inválidos.  
            Você deve enviar **exatamente 2 arquivos**:
            - Um que termine com **REF.gz** (layout)  
            - Um que termine com **TXT.gz** (dados)  
            """)
        else:
            st.success("✔️ Arquivos carregados com sucesso!")

            try:
                # Processar arquivos 
                lista_colunas = formatar_dados.configurar_arquivos_extrator(
                    arquivo=arquivo_layout, 
                    tipo_arquivo="layout"
                )

                df_dados = formatar_dados.configurar_arquivos_extrator(
                    arquivo=arquivo_dados, 
                    tipo_arquivo="dados"
                )
                
                # Armazenar dataframe na sessão
                st.session_state.df_final = df_dados
                st.session_state.lista_colunas = lista_colunas
                
                # Para validar que há conteúdo no arquivo
                st.session_state["conteudo_arquivo"] = df_dados
                
                # Separar por colunas para centralizar o botão
                col1, col2, col3 = st.columns([0.5, 0.8, 0.1])                
                
                with col1:
                    pass
                
                with col2:
                  if st.button("📄 Formatar Dados"):
                        
                        if "pagina2" not in st.session_state:
                            st.session_state["pagina2"] = 1
                        # Efeito de carregamento
                        with st.spinner("Carregando dados..."):
                            time.sleep(3)
                        st.switch_page("pages/2_Formatar_Dados.py")

                with col3:
                    pass    
                    
            except Exception as e:
                st.error("❌ Erro ao processar os arquivos. Verifique o formato e tente novamente.")
                st.exception(e)
st.markdown("<br><hr>", unsafe_allow_html=True)
   
