#!/usr/bin/env python2
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer,SimpleJSONRPCRequestHandler
server = SimpleJSONRPCServer(('localhost', 8000))
server.register_function(lambda x: x[::-1], 'reverse')
server.serve_forever()
