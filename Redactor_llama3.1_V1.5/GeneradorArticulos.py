import logging
from utils import obtener_fecha_actual, save_to_csv, get_random_google_link, generate_content, read_keywords

def generar_articulo(tema):
    """Genera un artículo sobre un tema usando LM Studio."""
    enlaces = [get_random_google_link(tema) for _ in range(3)]  # Obtener 3 enlaces aleatorios
    enlaces = [link for link in enlaces if link]  # Filtrar enlaces nulos

    prompt = f"Genera un artículo sobre {tema} en español con estructura CSV, incluyendo títulos, negritas y enlaces a: {', '.join(enlaces)}."
    contenido = generate_content(prompt)

    fecha = obtener_fecha_actual()
    data = [{
        "keyword": tema,
        "title": contenido[:100],  # Extraer un título básico
        "introduction": contenido[:200],  # Introducción tentativa
        "body": contenido,  # Cuerpo completo
        "conclusion": "Conclusión generada automáticamente",
        "full_article": contenido
    }]

    save_to_csv(data, "articulos.csv")
    return contenido

if __name__ == "__main__":
    temas = read_keywords("tematica.txt")  # Leer temas desde el archivo
    for tema in temas:
        print(f"Generando artículo para: {tema}")
        articulo = generar_articulo(tema)
        print("Artículo generado:\n", articulo)
