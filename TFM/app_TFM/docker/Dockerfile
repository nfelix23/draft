# Usa la imagen base de Jupyter con PySpark
FROM jupyter/pyspark-notebook:latest

# Cambiar el usuario predeterminado a nfelix
USER root
RUN useradd -ms /bin/bash nfelix
USER nfelix

# Instalar las librerías de Python necesarias
RUN pip install --upgrade pip && \
    pip install urbanpy apache-airflow streamlit pyspark pandas h3 geopy requests python-dotenv && \
    pip install git+https://github.com/OCHA-DAP/hdx-python-api.git && \
    pip install pyhive

# Copiar el código de la aplicación al directorio de trabajo
COPY C:\Users\nfeli\Documents\Code\TFM\app_TFM\fin_edu /app
WORKDIR /app

# Exponer el puerto para Streamlit
EXPOSE 8501

# Comando por defecto para iniciar Streamlit y Jupyter Notebook
CMD ["sh", "-c", "streamlit run streamlit_app.py & start-notebook.sh"]
