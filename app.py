import http.server
import socketserver
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("Received request from", self.client_address[0])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("You've hit " + os.uname().nodename + "\n", "utf-8"))

print("Captain server starting...")

# Use 0.0.0.0 to listen on all available interfaces
with socketserver.TCPServer(("0.0.0.0", 8001), Handler) as httpd:
    httpd.serve_forever()
