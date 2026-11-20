# Ejercicio práctico LLM Bedrock - Johan Suarez

Asistente educativo conversacional para aprender sobre **modelos de lenguaje (LLMs)**, **Retrieval-Augmented Generation (RAG)**, enfocado al AWS AI Practitioner.

La aplicación está desarrollada con **Python y Streamlit** y genera respuestas mediante **Amazon Bedrock Converse API**, utilizando **Boto3**. Permite cambiar de experto durante una conversación sin perder el historial de la sesión.

## Funcionalidades

- **Tres perfiles de expertos:**
  - **Profesor de IA:** explica conceptos de forma clara y pedagógica.
  - **Arquitecto AWS:** se centra en servicios, arquitecturas y decisiones técnicas de AWS.
  - **Entrenador:** propone preguntas y ejercicios para practicar.
- **Historial de conversación por sesión:** los mensajes se conservan al cambiar de perfil.
- **Interfaz conversacional:** selector de experto, bienvenida con preguntas sugeridas y mensajes diferenciados por participante.
- **Ejecución local o en Docker.**

## Tecnologías

- Python 3.11
- Streamlit
- Boto3
- Amazon Bedrock (Converse API)
- python-dotenv
- Docker

## Estructura del proyecto

```text
.
├── app/
│   ├── __init__.py
│   ├── main.py             # Interfaz Streamlit y estado de sesión
│   ├── profiles.py         # Perfiles y prompts de sistema
│   ├── chat.py             # Historial y preparación de conversaciones
│   ├── bedrock_client.py   # Invocación de Converse API con Boto3
│   ├── config.py           # Lectura y validación de configuración
│   └── styles/
│       └── chat.css        # Estilos de la interfaz
├── docs/                   # Documentación del proyecto
├── .dockerignore           # Exclusiones del contexto de Docker
├── .gitignore              # Exclusiones de Git
├── Dockerfile              # Imagen de la aplicación
├── README.md
└── requirements.txt        # Dependencias Python
```

El archivo `.env` se crea **localmente** en la raíz del proyecto; no debe subirse al repositorio ni incorporarse a la imagen Docker.

## Requisitos previos.

Para ejecutar la aplicación localmente:

1. Tener **Python 3.11** instalado.
2. Tener acceso autorizado a **Amazon Bedrock** en la cuenta y región de AWS correspondiente.
3. Contar con una **API Key de corta duración de Bedrock** válida y permisos para invocar el modelo configurado.

Para ejecutarla en un contenedor  se necesita **Docker Desktop** o un motor Docker compatible en funcionamiento.

> La configuración utilizada durante el desarrollo fue la región **N. Virginia (`us-east-1`)** y el modelo **Amazon Nova Lite (`amazon.nova-lite-v1:0`)**. 

## Configuración

Crea un archivo `.env` en la raíz del proyecto con estas variables:

```dotenv
AWS_BEARER_TOKEN_BEDROCK=TU_API_KEY_TEMPORAL
AWS_DEFAULT_REGION=us-east-1
AWS_BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
```

Sustituye `TU_API_KEY_TEMPORAL` por una API Key válida.

## Ejecutar localmente con Python

Abre una terminal en la raíz del repositorio.

**1. Instala las dependencias:**

```powershell
python -m pip install -r requirements.txt
```

**2. Inicia Streamlit:**

```powershell
python -m streamlit run app/main.py
```

**3. Abre la aplicación:**

Visita [http://localhost:8501](http://localhost:8501) en tu navegador.

## Ejecutar con Docker

Ejecuta estos comandos desde la raíz del repositorio, con Docker en funcionamiento.

**1. Construye la imagen:**

```powershell
docker build -t aws-ai-assistant:1.0 .
```

**2. Inicia el contenedor:**

```powershell
docker run --rm --name aws-ai-assistant -p 8501:8501 --env-file .env aws-ai-assistant:1.0
```

**3. Abre la aplicación:**

Visita [http://localhost:8501](http://localhost:8501).

## Cómo utilizar el asistente

1. Abre la aplicación.
2. Selecciona **Profesor de IA**, **Arquitecto AWS** o **Entrenador** en la barra lateral.
3. Escribe una pregunta o elige una sugerencia de la pantalla de bienvenida.
4. Continúa la conversación y cambia de experto cuando lo necesites: el historial se mantiene durante la sesión activa de Streamlit.

## Documentación y diseño

- Documentación técnica: [`docs/04-technical-architecture.md`](docs/04-technical-architecture.md)
- [Diseño UX/UI en Figma](https://www.figma.com/design/tWNL7UNewdMUwDjCH0926V)
