#!/usr/bin/env python2
from pprint import pprint
from jsonrpc import ServiceProxy
from jsonrpc.proxy import JSONRPCException

s = ServiceProxy("http://localhost:8000/RPC2")

try:
    #print(s.reverse('foobar'))
    print(s.set([{u'duration': 2, u'time': u'15:40:00', u'weekdays': [0, 1, 2, 3, 4, 5]}]))
except JSONRPCException as (e):
    pprint(e.error)
