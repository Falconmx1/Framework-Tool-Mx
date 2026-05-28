#!/bin/bash
echo "[*] Instalando dependencias..."
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
echo "[✔] Todo listo. Ejecuta ./run.sh"
chmod +x run.sh
