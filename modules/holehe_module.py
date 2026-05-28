import subprocess
import json

def check_email_breaches(email):
    """Usa holehe para verificar leaks"""
    try:
        result = subprocess.run(
            ['holehe', email, '--no-color', '--format', 'json'],
            capture_output=True, text=True, timeout=30
        )
        if result.stdout:
            data = json.loads(result.stdout)
            servicios = []
            for site, info in data.items():
                if info.get('rateLimit') == False and info.get('exists'):
                    servicios.append(f"✅ {site}")
            return servicios if servicios else ["No se encontraron cuentas asociadas"]
        return ["Error: No se pudo consultar holehe"]
    except Exception as e:
        return [f"Error: {str(e)}"]
