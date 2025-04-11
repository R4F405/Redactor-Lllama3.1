import os
import csv
import logging
import random
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime


# Cargar variables de entorno desde .env
load_dotenv()

# URL de la API de LM Studio desde el .env
LM_STUDIO_API_URL = os.getenv("LM_STUDIO_API_URL", "http://localhost:1234/v1")

def read_keywords(file_path):
    """Leer palabras clave desde un archivo"""
    try:
        logging.debug(f"Leyendo palabras clave desde: {file_path}")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Archivo de palabras clave no encontrado: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            keywords = [line.strip() for line in file]
        if not keywords:
            raise ValueError(f"No se encontraron palabras clave en el archivo: {file_path}")
        logging.debug(f"Palabras clave leídas: {keywords}")
        logging.info("Palabras clave leídas correctamente desde el archivo.")
        return keywords
    except Exception as e:
        logging.error(f"Error leyendo el archivo de palabras clave: {e}")
        return []

def generate_content(prompt, max_tokens=8000, temperature=1, retries=3, backoff=5):
    """Generar contenido usando LM Studio"""
    for attempt in range(retries):
        try:
            logging.debug(f"Generando contenido con el prompt: {prompt}")
            response = requests.post(
                f"{LM_STUDIO_API_URL}/chat/completions",
                json={
                    "model": "meta-llama-3.1-8b-instruct",
                    "messages": [
                        {"role": "system", "content": "Eres un asistente útil."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                }
            )
            if response.status_code != 200:
                raise ValueError(f"Error en la API de LM Studio: {response.status_code} {response.text}")
            content = response.json()["choices"][0]["message"]["content"].strip()
            logging.debug(f"Contenido generado: {content}")
            logging.info("Contenido generado correctamente.")
            return content
        except Exception as e:
            logging.error(f"Falló la generación de contenido: {e}")
            return "Error generando contenido"
    return "Error: No se pudo generar contenido tras varios intentos"

def get_random_google_link(keyword, num_results=10):
    """Obtiene un enlace aleatorio de los primeros resultados orgánicos de Google para la palabra clave dada"""
    try:
        logging.debug(f"Buscando en Google para la palabra clave: {keyword}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(f'https://www.google.com/search?q={keyword}', headers=headers)
        if response.status_code != 200:
            raise Exception(f"HTTP error {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = [a['href'] for a in soup.find_all('a', href=True) if 'url?q=' in a['href']]

        clean_results = [result.split('&')[0].replace('/url?q=', '') for result in search_results]
        logging.debug(f"Resultados de búsqueda: {clean_results}")
        if not clean_results:
            return None

        random_link = random.choice(clean_results[:num_results])
        return random_link
    except Exception as e:
        logging.error(f"Error mientras se buscaba en Google para la palabra clave '{keyword}': {e}")
        return None

def insert_link_in_content(content, keyword):
    """Inserta un enlace HTML en el contenido usando la palabra clave"""
    link = get_random_google_link(keyword)
    if link:
        anchor_tag = f'<a href="{link}" target="_blank">{keyword}</a>'
        content = content.replace("[ENLACE]", anchor_tag, 1)  # Reemplaza solo la primera aparición
    return content

def save_to_csv(data, file_path):
    """Guardar contenidos generados en un archivo CSV, añadiendo al archivo existente"""
    file_exists = os.path.isfile(file_path)
    try:
        logging.debug(f"Guardando datos en el archivo CSV: {file_path}")
        with open(file_path, 'a' if file_exists else 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['keyword', 'title', 'introduction', 'body', 'conclusion', 'full_article']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # Solo escribir el encabezado si el archivo no existe
            for row in data:
                writer.writerow(row)
        logging.info(f"Datos guardados en el archivo CSV: {file_path}")
    except Exception as e:
        logging.error(f"Error al escribir en el CSV: {e}")


def obtener_fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")
