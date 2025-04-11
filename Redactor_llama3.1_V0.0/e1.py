import requests

# Leer el archivo Prompts.txt
with open('Prompts.txt', 'r', encoding='utf-8') as file:
    prompts = file.readlines()

# Asegúrate de que no está vacío y obtenemos el primer prompt
if prompts:
    prompt_usuario = prompts[0].strip()  # Obtiene la primera línea del archivo y elimina saltos de línea
else:
    prompt_usuario = "Escríbeme una historia simple"  # Fallback en caso de que el archivo esté vacío

# URL de la API de LM Studio
url = "http://localhost:1234/v1/chat/completions"

# Estructura del payload con el mensaje del usuario
payload = {
    "model": "meta-llama-3.1-8b-instruct",  # Asegúrate de que coincide con el nombre del modelo cargado en LM Studio
    "messages": [
        {"role": "user", "content": prompt_usuario}
    ]
}

# Enviar la solicitud POST
response = requests.post(url, json=payload)

# Obtener la respuesta en formato JSON
response_data = response.json()

# Imprimir el contenido generado por el modelo
print(response_data['choices'][0]['message']['content'])
