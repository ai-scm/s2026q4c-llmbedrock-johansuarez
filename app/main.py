"""Interfaz principal del asistente."""

import streamlit as st

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
    new_message = {
        "role": "user",
        "content": [{"text": user_message}],
    }

    st.session_state.messages.append(new_message)

    with st.chat_message("user"):
        st.write(user_message)
