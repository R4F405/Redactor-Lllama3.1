import random
from utils import obtener_fecha_actual, save_to_csv, generate_content, read_keywords

# Definir listas de prompts para variedad
title_prompts = [
    "Escribe un título impactante y envolvente en español alrededor de 70 caracteres que despierte la emoción sobre: {}",
    "Escribe un título llamativo y atractivo en español (50-65 caracteres) para un artículo sobre: {}",
    "Redacta un título directo y práctico en español (50-65 caracteres) que resuma el valor del artículo sobre: {}"
]

introduction_prompts = [
    "Redacta en español una introducción atrapante con etiquetas HTML. Usa <b> para destacar puntos clave y despierta la curiosidad del lector con una historia o dato sorprendente. Debe tener de 2 párrafos sobre: {}",
    "Redacta en español una introducción con etiquetas HTML (<b> por ejemplo para negrita) de 1 a 3 párrafos que enganche al lector sobre: {}",
    "Escribe en español una introducción clara y atractiva con etiquetas HTML. Usa <b> para resaltar conceptos importantes y menciona los beneficios que obtendrá el lector al seguir leyendo. Debe contener de 2 a 4 párrafos sobre: {}"
]

body_prompts_part1 = [
    "Desarrolla la primera sección del artículo en español con etiquetas HTML. Debe contener de 3 a 5 parrafos. Usa subtítulos <h2> y <h3>, resalta términos con <b> y presenta el tema con un enfoque narrativo o una anécdota llamativa. Debe contener de 3 a 5 párrafos. No repitas la introducción. Tema: {}Introducción: {}Primera parte:",
    "Desarrolla en español y con etiquetas HTML  la primera parte del cuerpo del artículo con una estructura clara y jerárquica. Debe contener de 3 a 5 parrafos. Usa subtítulos <h2> y <h3>, destaca términos clave con <b> y proporciona ejemplos. Tambien recuerda que no debe repetir informacion de la introudccion. Título: {}Introducción: {}Cuerpo:",
    "Elabora la primera parte del artículo en español con etiquetas HTML. Usa subtítulos <h2> y <h3>, resalta términos clave con <b> y organiza la información en una lista o puntos clave si es relevante. Debe contener de 3 a 5 parrafos. No repitas la introducción. Tema: {}Introducción: {}Primera parte:"
]

body_prompts_part2 = [
    "Expande la información con la segunda parte del artículo en español usando etiquetas HTML. Incluye subtítulos <h2> y <h3>, resalta palabras clave con <b> y presenta datos relevantes o curiosidades. Debe contener de 3 a 5 parrafos. No repitas información de secciones anteriores. Tema: {}Introducción: {}Primera parte del cuerpo: {}Segunda parte:",
    "Continúa el desarrollo en español y con etiquetas HTML con la segunda parte del artículo. Debe contener de 3 a 5 parrafos. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> para destacar términos clave y agrega ejemplos relevantes. Título: {}Introducción: {} Recuerda que para generar el segundo body NO debes repetir informacion de la introduccion ni del primer body, ni ser redundante. {}Segunda parte:",
    "Desarrolla la segunda parte del artículo en español usando etiquetas HTML. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> en palabras clave y ofrece una lista de consejos, pasos o elementos si es adecuado. No repitas información de secciones previas. Debe contener de 3 a 5 parrafos. Tema: {}Introducción: {}Primera parte del cuerpo: {}Segunda parte:"
]

body_prompts_part3 = [
    "Cierra el cuerpo del artículo con una tercera parte en español utilizando etiquetas HTML. Usa subtítulos <h2> y <h3>, resalta términos clave con <b> y finaliza con una reflexión o una pregunta al lector. Debe contener de 3 a 5 parrafos. No repitas información previa. Tema: {}Introducción: {}Cuerpo desarrollado hasta ahora: {}Tercera parte:",
    "Completa el desarrollo del artículo con la tercera parte en español, utilizando etiquetas HTML. Debe contener de 3 a 5 parrafos. Usa subtítulos <h2> y <h3>, resalta palabras clave con <b> y aporta ejemplos, recomendaciones finales o estudios de caso. No repitas información de secciones anteriores. Tema: {}Introducción: {}Cuerpo desarrollado hasta ahora: {}Tercera parte:",
    "Finaliza el cuerpo del artículo en español y con etiquetas HTML con la tercera parte. Debe contener de 3 a 5 parrafos. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> en palabras clave y cierra el desarrollo con ejemplos y análisis. Título: {}Introducción: {}Recuerda que para generar el segundo body NO debes repetir informacion de la introduccion nidel primer y segundo body, ni ser redundante: {}Tercera parte:"
]

conclusion_prompts = [
    "Escribe una conclusión que deje una impresión duradera en español con etiquetas HTML. Debe contener de 3 a 5 parrafos.Resume las ideas principales e invita al lector a la acción o reflexión. Tema: {}Introducción: {}Cuerpo: {}Conclusión:",
    "Finaliza el cuerpo del artículo en español y con etiquetas HTML con la tercera parte. Debe contener de 3 a 5 parrafos. Mantén la estructura con subtítulos <h2> y <h3>, usa <b> en palabras clave y cierra el desarrollo con ejemplos y análisis. Título: {}Introducción: {}Recuerda que para generar el segundo body NO debes repetir informacion de la introduccion nidel primer y segundo body, ni ser redundante: {}Tercera parte:",
    "Escribe una conclusión en español con etiquetas HTML que resuma los puntos clave y proporcione un cierre práctico. Debe contener de 3 a 5 parrafos. Puede incluir una llamada a la acción o un consejo final. Tema: {}Introducción: {}Cuerpo: {}Conclusión:"
]

def generar_articulo(tema):
    """Genera un artículo sobre un tema usando LM Studio."""

    titulo_prompt = random.choice(title_prompts).format(tema)
    introduccion_prompt = random.choice(introduction_prompts).format(tema)
    cuerpo_prompt1 = random.choice(body_prompts_part1).format(tema, "[INTRODUCCIÓN]")
    cuerpo_prompt2 = random.choice(body_prompts_part2).format(tema, "[INTRODUCCIÓN]", "[CUERPO1]")
    cuerpo_prompt3 = random.choice(body_prompts_part3).format(tema, "[INTRODUCCIÓN]", "[CUERPO1]", "[CUERPO2]")
    conclusion_prompt = random.choice(conclusion_prompts).format(tema, "[INTRODUCCIÓN]", "[CUERPO1] [CUERPO2] [CUERPO3]")

    aclraciones = 'Antes de todo quiero hacerte unas aclaraciones: Recuerda abrir y cerrar bien las etiquetas y que sean del mismo tipo para que no surgan errores. NO utilizes saltos de linea (n), ni tabulaciones (t).NO hagas aclaraciones o comentarios solo escribe lo que te pido, y como te digo debes utilizar etiquetas HTML, NO quiero estructura HTML, NO quiero div ni nada de eso, tampoco quiero MarkDown, tampoco NO quiero que uses css. Aqui te describo lo que quiero que hagas: '

    titulo = generate_content(aclraciones + titulo_prompt)
    introduccion = generate_content(aclraciones + introduccion_prompt)
    cuerpo1 = generate_content(aclraciones + cuerpo_prompt1.replace("[INTRODUCCIÓN]", introduccion))
    cuerpo2 = generate_content(aclraciones + cuerpo_prompt2.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1))
    cuerpo3 = generate_content(aclraciones + cuerpo_prompt3.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1).replace("[CUERPO2]", cuerpo2))
    conclusion = generate_content(aclraciones + conclusion_prompt.replace("[INTRODUCCIÓN]", introduccion).replace("[CUERPO1]", cuerpo1).replace("[CUERPO2]", cuerpo2).replace("[CUERPO3]", cuerpo3))

    fecha = obtener_fecha_actual()
    data = [{
        "keyword": f'{tema} \t ',
        "title": f'{titulo} \t ',
        "introduction": f'{introduccion} \t ',
        "body1": f'{cuerpo1} \t ' ,
        "body2": f'{cuerpo2} \t ' ,
        "body3": f' {cuerpo3} \t ' ,
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
