import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b"I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison")

httpd = socketserver.TCPServer(('', 5000), Handler)
httpd.serve_forever()
