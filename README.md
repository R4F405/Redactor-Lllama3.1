# 📝 Redactor-Llama3.1-V2.5

**Redactor-Llama3.1-V2.5** es un script en Python que utiliza modelos de lenguaje locales a través de **LM Studio** para generar artículos completos y estructurados en HTML, listos para su publicación en WordPress (aunque también útiles para otros fines). Diseñado para trabajar a partir de una o varias *keywords*, permite crear contenido de forma automática, segmentada y altamente personalizable.

---

## 🚀 Características principales

- ✅ **Compatible con Llama 3.1 (vía LM Studio)**
- 🧠 Generación de contenido por secciones: título, introducción, cuerpo y conclusión.
- 🗂️ Estructura HTML optimizada para WordPress.
- 🔁 Manejo robusto de archivos CSV para importar/exportar datos sin sobrescribir encabezados.
- ✍️ Prompts mejorados para obtener artículos más coherentes, naturales y útiles.
- 🧩 Modular y fácilmente adaptable a otros modelos o plataformas.

---

## 🛠 Requisitos

- Python 3.8 o superior
- [LM Studio](https://lmstudio.ai/) instalado y configurado para servir modelos LLM localmente
- Modelo **LLaMA 3.1** (cargado localmente en LM Studio)

### Python packages
Instálalos con:

```bash
pip install -r requirements.txt
