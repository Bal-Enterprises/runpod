from http.server import BaseHTTPRequestHandler, HTTPServer
import os

url = os.environ["BAL_ENT_SERVER_URL"]
port = os.environ["BAL_ENT_SERVER_PORT"]


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("do_get")
        if self.path == "/get":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found")

    def do_POST(self):
        if self.path == "/post":
            content_length = int(
                self.headers["Content-Length"]
            )  # Get the length of the post data
            post_data = self.rfile.read(content_length)  # Read the post data
            print(f"Received POST data: {post_data.decode('utf-8')}")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"POST request received successfully!")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not found")


if __name__ == "__main__":
    port = int(port)
    server_address = ("", port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server listening on port {port}")
    httpd.serve_forever()
