import requests
import json
import subprocess

class OSINTScanner:
    def __init__(self, target):
        self.target = target
        self.results = {}

    def search_email(self):
        print(f"[+] Buscando email: {self.target}")
        # Simulación de búsqueda real (puedes agregar holehe, hunter.io, etc)
        self.results['email'] = f"Resultados para {self.target} - No leaks encontrados (demo)"

    def search_social(self):
        sites = ["twitter", "github", "instagram", "facebook"]
        found = []
        for site in sites:
            url = f"https://www.{site}.com/{self.target}"
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    found.append(f"{site}: {url}")
            except:
                pass
        self.results['social'] = found if found else ["No encontrado en redes comunes"]

    def geo_ip(self):
        try:
            r = requests.get(f"http://ip-api.com/json/{self.target}")
            data = r.json()
            self.results['ip_geo'] = f"{data.get('city')}, {data.get('country')} - Lat: {data.get('lat')}, Lon: {data.get('lon')}"
        except:
            self.results['ip_geo'] = "No se pudo geolocalizar"

    def run_all(self):
        if '@' in self.target:
            self.search_email()
        elif self.target.replace('.', '').isdigit():
            self.geo_ip()
        else:
            self.search_social()
        return self.results
