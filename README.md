
# 📝 Redactor-Llama3.1-V2.5

Versión estable y funcional de un script de redacción automática que utiliza **LLaMA 3.1** a través de **LM Studio**. Este script genera artículos estructurados (HTML) a partir de palabras clave proporcionadas en un archivo CSV, diseñados para optimización SEO y uso en plataformas como WordPress, aunque es totalmente multifuncional.

## 🚀 Características

- Generación de artículos HTML con título, introducción, cuerpo 1, 2 y 3, y conclusión.
- Prompts diferenciados por sección para mejorar la calidad del contenido.
- Manejo avanzado de CSV sin sobrescribir encabezados ni duplicar datos.
- Salida organizada en lineas donde se encuentra cada artículo generado.
- 100% ejecutado en local usando **LM Studio**.

---

## 📦 Instalación

Clona el repositorio:

```bash
git clone https://github.com/tuusuario/Redactor-Lllama3.1.git
cd Redactor-Lllama3.1.git
```

Asegúrate de que **LM Studio** está corriendo en local y el modelo **LLaMA 3.1** está cargado correctamente.

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta el script principal:

```bash
python redactor.py
```

---

## ⚙️ Uso

1. Prepara un archivo TXT llamado `tematica.txt` donde cada linea formara un articulo:

```txt
inteligencia artificial en educación
climatización sostenible
robots domésticos en 2025
```

2. El script procesará cada palabra clave de forma independiente y generará un artículo por fila.

3. Los artículos se registrarán en un archivo `articulos.csv`.

---

## 📁 Estructura del proyecto

```
Redactor-Llama3.1/
├── redactor.py               # Script principal
├── utils.py                  # Funciones auxiliares (lectura CSV, conexión LLM, etc.)
├── tematica.txt              # Archivo con las keywords a procesar
├── articulos.csv             # Registro de resultados generados
└── README.md                 # Este archivo
```

---

## 🧠 Ejemplo de contenido generado

```html
  <h1>El Futuro de la Inteligencia Artificial en la Educación</h1>
  <p><strong>Introducción:</strong> La inteligencia artificial está transformando los métodos de enseñanza...</p>
  <p><strong>Cuerpo:</strong> Desde tutores virtuales hasta análisis de rendimiento estudiantil, los sistemas IA están...</p>
  <p><strong>Conclusión:</strong> La implementación efectiva de IA en la educación puede marcar una diferencia significativa...</p>
```

---

## 🛡️ Licencia

Este proyecto se distribuye bajo la licencia GPL-3.0 license. Consulta el archivo `LICENSE` para más detalles.

---

## 🙌 Autor

**Rafa San Pablo González**  
Desarrollador de aplicaciones multiplataforma con interés en la inteligencia artificial y la automatización de procesos.  
[LinkedIn](#) · [GitHub](#)

---

## 📬 Contacto

¿Tienes sugerencias, mejoras o quieres colaborar?  
¡No dudes en abrir un issue o contactar!

---

## 📌 Notas adicionales

- Si estás utilizando otro modelo de lenguaje o quieres adaptarlo a nuevas versiones de LLama o herramientas como **Ollama**, puedes modificar los prompts en `GeneradorArticulos.py` y las funciones de conexión en `utils.py`.

---

## 💡 Próximas mejoras (TODO)

- Interfaz gráfica básica (GUI)
- Exportación directa a WordPress vía API
- Soporte para múltiples idiomas
- Mejora en el control del tono y estilo del contenido
