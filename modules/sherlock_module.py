import subprocess

def search_username_sherlock(username):
    """Busca username en redes con Sherlock"""
    try:
        result = subprocess.run(
            ['sherlock', username, '--print-found', '--timeout', '5'],
            capture_output=True, text=True, timeout=60
        )
        lines = result.stdout.split('\n')
        encontrados = []
        for line in lines:
            if 'https://' in line and '[' in line:
                encontrados.append(line.strip())
        return encontrados if encontrados else ["No encontrado en redes sociales"]
    except Exception as e:
        return [f"Error ejecutando Sherlock: {str(e)}"]
