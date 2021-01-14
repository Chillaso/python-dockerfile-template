import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests

KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER')
KAFKA_BOOTSTRAP_PORT = os.getenv('KAFKA_BOOTSTRAP_PORT')
KAFKA_AUTO_OFFSET = os.getenv('KAFKA_AUTO_OFFSET')
KAFKA_CONSUMER_TIMEOUT = os.getenv('KAFKA_CONSUMER_TIMEOUT')
KAFKA_TOPICS = os.getenv('KAFKA_TOPICS')

print(KAFKA_BOOTSTRAP_SERVER)
print(KAFKA_BOOTSTRAP_PORT)
print(KAFKA_AUTO_OFFSET)
print(KAFKA_CONSUMER_TIMEOUT)
print(KAFKA_TOPICS)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer(("localhost", 8080), MyServer)
    print("Server started http://%s:%s" % ("localhost", "8080"))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
