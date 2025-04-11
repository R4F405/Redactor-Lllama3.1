import logging
import random
from utils import obtener_fecha_actual, save_to_csv, generate_content, read_keywords

# Definir listas de prompts para variedad
title_prompts = [
    "Escribe un título llamativo y atractivo en español (50-65 caracteres) para un artículo sobre: {}"
]

introduction_prompts = [
    "Redacta en español una introducción con etiquetas HTML (<b> por ejemplo para negrita) de 1 a 3 párrafos que enganche al lector sobre: {}"
]

body_prompts_part1 = [
    "Desarrolla en español y con etiquetas HTML  la primera parte del cuerpo del artículo con una estructura clara y jerárquica. Debe contener de 3 a 5 parrafos. Usa subtítulos <h2> y <h3>, destaca términos clave con <b> y proporciona ejemplos. Título: {}Introducción: {}Cuerpo:"
]

body_prompts_part2 = [
    "Continúa el desarrollo en español y con etiquetas HTML con la segunda parte del artículo. Debe contener de 3 a 5 parrafos. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> para destacar términos clave y agrega ejemplos relevantes. Título: {}Introducción: {}Primera parte del cuerpo: {}Segunda parte:"
]

body_prompts_part3 = [
    "Finaliza el cuerpo del artículo en español y con etiquetas HTML con la tercera parte. Debe contener de 3 a 5 parrafos. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> en palabras clave y cierra el desarrollo con ejemplos y análisis. Título: {}Introducción: {}Partes anteriores del cuerpo: {}Tercera parte:"
]

conclusion_prompts = [
    "Redacta una conclusión en español que resuma las ideas principales y proporcione un cierre adecuado para el artículo. Título: {}Introducción: {}Cuerpo: {}Conclusión:"
]

def generar_articulo(tema):
    """Genera un artículo sobre un tema usando LM Studio."""

    titulo_prompt = random.choice(title_prompts).format(tema)
    introduccion_prompt = random.choice(introduction_prompts).format(tema)
    cuerpo_prompt1 = random.choice(body_prompts_part1).format(tema, "[INTRODUCCIÓN]")
    cuerpo_prompt2 = random.choice(body_prompts_part2).format(tema, "[INTRODUCCIÓN]", "[CUERPO1]")
    cuerpo_prompt3 = random.choice(body_prompts_part3).format(tema, "[INTRODUCCIÓN]", "[CUERPO1]", "[CUERPO2]")
    conclusion_prompt = random.choice(conclusion_prompts).format(tema, "[INTRODUCCIÓN]", "[CUERPO1] [CUERPO2] [CUERPO3]")

    aclraciones = 'Antes de todo quiero hacerte unas aclaraciones:NO utilizes saltos de linea (\n). No utilizes = ,NO hagas aclaraciones o comentarios solo escribe lo que te pido, y como te digo debes utilizar etiquetas HTML, NO quiero estructura HTML, NO quiero div ni nada de eso, tampoco quiero MarkDown, tampoco quiero css. Aqui te describo lo que quiero que hagas: '

    titulo = generate_content(aclraciones + titulo_prompt)
    introduccion = generate_content(aclraciones + introduccion_prompt)
    cuerpo1 = generate_content(aclraciones + cuerpo_prompt1.replace("[INTRODUCCIÓN]", introduccion))
    cuerpo2 = generate_content(aclraciones + cuerpo_prompt2.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1))
    cuerpo3 = generate_content(aclraciones + cuerpo_prompt3.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1).replace("[CUERPO2]", cuerpo2))
    conclusion = generate_content(aclraciones + conclusion_prompt.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1).replace("[CUERPO2]", cuerpo2).replace("[CUERPO3]", cuerpo3))

    fecha = obtener_fecha_actual()
    data = [{
        "keyword": f'{tema} = ',
        "title": f'{titulo} = ',
        "introduction": f'{introduccion} = ',
        "body1": f'{cuerpo1} = ' ,
        "body2": f'{cuerpo2} = ' ,
        "body3": f' {cuerpo3} = ' ,
        "conclusion": f'{conclusion}' ,
    }]

    save_to_csv(data, "articulos.csv")
    return f"{titulo}{introduccion}{cuerpo1}{cuerpo2}{cuerpo3}{conclusion}"

if __name__ == "__main__":
    temas = read_keywords("tematica.txt")
    for tema in temas:
        print(f"Generando artículo para: {tema}")
        articulo = generar_articulo(tema)
        print("Artículo generado:\n", articulo)
