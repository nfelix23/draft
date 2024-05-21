import streamlit as st
from src.components.sidebar import sidebar
from src.calculations.data_generation import generate_synthetic_data, load_real_school_data
from src.calculations.data_encoding import encode_data
from src.calculations.model_training import train_and_evaluate_models
from src.calculations.ranking_and_budget import calculate_ranking, allocate_budget
from src.calculations.geospatial_analysis import plot_geospatial_data, get_and_plot_pois
from src.utils.visualization import plot_results
from src.calculations.sentiment_analysis import analyze_sentiments
import pandas as pd
from pathlib import Path
from streamlit_folium import st_folium

# Función para cargar CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Cargar el archivo CSS
load_css('assets/css/custom_style.css')

st.set_page_config(page_title="Mi Aplicación de Educación", page_icon=":school:", layout="wide")

# Configurar barra lateral
sidebar()

# Contenido principal
st.title("Análisis de Determinantes del Rendimiento Escolar")

menu = st.sidebar.selectbox("Selecciona una opción", ["Análisis de Datos", "Ranking Multicriterio y Presupuesto", "Análisis Geoespacial"])

school_data_file = 'data/schools.csv'  # Ruta al archivo de datos de escuelas reales

# Cargar los datos de las escuelas una vez
school_locations = load_real_school_data(school_data_file)
provincias = school_locations['provincia'].unique()
selected_province = st.sidebar.selectbox("Selecciona una provincia", provincias)

# Filtrar los datos de las escuelas por la provincia seleccionada
filtered_school_locations = school_locations[school_locations['provincia'] == selected_province]

if menu == "Análisis de Datos":
    n_students_per_school = st.sidebar.slider("Número de Estudiantes por Escuela", 50, 200, 100)

    if st.sidebar.button("Generar y Analizar Datos"):
        data, _ = generate_synthetic_data(n_students_per_school, filtered_school_locations)
        st.write(f"### Datos Sintéticos de Estudiantes en {selected_province}")
        st.write(data.head())

        st.write(f"### Ubicaciones de las Escuelas en {selected_province}")
        st.write(filtered_school_locations.head())

        data_encoded = encode_data(data)
        results = train_and_evaluate_models(data_encoded)
        plot_results(results)

        # Análisis de sentimientos
        if 'Comentario' in data.columns:
            st.write(f"### Análisis de Sentimientos de los Comentarios en {selected_province}")
            sentiments_df = analyze_sentiments(data)
            st.write(sentiments_df[['Comentario', 'sentimiento_transformers', 'confianza_transformers']])

elif menu == "Ranking Multicriterio y Presupuesto":
    total_budget = st.sidebar.number_input("Presupuesto Total", min_value=1000, max_value=100000, value=50000, step=1000)
    n_students_per_school = st.sidebar.slider("Número de Estudiantes por Escuela", 50, 200, 100)

    if st.sidebar.button("Generar Datos y Calcular Ranking"):
        data, _ = generate_synthetic_data(n_students_per_school, filtered_school_locations)
        st.write(f"### Datos Sintéticos de Estudiantes en {selected_province}")
        st.write(data.head())

        school_ranking = calculate_ranking(data)
        st.write(f"### Ranking de Escuelas en {selected_province}")
        st.write(school_ranking)

        budget_allocation = allocate_budget(school_ranking, total_budget)
        st.write(f"### Asignación de Presupuesto en {selected_province}")
        st.write(budget_allocation)

elif menu == "Análisis Geoespacial":
    submenu = st.sidebar.selectbox("Selecciona una opción", ["Visualizar Características", "Accesibilidad a Escuelas"])
    n_students_per_school = st.sidebar.slider("Número de Estudiantes por Escuela", 50, 200, 100)

    if submenu == "Visualizar Características":
        feature = st.sidebar.selectbox("Selecciona una característica", ["attendance", "socioeconomic_status", "final_grade"])

        if st.sidebar.button("Mostrar Mapa"):
            data, _ = generate_synthetic_data(n_students_per_school, filtered_school_locations)
            m = plot_geospatial_data(filtered_school_locations, data, feature)
            st_folium(m, width=700, height=500)

    elif submenu == "Accesibilidad a Escuelas":
        if st.sidebar.button("Mostrar POIs Cercanos"):
            data, _ = generate_synthetic_data(n_students_per_school, filtered_school_locations)
            m = get_and_plot_pois(filtered_school_locations)
            st_folium(m, width=700, height=500)
