import streamlit as st
from actions import backgroun

def compontente_downoload_dados(df, estilo_html):
    with st.expander("📥 Escolha o formato para download"):
        # Criar 4 colunas para alinhar os botões
        col1, col2, col3, col4 = st.columns(4)

        with col1:
                backgroun.baixar_df(df, "csv", "")

        with col2:
                backgroun.baixar_df(df, "json", "")

        with col3:
                backgroun.baixar_df(df, "xlsx", "")

        with col4:
                backgroun.baixar_df(df, "html", estilo_html)
