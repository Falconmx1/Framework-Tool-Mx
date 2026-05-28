import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
sys.path.append('..')
from core.scanner import OSINTScanner
from core.utils import save_report

def buscar():
    target = entry.get()
    if not target:
        messagebox.showwarning("Aguas", "Ingresa un email, usuario o IP")
        return
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, f"🔍 Escaneando {target}...\n\n")
    scanner = OSINTScanner(target)
    results = scanner.run_all()
    for k, v in results.items():
        text_area.insert(tk.END, f"--- {k.upper()} ---\n{v}\n\n")
    save_report(results, target)

# Ventana
root = tk.Tk()
root.title("Framework Tools Mx")
root.geometry("600x500")
root.configure(bg='#1e1e1e')

tk.Label(root, text="Framework Tools Mx", fg="green", bg="#1e1e1e", font=("Arial", 20)).pack(pady=10)
tk.Label(root, text="Target (email, usuario o IP):", fg="white", bg="#1e1e1e").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
tk.Button(root, text="Ejecutar OSINT", command=buscar, bg="orange").pack(pady=10)
text_area = scrolledtext.ScrolledText(root, width=70, height=20, bg="black", fg="lime")
text_area.pack(pady=10)

root.mainloop()
