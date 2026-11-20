"""Cliente para interactuar con Amazon Bedrock mediante Converse API."""

import boto3

from app.config import (
    AWS_REGION,
    BEDROCK_MODEL_ID,
    validate_bedrock_config,
)


def generate_response(conversation: dict) -> str:
    """Envía una conversación a Bedrock y devuelve la respuesta."""

    # Comprobar la configuración antes de conectarnos.
    validate_bedrock_config()

    # Crear el cliente de Amazon Bedrock.
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=AWS_REGION,
    )

    # Enviar la conversación al modelo.
    response = client.converse(
        modelId=BEDROCK_MODEL_ID,
        system=conversation["system"],
        messages=conversation["messages"],
    )

    # Extraer el texto de la respuesta.
    assistant_message = response["output"]["message"]

    return "".join(
        block["text"]
        for block in assistant_message["content"]
        if "text" in block
    )