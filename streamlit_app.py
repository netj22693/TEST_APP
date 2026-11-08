import streamlit as st



main = st.Page(
    "Subpages/main_page.py",
    title="Main page"
)

Function = st.Page(
    "Subpages/Function/Function.py",
    title="Function"
)

Function_2 = st.Page(
    "Subpages/Function/Function_2.py",
    title="Function_2"
)

# ===== Navigation: =====
pg = st.navigation(
    {
        "About this application": [
            main
            ],
            
        "TESTING": [Function, Function_2],
    },
    expanded=True  #23-Jun-2025: since streamlit version 1.46.0, this is needed to have the right menu bar always open as default (possibility to collaps still available)
)

pg.run()