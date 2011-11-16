from pyjamas.JSONService import JSONProxy

class SchoolbellRPC(JSONProxy):
    methods = [ 'get', 'add', 'remove', 'test', 'reverse' ]

    def __init__(self):
        JSONProxy.__init__(self, "/RPC2", SchoolbellRPC.methods)

class AlarmsGetHandler:
    def __init__(self, alarms):
        self.alarms = alarms

    def onRemoteResponse(self, response, request_info):
        print("Response: %s %s %s" % (request_info.method, request_info.handler, response))
        self.alarms.alarms = response
        self.alarms.widget.fill_table()

    def onRemoteError(self, code, errobj, request_info):
        message = errobj['message']
        if code != 0:
            print("HTTP error %d: %s" % (code, message))
        else:
            code = errobj['code']
            print("JSONRPC Error %s: %s" % (code, message))

class Alarms:
    def __init__(self, widget):
        self.widget = widget
        self.alarms = []
        self.remote = SchoolbellRPC()
        self.load()

    def load(self):
        # pylint: disable=E1101
        self.remote.get(AlarmsGetHandler(self))

    def save(self):
        pass

    def add(self, alarm):
        self.alarms.append(alarm)

    def remove(self, idx):
        self.alarms.pop(idx)

    def get(self, idx=None):
        if idx is not None:
            return self.alarms[idx]

        return self.alarms
