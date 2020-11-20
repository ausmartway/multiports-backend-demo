from threading import Thread
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT1 = 8087
PORT2 = 8088

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        print("the request is from:",self.client_address)
        print("the request is served by :",self.server)
        print("URL:",url)
        if url == "hello":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Echo to "+str(self.client_address)+ " from "+str(self.server.server_address), "utf-8"))
        else:
            self.send_response(404)
        
            

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def serve_on_port(port):
    server = ThreadingHTTPServer(("",port), Handler)
    server.serve_forever()

Thread(target=serve_on_port, args=[PORT1]).start()
serve_on_port(PORT2)