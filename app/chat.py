"""Lógica de preparación de conversaciones."""

from app.profiles import get_profile_prompt


def prepare_conversation(
    profile_id: str,
    history: list[dict],
) -> dict:
    """Prepara una conversación con el perfil activo y su historial."""

    system_prompt = get_profile_prompt(profile_id)

    return {
        "system": [{"text": system_prompt}],
        "messages": history.copy(),
    }

def add_message(
    history: list[dict],
    role: str,
    content: str,
) -> None:
    """Añade un mensaje al historial de conversación."""

    if role not in ("user", "assistant"):
        raise ValueError("El rol debe ser 'user' o 'assistant'.")

    if not content.strip():
        raise ValueError("El mensaje no puede estar vacío.")

    history.append(
        {
            "role": role,
            "content": [{"text": content}],
        }
    )