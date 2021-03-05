from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn
import time


def hello_world_app(environ, start_response):
    start_response('200 OK', [])
    path_info = environ['PATH_INFO']
    print(path_info)
    time.sleep(3)
    yield f"Hello World{path_info}\n".encode("utf8")


class ThreadedWSGIServer(ThreadingMixIn, WSGIServer):
    pass


http = make_server('', 8000, hello_world_app, server_class=ThreadedWSGIServer)
http.serve_forever()
