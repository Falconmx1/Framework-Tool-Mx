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
