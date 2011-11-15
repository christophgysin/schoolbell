#!/usr/bin/env python2

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer,SimpleJSONRPCRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os, sys

__version__ = '0.1'

class RequestHandler(SimpleJSONRPCRequestHandler, SimpleHTTPRequestHandler):

    server_version = 'Schoolbell/' + __version__

    def do_POST(self):
        if self.path == '/RPC2':
            SimpleJSONRPCRequestHandler.do_POST(self)
        else:
            SimpleHTTPRequestHandler.do_POST(self)


class Alarms:
    def __init__(self):
        self.alarms = []
        self.load()

    def load(self):
        self.alarms = [
                { 'time': '08:00:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '08:50:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '08:55:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '09:45:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '10:00:00', 'weekdays': range(6), 'duration': 5 },
                { 'time': '10:50:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '10:55:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '11:45:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '13:00:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '13:50:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '13:55:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '14:45:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '14:50:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '14:45:00', 'weekdays': range(6), 'duration': 2 },
                { 'time': '14:50:00', 'weekdays': range(6), 'duration': 3 },
                { 'time': '15:40:00', 'weekdays': range(6), 'duration': 2 },
        ]

    def list(self):
        return self.alarms

    def add(self):
        pass

    def remove(self):
        pass

    def test(self):
        pass

if __name__ == '__main__':

    if(sys.argv[1]):
        os.chdir(sys.argv[1])
    server = SimpleJSONRPCServer(('localhost', 8000), requestHandler=RequestHandler)

    alarms = Alarms()
    server.register_function(alarms.list, 'list')
    server.register_function(alarms.add, 'add')
    server.register_function(alarms.remove, 'remove')
    server.register_function(alarms.test, 'test')

    server.serve_forever()
