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