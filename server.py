from gevent.wsgi import WSGIServer
from denta import app

http_server = WSGIServer(('0.0.0.0', 80), app)
http_server.serve_forever()