from rpc import SchoolbellRPC

class AlarmsGetHandler(object):
    def __init__(self, alarms):
        self.alarms = alarms

    def onRemoteResponse(self, response, request_info):
        self.alarms.alarms = response
        self.alarms.widget.fill_table()

    def onRemoteError(self, code, errobj, request_info):
        message = errobj['message']
        if code != 0:
            print("HTTP error %d: %s" % (code, message))
        else:
            code = errobj['code']
            print("JSONRPC Error %s: %s" % (code, message))

class Alarms(object):
    def __init__(self, widget):
        self.widget = widget
        self.alarms = []
        self.remote = SchoolbellRPC()
        self.load()

    def load(self):
        # pylint: disable=E1101
        self.remote.get(AlarmsGetHandler(self))

    def save(self):
        # pylint: disable=E1101
        self.remote.set(self.alarms)

    def add(self, alarm):
        self.alarms.append(alarm)

    def remove(self, idx):
        self.alarms.pop(idx)

    def get(self, idx=None):
        if idx is not None:
            return self.alarms[idx]

        return self.alarms
