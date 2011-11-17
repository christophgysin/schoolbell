from pyjamas.JSONService import JSONProxy

class SchoolbellRPC(JSONProxy):
    methods = [ 'get', 'set', 'add', 'remove', 'test', 'reverse' ]

    def __init__(self):
        JSONProxy.__init__(self, "/RPC2", SchoolbellRPC.methods)

