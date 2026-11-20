"""Interfaz principal del asistente."""

import streamlit as st

from app.chat import add_message, prepare_conversation
from app.bedrock_client import generate_response
from app.profiles import PROFILES


st.set_page_config(
    page_title="AWS Assistant",
    page_icon="🤖",
    layout="centered",
)

# Inicializar el estado de la sesión.
if "active_profile" not in st.session_state:
    st.session_state.active_profile = "profesor_ia"

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("RAG and LLMs Assistant for AI Practitioner")

# Selector de perfiles.
profile_ids = list(PROFILES.keys())

selected_profile = st.selectbox(
    "Selecciona un experto",
    options=profile_ids,
    format_func=lambda profile_id: PROFILES[profile_id]["name"],
    key="active_profile",
)

st.caption(
    f"Estás conversando con: {PROFILES[selected_profile]['name']}"
)

# Mostrar el historial.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"][0]["text"])

# Recibir mensajes del usuario.
if user_message := st.chat_input("Escribe tu pregunta..."):
    # Guardar y mostrar el mensaje del usuario.
    add_message(
        history=st.session_state.messages,
        role="user",
        content=user_message,
    )

    with st.chat_message("user"):
        st.write(user_message)

    # Generar una respuesta real con Amazon Bedrock.
    with st.chat_message("assistant"):
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

                st.write(assistant_response)

            except Exception:
                st.error(
                    "No se pudo generar la respuesta. "
                    "Comprueba la conexión y la configuración de Bedrock."
                )