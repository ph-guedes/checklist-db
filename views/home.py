import streamlit as st
import random

def gerar_porcentagem():
    return f"+{round(random.uniform(0, 5), 2)}%"

delta_operadores = gerar_porcentagem()
delta_checklists = gerar_porcentagem()
delta_revenue = gerar_porcentagem()

cols = st.columns(3)
with cols[0]:
    with st.container(border=True):
        st.metric(label="Operadores", value="50", delta=f"{delta_operadores} from last month")

with cols[1]:
    with st.container(border=True):
        st.metric(label="Checklists", value="122", delta=f"{delta_checklists} from last month")

with cols[2]:
    with st.container(border=True):
        st.metric(label="Total Revenue", value="$45,231.89", delta=f"{delta_revenue} from last month")