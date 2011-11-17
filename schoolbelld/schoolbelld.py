#!/usr/bin/env python2

import os, sys
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

from requesthandler import RequestHandler
from alarms import Alarms, AlarmsRPC

def test(self, duration):
    print('test! (%ds)' % duration)

if __name__ == '__main__':

    if(sys.argv[1]):
        os.chdir(sys.argv[1])
    server = SimpleJSONRPCServer(('localhost', 8000), requestHandler=RequestHandler)

    alarms = Alarms()
    rpc = AlarmsRPC(alarms)
    server.register_function(rpc.get, 'get')
    server.register_function(rpc.set, 'set')
    server.register_function(test, 'test')

    server.serve_forever()
