import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        # Ensure browsers don't cache the old headers during testing
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

# Kill any other servers on port 8000 before running this
with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("Server running on http://localhost:8000")
    httpd.serve_forever()