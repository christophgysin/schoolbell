#!/usr/bin/env python2

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer,SimpleJSONRPCRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler

class RequestHandler(SimpleJSONRPCRequestHandler, SimpleHTTPRequestHandler):

    server_version = 'JSONRPCtest/0.1'

    def do_POST(self):
        if self.path == '/RPC2':
            SimpleJSONRPCRequestHandler.do_POST(self)
        else:
            SimpleHTTPRequestHandler.do_POST(self)


#server = SimpleJSONRPCServer(('localhost', 8000))
server = SimpleJSONRPCServer(('localhost', 8000), requestHandler=RequestHandler)

server.register_function(lambda x: x[::-1], 'reverse')
server.serve_forever()
