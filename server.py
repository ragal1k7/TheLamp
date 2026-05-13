from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Лампа</title>
    <style>
        body {
            background-color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        #lamp {
            font-size: 200px;
            user-select: none;
        }
        #hint {
            position: fixed;
            bottom: 30px;
            color: #555;
            font-size: 14px;
            text-align: center;
        }
        a {
            color: #888;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div id="lamp">🔌</div>
    <div id="hint">
        Перейдите на <a href="/lamp_on">/lamp_on</a> чтобы включить<br>
        или на <a href="/lamp_off">/lamp_off</a> чтобы выключить
    </div>
    <script>
        const lamp = document.getElementById('lamp');
        function update() {
            if (window.location.pathname === '/lamp_on') {
                lamp.textContent = '💡';
                document.body.style.backgroundColor = '#1a1a00';
                document.title = 'Лампа включена';
            } else {
                lamp.textContent = '🔌';
                document.body.style.backgroundColor = 'black';
                document.title = 'Лампа выключена';
            }
        }
        window.addEventListener('popstate', update);
        update();
    </script>
</body>
</html>'''

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/lamp_on', '/lamp_off']:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML.encode())
        else:
            self.send_response(404)
            self.end_headers()

print('Сервер запущен: http://localhost:8080')
HTTPServer(('localhost', 8080), Handler).serve_forever()