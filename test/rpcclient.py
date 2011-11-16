#!/usr/bin/env python2

from jsonrpc import ServiceProxy
from jsonrpc.proxy import JSONRPCException

s = ServiceProxy("http://localhost:8000/RPC2")
#print(s.reverse('foobar'))

try:
    print(s.get())
except JSONRPCException as (e):
    print('error: %s' % e['error'])
