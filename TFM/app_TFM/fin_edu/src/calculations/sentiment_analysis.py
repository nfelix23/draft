from transformers import pipeline
import pandas as pd

# Cargar el pipeline de análisis de sentimientos de Hugging Face para español
analizador_sentimientos = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

# Función para analizar sentimientos con Transformers
def analizar_sentimiento_transformers(texto):
    resultado = analizador_sentimientos(texto)[0]
    return resultado['label'], resultado['score']

# Función principal para realizar el análisis de sentimientos
def analyze_sentiments(df):
    if 'Comentario' in df.columns:
        sentimientos_transformers = df['Comentario'].apply(analizar_sentimiento_transformers)
        df['sentimiento_transformers'] = sentimientos_transformers.apply(lambda x: x[0])
        df['confianza_transformers'] = sentimientos_transformers.apply(lambda x: x[1])
    return df
