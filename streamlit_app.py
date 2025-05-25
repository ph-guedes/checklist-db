import streamlit as st

st.set_page_config(
    layout="wide",
)

home_page = st.Page(
    page="views/home.py",
    title="Pagina Inicial",
    icon=":material/home:",
    default=True
)  

checklist_page = st.Page(
    page="views/checklist.py",
    title="Checklist",
    icon=":material/list:"
)

operators_page = st.Page(
    page="views/operators.py",
    title="Operador",
    icon=":material/person:"
)

uid_page = st.Page(
    page="views/uid.py",
    title="UID Operador",
    icon=":material/assignment_ind:"
)


pg = st.navigation( {
    "A": [home_page, checklist_page, ],
    "B": [operators_page, uid_page]
}
)

st.logo("assets/logo.png")
pg.run()