"""Configuración de la aplicación y Amazon Bedrock."""

import os
from pathlib import Path

from dotenv import load_dotenv


# Cargar las variables del archivo .env.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Configuración de Amazon Bedrock.
AWS_REGION = os.getenv("AWS_DEFAULT_REGION")
BEDROCK_MODEL_ID = os.getenv("AWS_BEDROCK_MODEL_ID")


def validate_bedrock_config() -> None:
    """Valida las variables necesarias para utilizar Amazon Bedrock."""

    required_variables = (
        "AWS_BEARER_TOKEN_BEDROCK",
        "AWS_DEFAULT_REGION",
        "AWS_BEDROCK_MODEL_ID",
    )

    for variable in required_variables:
        if not os.getenv(variable):
            raise ValueError(
                f"No se encontró {variable}. "
                "Comprueba tu archivo .env."
            )