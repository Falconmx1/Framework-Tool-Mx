import subprocess

def search_emails_and_domains(domain):
    """Extrae emails/subdominios con theHarvester"""
    try:
        result = subprocess.run(
            ['theHarvester', '-d', domain, '-b', 'google', '--limit', '50'],
            capture_output=True, text=True, timeout=90
        )
        emails = []
        for line in result.stdout.split('\n'):
            if '@' in line and line.strip().count('@') == 1:
                emails.append(line.strip())
        return emails[:20] if emails else ["No se encontraron emails públicos"]
    except Exception as e:
        return [f"Error: {str(e)}"]
