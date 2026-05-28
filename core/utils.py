import os
import json
from datetime import datetime

def save_report(data, target, format='txt'):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{target}_{timestamp}.{format}"
    os.makedirs("reports", exist_ok=True)
    
    if format == 'json':
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        with open(filename, 'w') as f:
            for k, v in data.items():
                f.write(f"{k.upper()}: {v}\n")
    print(f"[+] Reporte guardado: {filename}")
