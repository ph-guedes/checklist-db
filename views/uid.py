import streamlit as st
import pandas as pd

data = [
    {
        "UID": "987732A",
        "NOME": "Pedro Guedes"
    },
    {
        "UID": "98SA2A",
        "NOME": "Azul Marinho"
    },
    {
        "UID": "554302A",
        "NOME": "Arthur Lanches"
    }
]

colunas_ordenadas = [
    "UID", "NOME"
]

invoice_df = pd.DataFrame(data)[colunas_ordenadas]

st.header("UID's")
st.dataframe(data=invoice_df, hide_index=True)

st.header("UID Logs")