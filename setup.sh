#!/bin/bash

echo "🔥 Framework Tools MX - Instalador 🔥"
echo "======================================"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 no encontrado. Instalando..."
    sudo apt update && sudo apt install python3 python3-pip -y
fi

# Instalar dependencias Python
echo "[*] Instalando dependencias Python..."
pip3 install --break-system-packages -r requirements.txt || pip3 install -r requirements.txt

# Instalar herramientas externas
echo "[*] Instalando Sherlock..."
git clone https://github.com/sherlock-project/sherlock.git /tmp/sherlock
cd /tmp/sherlock && python3 setup.py install && cd -

echo "[*] Instalando theHarvester..."
git clone https://github.com/laramies/theHarvester.git /tmp/theHarvester
cd /tmp/theHarvester && python3 setup.py install && cd -

echo "[✓] Instalación completada!"
echo "Ejecuta: ./run.sh"
