# 📝 Redactor-Llama3.1-V2.5

A stable and functional version of an automated writing script that utilizes **LLaMA 3.1** via **LM Studio**. This script generates structured HTML articles from keywords provided in a TXT file. It's designed for SEO optimization and use on platforms like WordPress, though it is highly versatile.

## 🚀 Features

-   Generates HTML articles with a title, introduction, body sections 1, 2, and 3, and a conclusion.
-   Utilizes section-specific prompts to enhance content quality.
-   Advanced CSV handling that avoids overwriting headers or duplicating data.
-   Each generated article is logged as a new line in the `articulos.csv` file, facilitating tracking and management.
-   Runs 100% locally using **LM Studio**.

---

## 📦 Installation

### Prerequisites

1.  **Install LM Studio**:
    * Download LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/)
    * Install by following the instructions for your operating system.

2.  **Set up LLaMA 3.1**:
    * Open LM Studio.
    * Go to the "Browse" tab.
    * Search for "llama 3.1 8b instruct" and download the Meta-Llama-3.1-8B-Instruct model.
    * This process may take some time depending on your internet connection.

3.  **Run the LM Studio Server**:
    * Once the model is downloaded, select it from your local library.
    * Click on "Start Server" (or the equivalent in your LM Studio version, often under a "Local Server" tab).
    * Configure the server to listen on `http://localhost:1234/v1`.
    * Start the server.

### Project Installation

Clone the repository:

```bash
git clone https://github.com/R4F405/Redactor-Llama3.1.git
```

Create a `.env` file based on the example:

```bash
# On Windows
copy .env.example .env

# On Linux/Mac
cp .env.example .env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

1.  Prepare a TXT file named `tematica.txt` where each line will be the basis for an article:

    ```txt
    artificial intelligence in education
    sustainable air conditioning
    domestic robots in 2025
    ```

2.  Ensure LM Studio is running with the LLaMA 3.1 model loaded and the server active.

3.  Run the main script:

    ```bash
    python GeneradorArticulos.py
    ```

4.  The articles will be logged in an `articulos.csv` file.

---

## 📁 Project Structure

```
Redactor-Llama3.1/
├── GeneradorArticulos.py     # Main script
├── utils.py                  # Helper functions (LLM connection, CSV saving, etc.)
├── tematica.txt              # File with keywords to process
├── articulos.csv             # Log of generated results
├── .env.example              # Example of required environment variables
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

---

## 🔧 Configuration

The `.env` file should contain:

```
LM_STUDIO_API_URL=http://localhost:1234/v1
```

You can adjust this URL if you have configured LM Studio to use a different port.

---

## 🧠 Example of Generated Content

```html
  <h1>The Future of Artificial Intelligence in Education</h1>
  <p><b>Introduction:</b> Artificial intelligence is transforming teaching methods...</p>
  <h2>Current AI Applications in Education</h2>
  <p>From virtual tutors to student performance analysis, AI systems are...</p>
  <p><b>Conclusion:</b> The effective implementation of AI in education can make a significant difference...</p>
```

---

## 🔍 Troubleshooting

-   **Connection Error**: Ensure LM Studio is running and the API server is active at the configured URL.
-   **Generation Errors**: Verify that the Meta-Llama-3.1-8B-Instruct model is correctly loaded in LM Studio.
-   **Slow Responses**: Adjust LM Studio settings according to your system's resources.

---

## 🛡️ License

This project is distributed under the GPL-3.0 license. See the `LICENSE` file for more details.

---

## 🙌 Author

**R4F405**
[LinkedIn](https://www.linkedin.com/in/rafaspg) · [GitHub](https://github.com/R4F405)

---

## 📬 Contact

Have suggestions, improvements, or want to collaborate?
Feel free to open an issue or get in touch!

---

## 📌 Additional Notes

-   Larger models like Llama-3.1-70B will require more system resources.
-   You can modify the prompts in `GeneradorArticulos.py` to customize the article style.
-   The generated HTML format is optimized for WordPress but can be used on any system.

---

## 💡 Upcoming Improvements (TODO)

-   Basic Graphical User Interface (GUI)
-   Direct export to WordPress via API
-   Multi-language support
-   Improved control over content tone and style
