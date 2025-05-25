import random
import streamlit as st
import pandas as pd

# Dados
data = [
    {
        "BANCADA": "Bancada_12",
        "DATA": "2025-05-18",
        "OPERADOR": "Pedro Guedes",
        "TURNO": "Tarde",
        "CORDAO COM PLUG": "OK",
        "DADOS DE PLACA": "OK",
        "GRAVACAO DE COLUNA": "OK",
        "MODELO": "VE40",
        "MOTOR": "OK",
        "PROCEL": "OK",
        "VOLTAGEM": "127V"
    },
    {
        "BANCADA": "Bancada_7",
        "DATA": "2025-05-18",
        "OPERADOR": "Ana Souza",
        "TURNO": "Manhã",
        "CORDAO COM PLUG": "OK",
        "DADOS DE PLACA": "OK",
        "GRAVACAO DE COLUNA": "NOK",
        "MODELO": "VE35",
        "MOTOR": "OK",
        "PROCEL": "N/A",
        "VOLTAGEM": "220V"
    },
    {
        "BANCADA": "Bancada_3",
        "DATA": "2025-05-17",
        "OPERADOR": "Carlos Lima",
        "TURNO": "Noite",
        "CORDAO COM PLUG": "OK",
        "DADOS DE PLACA": "OK",
        "GRAVACAO DE COLUNA": "OK",
        "MODELO": "VE50",
        "MOTOR": "OK",
        "PROCEL": "OK",
        "VOLTAGEM": "127V"
    }
]

colunas_ordenadas = [
    "BANCADA", "DATA", "TURNO", "OPERADOR",
    "MODELO", "VOLTAGEM", "DADOS DE PLACA", "PROCEL",
    "GRAVACAO DE COLUNA", "CORDAO COM PLUG", "MOTOR"
]

def gerar_dados(base, quantidade=50):
    return [random.choice(base) for _ in range(quantidade)]

dados_expandidos = gerar_dados(data, quantidade=500)

invoice_df = pd.DataFrame(dados_expandidos)[colunas_ordenadas]
st.dataframe(data=invoice_df)
