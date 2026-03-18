#!/usr/bin/env python3
"""Simple server that serves the presentation and saves live edits to edits.json."""
import http.server, json, os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)

    def do_POST(self):
        if self.path == '/save-edits':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            with open(os.path.join(DIR, 'edits.json'), 'w') as f:
                f.write(body.decode())
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        if '/save-edits' not in str(args):
            super().log_message(format, *args)

print(f"\n  Presentation: http://localhost:{PORT}/presentation.html\n")
http.server.HTTPServer(('', PORT), Handler).serve_forever()
