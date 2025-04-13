import os
import logging
import requests
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
                        {"role": "system", "content": "Dictatae a escribir articulos en html para introducirlo en Wordpress. No hagas aclaraciones sobre lo que has escrito."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                }
            )
            if response.status_code != 200:
                raise ValueError(f"Error en la API de LM Studio: {response.status_code} {response.text}")
            content = response.json()["choices"][0]["message"]["content"].strip().replace("\n", " ")
            logging.debug(f"Contenido generado: {content}")
            logging.info("Contenido generado correctamente.")
            return content
        except Exception as e:
            logging.error(f"Falló la generación de contenido: {e}")
            return "Error generando contenido"
    return "Error: No se pudo generar contenido tras varios intentos"

import os
import logging

def save_to_csv(data, file_path):
    """Guardar contenidos en un archivo CSV sin sobrescribir los datos anteriores, agregando encabezado si es necesario."""
    temp_file_path = file_path.replace(".csv", ".txt")  # Archivo temporal .txt

    try:
        logging.debug(f"Guardando datos en: {temp_file_path}")

        encabezado = "KEYWORD\tTITLE\tINTRODUCTION\tBODY1\tBODY2\tBODY3\tCONCLUSION\n"

        # Verifica si el CSV original existe y tiene contenido
        escribir_encabezado = not os.path.exists(file_path) or os.stat(file_path).st_size == 0

        with open(temp_file_path, 'w', encoding='utf-8') as txtfile:
            if escribir_encabezado:
                txtfile.write(encabezado)

            for row in data:
                line = f"{row['keyword']}{row['title']}{row['introduction']}{row['body1']}{row['body2']}{row['body3']}{row['conclusion']}\n"
                txtfile.write(line)

        logging.info(f"Datos preparados en archivo temporal: {temp_file_path}")

        # Añadir el contenido del .txt al final del .csv
        with open(temp_file_path, 'r', encoding='utf-8') as temp_file:
            with open(file_path, 'a', encoding='utf-8', newline='') as csv_file:
                csv_file.write(temp_file.read())

        os.remove(temp_file_path)
        logging.info(f"Archivo renombrado y actualizado correctamente: {file_path}")

    except Exception as e:
        logging.error(f"Error al escribir o renombrar el archivo: {e}")




def obtener_fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")
