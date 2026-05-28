from flask import Flask, request, render_template_string
import sys
sys.path.append('..')
from core.scanner import OSINTScanner
from core.utils import save_report

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Framework Tools Mx</title></head>
<body style="background:#111;color:#0f0;font-family:monospace;">
    <h1>🔍 Framework Tools Mx - Web OSINT</h1>
    <form method="post">
        <input type="text" name="target" placeholder="Email, usuario o IP" size="40" required>
        <button type="submit">Buscar</button>
    </form>
    {% if results %}
        <pre>{{ results }}</pre>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form['target']
        scanner = OSINTScanner(target)
        data = scanner.run_all()
        save_report(data, target)
        return render_template_string(HTML, results=data)
    return render_template_string(HTML, results=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
