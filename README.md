# Rebel Assistant
#### Created with streamlit and langchain
---
### chat.py
- chat.py es una aplicación clon de ChatGPT
- Utiliza GPT-3 como LLM y lo expone en forma de interfaz de chat con streamlit.
- Gracias a langchain podemos llevar el registro del contexto del agente así como la posibilidad de extender las funcionalidades del agente en cualquier momento
- Se puede configurar un contexto inicial para que GPT-3 se comporte de alguna forma deseada

### doc_chat.py
- doc_chat.py es una aplicación que permite tener conversaciones con archivos PDF.
- Langchain nos permite cargar los pdf y transformarlos a texto para tokenizarlos y almacenarlos (temporalmente) en el VectorStore y poder hacer preguntas a partir de ese contexto

### Instalación
1. Clona el repositorio

```bash
git clone https://github.com/emanuelalvaradog/rebel-assistant.git
```

2. Instala las librerías
```bash
pip install -r requirements.txt
```

3. Configura la OpenAI API Key
Si lo vas a correr local elimina la siguiente línea de código (st.secrets["OEPNAI_API_KEY"]) y reemplázala por tu API KEY
```python
# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = API_KEY
```

5. Corre la aplicación de streamlit
```bash
streamlit run app.py
```
