#!/bin/bash
echo "🌮 Framework Tools Mx - Elige interfaz:"
echo "1) CLI"
echo "2) GUI"
echo "3) Web (Flask)"
read -p "Opción: " opt
case $opt in
    1) python3 interfaces/cli.py ;;
    2) python3 interfaces/gui.py ;;
    3) python3 interfaces/web_app.py ;;
    *) echo "Opción no válida" ;;
esac
