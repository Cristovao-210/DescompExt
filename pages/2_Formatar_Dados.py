import streamlit as st
from actions import formatar_dados, backgroun
from views import componentes_pagina, estilos_pagina
import pandas as pd


st.set_page_config(page_title="Dados do Arquivo", page_icon="📄")
with st.container():
    st.title("📄 Dados Tabulados")

    try:
        # Para impedir que não tenha nenhum arquivo carregado e os dados continuem aparecendo em caso de navegação pela barra lateral
        if st.session_state["pagina2"] == 2:
            st.session_state["pagina2"] = 0
            backgroun.reset_app()
        else:
            # Impede acesso direto
            if "conteudo_arquivo" not in st.session_state:
                st.warning("⚠️ Nenhum arquivo foi carregado ainda. Volte para a página inicial.")
                if st.button("⬅️ Voltar"):
                    st.switch_page("Pagina_Inicial.py")
                # backgroun.reset_app()    
                st.stop()
            else:
                # Mostarar dados na tela e deixar acessível para Baixar        
                df_dowload = formatar_dados.gerar_tabela_dados_extrator(lista_colunas=st.session_state.lista_colunas, df_dados=st.session_state.df_final)
                st.session_state.pagina2 = 2
                # Barra com as opções de Download
                componentes_pagina.compontente_downoload_dados(df=df_dowload, estilo_html=estilos_pagina.estilo_tabela_download())               
    except:
                   # POR ENQUANTO VOU DEIXAR O CÓDIGO REPETIDO... MAS PRECISO REFATORAR.
        # Impede acesso direto
        if "conteudo_arquivo" not in st.session_state:
            st.warning("⚠️ Nenhum arquivo foi carregado ainda. Volte para a página inicial e carregue os arquivos necessários.")
            if st.button("⬅️ Voltar"):
                st.switch_page("Pagina_Inicial.py")
            # backgroun.reset_app()    
            st.stop()
        else:
            # Mostarar dados na tela e deixar acessível para Baixar
            formatar_dados.gerar_tabela_dados_extrator(lista_colunas=st.session_state.lista_colunas, df_dados=st.session_state.df_final)
            st.session_state.pagina2 = 2

    # Separar por colunas para centralizar o botão
    col1, col2, col3 = st.columns([0.5, 0.8, 0.1])
    with col1:
        pass
    
    with col2:
        # Botão para voltar (limpa tudo antes)
        if st.button("⬅️ Voltar"):
            st.session_state["from_back"] = True  # 🔹 marca que o usuário clicou em "Voltar"
            st.switch_page("Pagina_Inicial.py")
            backgroun.reset_app()
            
    with col3:
        pass
