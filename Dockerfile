
# Imagen base con Python 3.11.
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor.
WORKDIR /app

# Evitar archivos .pyc y utilizar salida sin búfer.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar las dependencias de Python.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación.
COPY app/ ./app/

# Puerto utilizado por Streamlit.
EXPOSE 8501

# Ejecutar Streamlit y permitir conexiones externas al contenedor.
CMD ["python", "-m", "streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]
