# Usa una imagen base oficial de Python
FROM python:3.12

# Instalar dependencias del sistema
RUN apt-get update -y && \
    apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app/
#Instala las dependencias 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
