FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalar herramientas OSINT
RUN pip3 install --no-cache-dir \
    requests \
    flask \
    holehe \
    sherlock-project \
    theHarvester \
    beautifulsoup4 \
    colorama

# Crear directorio de trabajo
WORKDIR /app

# Copiar código
COPY . /app

# Permisos
RUN chmod +x /app/run.sh /app/setup.sh

# Puerto para web
EXPOSE 5000

# Comando por defecto
CMD ["/bin/bash", "-c", "./run.sh"]
