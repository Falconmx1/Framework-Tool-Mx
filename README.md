# 🔍 Framework Tools Mx

> Framework OSINT mexicano con múltiples interfaces y +30 módulos listos para usar.

![version](https://img.shields.io/badge/version-1.0-blue)
![license](https://img.shields.io/badge/license-GPLv3-green)
![python](https://img.shields.io/badge/python-3.8%2B-yellow)

## 🚀 Características
- 3 interfaces: CLI, GUI (Tkinter) y Web (Flask)
- Búsqueda en +40 sitios (redes sociales, foros, leaks)
- Extracción de correos, teléfonos, dominios y usuarios
- Geolocalización IP y archivos metadatos
- Reportes en HTML/JSON/TXT

## 📦 Instalación
```bash
git clone https://github.com/Falconmx1/FrameworkToolsMx.git
cd FrameworkToolsMx
chmod +x setup.sh run.sh
./setup.sh

## 🐳 Docker (corre en cualquier sistema)

```bash
# Construir imagen
docker build -t framework-tools-mx .

# Ejecutar CLI
docker run -it framework-tools-mx ./run.sh

# Ejecutar GUI (requiere X11 en Linux/Mac)
xhost +local:docker
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix framework-tools-mx

# Ejecutar Web
docker run -p 5000:5000 framework-tools-mx python3 interfaces/web_app.py

## 🐳 Docker (corre en cualquier sistema)

```bash
# Construir imagen
docker build -t framework-tools-mx .

# Ejecutar CLI
docker run -it framework-tools-mx ./run.sh

# Ejecutar GUI (requiere X11 en Linux/Mac)
xhost +local:docker
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix framework-tools-mx

# Ejecutar Web
docker run -p 5000:5000 framework-tools-mx python3 interfaces/web_app.py
