import streamlit as st
import pandas as pd

data = [
    {
        "MATRICULA": "0001",
        "NOME": "Pedro Guedes",
        "DATA DE NASCIMENTO": "2002-05-22",
        "EMAIL": "pedro.guedes@email.com",
        "CELULAR": "(11) 91234-5678",
        "FUNCAO": "Operador de Produção",
        "STATUS": "Ativo"
    },
    {
        "MATRICULA": "0002",
        "NOME": "Azul Marinho",
        "DATA DE NASCIMENTO": "2002-05-22",
        "EMAIL": "azul.marinho@email.com",
        "CELULAR": "(11) 98765-4321",
        "FUNCAO": "Técnico de Manutenção",
        "STATUS": "Ativo"
    },
    {
        "MATRICULA": "0003",
        "NOME": "Arthur Lanches",
        "DATA DE NASCIMENTO": "2002-05-22",
        "EMAIL": "arthur.lanches@email.com",
        "CELULAR": "(11) 90000-0000",
        "FUNCAO": "Auxiliar",
        "STATUS": "Inativo"
    }
]

colunas_ordenadas = [
    "MATRICULA", "NOME", "DATA DE NASCIMENTO",
    "EMAIL", "CELULAR", "FUNCAO", "STATUS"
]

invoice_df = pd.DataFrame(data)[colunas_ordenadas]

st.header("Lista de Operadores")
st.dataframe(data=invoice_df)