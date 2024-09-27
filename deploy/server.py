import http.server
import socketserver
from urllib.parse import urlparse
import os

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Check if the path is not root and doesn't have a file extension
        if path != "/" and not os.path.splitext(path)[1]:
            # Add .html to the path
            self.path = path + ".html"

        # Call the parent class method to complete the request
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    PORT = 8000
    Handler = MyHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
