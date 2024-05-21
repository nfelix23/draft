import streamlit as st

def sidebar():
    st.sidebar.title("Navegación")
    st.sidebar.image("assets/images/logo.png", use_column_width=True)
    st.sidebar.markdown("## Menú")
    st.sidebar.markdown("[Análisis de Datos](app.py?page=analysis)")
    st.sidebar.markdown("[Ranking Multicriterio y Presupuesto](app.py?page=ranking)")
    st.sidebar.markdown("[Análisis Geoespacial](app.py?page=geospatial)")
