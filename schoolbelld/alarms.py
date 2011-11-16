
class AlarmsRPC:
    def __init__(self, alarms):
        self.alarms = alarms

    def get(self, idx=None):
        if idx is None:
            return self.alarms.alarms
        else:
            return self.alarms.alarms[idx]

    def test(self, duration):
        pass

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

    def add(self, alarm):
        pass

    def remove(self, alarm):
        pass
