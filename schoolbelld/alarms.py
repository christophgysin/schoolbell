import json
from pprint import pprint

class AlarmsRPC:
    def __init__(self, alarms):
        self.alarms = alarms

    def get(self, idx=None):
        if idx is None:
            return self.alarms.alarms
        else:
            return self.alarms.alarms[idx]

    def set(self, alarms):
        self.alarms.alarms = alarms
        self.alarms.save()

class Alarms:
    config = 'alarms.json.conf'

    def __init__(self):
        self.alarms = []
        self.load()

    def load(self):
        f = open(Alarms.config, 'r')
        self.alarms = json.load(f)
        f.close()

    def save(self):
        f = open(Alarms.config, 'w')
        json.dump(self.alarms, f)
        f.close()
