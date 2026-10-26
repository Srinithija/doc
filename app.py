from http.server import HTTPServer, BaseHTTPRequestHandler

def get_message():
    return "Hello from CI/CD Pipeline!"

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(get_message().encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), App)
    server.serve_forever()