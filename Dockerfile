# Usa una imagen oficial de Python
FROM python:3.10

# Instalar dependencias del sistema necesarias para Grobid
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
COPY . /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8070

# Comando por defecto al iniciar el contenedor
CMD ["python", "scripts/main.py"]

