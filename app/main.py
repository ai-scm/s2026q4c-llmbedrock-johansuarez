"""Interfaz principal del asistente."""

import streamlit as st

from pathlib import Path
from app.chat import add_message, prepare_conversation
from app.bedrock_client import generate_response
from app.profiles import PROFILES


st.set_page_config(
    page_title="AWS Assistant",
    page_icon="🤖",
    layout="wide",
)

# Cargar estilos del chat.
CSS_PATH = Path(__file__).resolve().parent / "styles" / "chat.css"
st.html(CSS_PATH)

# Inicializar el estado de la sesión.
if "active_profile" not in st.session_state:
    st.session_state.active_profile = "profesor_ia"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_profiles" not in st.session_state:
    st.session_state.message_profiles = {}

# Barra lateral.
with st.sidebar:
    st.markdown("### 🔵 AI Learning")
    st.caption("AWS AI Practitioner")

    st.divider()

    st.markdown("**PERFIL DE EXPERTO**")

    profile_ids = list(PROFILES.keys())

    selected_profile = st.selectbox(
        "Perfil de experto",
        options=profile_ids,
        format_func=lambda profile_id: PROFILES[profile_id]["name"],
        key="active_profile",
        label_visibility="collapsed",
        accept_new_options=False,
        filter_mode=None,
    )

    st.markdown("**Puedes cambiar de experto**")
    st.caption("El historial se conserva en esta sesión.")

    st.divider()

    st.caption("Temas: RAG y LLMs")


# Pregunta seleccionada desde la pantalla de bienvenida.
suggested_question = None

# Mostrar la bienvenida solo cuando no hay mensajes.
if not st.session_state.messages:
    st.header("¡Hola! ¿Qué te gustaría aprender hoy?")

    st.write(
        "Pregunta sobre modelos de lenguaje, RAG o servicios "
        "de AWS. Puedes cambiar de experto sin perder "
        "la conversación."
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("**¿Qué es un LLM?**")
            st.caption("Explicación con ejemplos")

            if st.button(
                "Preguntar",
                key="question_llm",
                use_container_width=True,
            ):
                suggested_question = "¿Qué es un LLM?"

    with col2:
        with st.container(border=True):
            st.markdown("**¿Cómo funciona RAG?**")
            st.caption("Recuperación y generación")

            if st.button(
                "Preguntar",
                key="question_rag",
                use_container_width=True,
            ):
                suggested_question = "¿Cómo funciona RAG?"

    with col1:
        with st.container(border=True):
            st.markdown("**RAG vs. fine-tuning**")
            st.caption("Cuándo utilizar cada técnica")

            if st.button(
                "Preguntar",
                key="question_comparison",
                use_container_width=True,
            ):
                suggested_question = (
                    "¿Cuál es la diferencia entre RAG y fine-tuning?"
                )

def render_chat_message(
    role: str,
    content: str,
    message_index: int,
    profile_name: str = "Asistente",
) -> None:
    """Muestra los mensajes con el diseño definido en Figma."""

    if role == "user":
        left, right = st.columns([1, 1.6])

        with right:
            with st.container(key=f"user_message_{message_index}"):
                st.markdown("**Tú**")
                st.markdown(content)

    else:
        left, right = st.columns([1.6, 1])

        with left:
            with st.container(key=f"assistant_message_{message_index}"):
                st.markdown(f"**{profile_name}**")
                st.markdown(content)

# Mostrar el historial.
for index, message in enumerate(st.session_state.messages):
    profile_name = st.session_state.message_profiles.get(
        index,
        "Asistente",
    )

    render_chat_message(
        role=message["role"],
        content=message["content"][0]["text"],
        message_index=index,
        profile_name=profile_name,
    )

# Recibir mensajes del usuario.
typed_message = st.chat_input(
    "Escribe una pregunta sobre RAG o LLMs..."
)

user_message = typed_message or suggested_question

if user_message:
    # Guardar y mostrar el mensaje del usuario.
    add_message(
        history=st.session_state.messages,
        role="user",
        content=user_message,
    )

    render_chat_message(
        role="user",
        content=user_message,
        message_index=len(st.session_state.messages) - 1,
    )



    # Generar una respuesta real con Amazon Bedrock.
    with st.spinner("Pensando..."):
        try:
            conversation = prepare_conversation(
                profile_id=selected_profile,
                history=st.session_state.messages,
            )

            assistant_response = generate_response(conversation)

            add_message(
                history=st.session_state.messages,
                role="assistant",
                content=assistant_response,
            )

            message_index = len(st.session_state.messages) - 1

            st.session_state.message_profiles[message_index] = (
                PROFILES[selected_profile]["name"]
            )

            st.rerun()

            render_chat_message(
                role="assistant",
                content=assistant_response,
                message_index=len(st.session_state.messages) - 1,
                profile_name=PROFILES[selected_profile]["name"],
            )

        except Exception:
            st.error(
                "No se pudo generar la respuesta. "
                "Comprueba la conexión y la configuración de Bedrock."
            )

st.caption(
    "La IA puede cometer errores. "
    "Contrasta la información importante."
)