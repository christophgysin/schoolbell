from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer,SimpleJSONRPCRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler

class RequestHandler(SimpleJSONRPCRequestHandler, SimpleHTTPRequestHandler):

    server_version = 'Schoolbell/0.1'

    def do_POST(self):
        # pylint: disable=E1101
        if self.path == '/RPC2':
            SimpleJSONRPCRequestHandler.do_POST(self)
        else:
            SimpleHTTPRequestHandler.do_POST(self)
