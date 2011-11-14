#!/usr/bin/env python2

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer,SimpleJSONRPCRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os

__version__ = '0.1'

class RequestHandler(SimpleJSONRPCRequestHandler, SimpleHTTPRequestHandler):

    server_version = 'Schoolbell/' + __version__

    def do_POST(self):
        if self.path == '/RPC2':
            SimpleJSONRPCRequestHandler.do_POST(self)
        else:
            SimpleHTTPRequestHandler.do_POST(self)

if __name__ == '__main__':
    os.chdir('output')
    server = SimpleJSONRPCServer(('localhost', 8000), requestHandler=RequestHandler)
    server.register_function(lambda x: x, 'echo')
    server.register_function(lambda x: x[::-1], 'reverse')
    server.register_function(lambda x: x.upper(), 'uppercase')
    server.register_function(lambda x: x.lower(), 'lowercase')
    server.serve_forever()
