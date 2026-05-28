import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.logo import LOGO_ASCII
from modules.holehe_module import check_email_breaches
from modules.sherlock_module import search_username_sherlock
from modules.theharvester_module import search_emails_and_domains

class FrameworkToolsMX:
    def __init__(self, root):
        self.root = root
        self.root.title("Framework Tools MX - OSINT Framework")
        self.root.geometry("900x700")
        self.root.configure(bg='#0a0e1a')
        
        # Estilo moderno
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#0a0e1a')
        style.configure('TLabel', background='#0a0e1a', foreground='#00ff41', font=('Consolas', 10))
        style.configure('TButton', background='#1e3a2f', foreground='#00ff41', font=('Arial', 10, 'bold'))
        
        self.create_widgets()
        self.show_logo()
    
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Logo label
        self.logo_label = ttk.Label(main_frame, text="", font=('Consolas', 8), foreground='#00ff41')
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Selector de módulo
        ttk.Label(main_frame, text="Módulo OSINT:", font=('Arial', 12, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.module_var = tk.StringVar(value="Email Leaks (Holehe)")
        self.module_combo = ttk.Combobox(main_frame, textvariable=self.module_var, 
                                         values=["Email Leaks (Holehe)", "Usuario Redes (Sherlock)", 
                                                "Dominio/Email (theHarvester)"], width=30)
        self.module_combo.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Target input
        ttk.Label(main_frame, text="Target:", font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.target_entry = ttk.Entry(main_frame, width=50, font=('Arial', 11))
        self.target_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Botón ejecutar
        self.run_button = ttk.Button(main_frame, text="🔥 EJECUTAR OSINT 🔥", command=self.run_osint)
        self.run_button.grid(row=3, column=0, columnspan=2, pady=15)
        
        # Área de resultados
        self.result_text = scrolledtext.ScrolledText(main_frame, width=100, height=30, 
                                                      bg='#0a0e1a', fg='#00ff41', 
                                                      font=('Consolas', 9), insertbackground='white')
        self.result_text.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
    
    def show_logo(self):
        self.logo_label.config(text=LOGO_ASCII)
    
    def log_message(self, message):
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
        self.root.update()
    
    def run_osint(self):
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showwarning("Error", "Ingresa un target válido")
            return
        
        self.result_text.delete(1.0, tk.END)
        self.run_button.config(state=tk.DISABLED)
        self.progress.start(10)
        
        thread = threading.Thread(target=self.execute_module, args=(target,))
        thread.start()
    
    def execute_module(self, target):
        module = self.module_var.get()
        try:
            self.log_message(f"[*] Iniciando {module} para: {target}\n")
            self.log_message("-" * 60)
            
            if "Email Leaks" in module:
                if '@' not in target:
                    self.log_message("[!] Error: Debes ingresar un email válido")
                else:
                    resultados = check_email_breaches(target)
                    self.log_message(f"\n[+] Servicios donde aparece {target}:")
                    for res in resultados:
                        self.log_message(f"  {res}")
            
            elif "Usuario Redes" in module:
                resultados = search_username_sherlock(target)
                self.log_message(f"\n[+] Redes sociales encontradas para '{target}':")
                for res in resultados:
                    self.log_message(f"  {res}")
            
            elif "theHarvester" in module:
                resultados = search_emails_and_domains(target)
                self.log_message(f"\n[+] Emails encontrados para dominio '{target}':")
                for res in resultados:
                    self.log_message(f"  {res}")
            
            self.log_message("\n[✔] Escaneo completado")
        
        except Exception as e:
            self.log_message(f"\n[!] Error: {str(e)}")
        
        finally:
            self.progress.stop()
            self.run_button.config(state=tk.NORMAL)
            self.log_message("\n" + "="*60)

if __name__ == "__main__":
    root = tk.Tk()
    app = FrameworkToolsMX(root)
    root.mainloop()
