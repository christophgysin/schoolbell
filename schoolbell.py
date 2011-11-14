#!/usr/bin/env python2
import pyjd # dummy in pyjs

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.Image import Image
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.RowFormatter import RowFormatter
from pyjamas.JSONService import JSONProxy

class Alarms:
    def __init__(self):
        self.weekday_name = { 0: 'Mo', 1: 'Di', 2: 'Mi', 3: 'Do', 4: 'Fr', 5: 'Sa', 6: 'So' }
        self.make_alarm_table()
        self.fill_alarm_table()
        self.status = Label('status')

    def get_alarms(self):
        return [
                { 'time': '08:00:00', 'weekdays': [ 0, 1, 2, 3, 4, 5 ], 'duration': 3 },
                { 'time': '08:55:00', 'weekdays': [ 0, 1, 2, 3, 4, 5 ], 'duration': 3 },
                { 'time': '09:05:00', 'weekdays': [ 0, 1, 2, 3, 4, 5 ], 'duration': 3 },
                { 'time': '10:00:00', 'weekdays': [ 0, 1, 2, 3, 4, 5 ], 'duration': 5 },
                { 'time': '13:00:00', 'weekdays': [ 0, 1, 2, 3, 4 ], 'duration': 3 },
                { 'time': '13:50:00', 'weekdays': [ 0, 1, 2, 3, 4 ], 'duration': 3 },
                { 'time': '14:00:00', 'weekdays': [ 0, 1, 2, 3, 4 ], 'duration': 3 },
        ]

    def make_alarm_table(self):
        self.table = FlexTable(StyleName='alarms')
        self.table.setBorderWidth(1)
        self.table.setText(0, 0, 'Time')
        self.table.setText(0, 1, 'Days')
        self.table.setText(0, 2, 'Duration')
        for col in range(3):
            self.table.getCellFormatter().setStyleName(0, col, 'tablecell header')

        button = HorizontalPanel()
        button.setSpacing(5)
        image = Image('icons/plus.png')
        image.addClickListener(self.plus_clicked)
        button.add(image)
        self.table.setWidget(1, 3, button)
        for col in range(4):
            self.table.getCellFormatter().setStyleName(1, col, 'tablecell noborder')

    def plus_clicked(self):
        self.status.setText('button clicked')

    def fill_alarm_table(self):
        for idx, alarm in enumerate(self.get_alarms()):
            self.add_alarm(alarm['time'], alarm['weekdays'], alarm['duration'])

    def add_alarm(self, time, weekdays=range(5), duration=3):
        row = self.table.getRowCount()-1
        self.table.insertRow(row)
        self.table.setText(row, 0, time)
        weekdays_str = []
        for weekday in weekdays:
            weekdays_str.append(self.weekday_name[weekday])

        self.table.setText(row, 1, ', '.join(weekdays_str))
        self.table.setText(row, 2, str(duration) + 's')

        buttons = HorizontalPanel()
        buttons.setSpacing(5)
        buttons.add(Image('icons/e.png'))
        buttons.add(Image('icons/x.png'))
        self.table.setWidget(row, 3, buttons)

        for col in range(3):
            self.table.getCellFormatter().setStyleName(row, col, 'tablecell')
        self.table.getCellFormatter().setStyleName(row, 3, 'tablecell noborder')

class schoolbell:

    def __init__(self):
        pass

    def make_gui(self):
        header = HorizontalPanel(StyleName='header')
        header.add(Image('icons/bell.png', StyleName='logo'))
        header.add(Label('Schoolbell', StyleName='title'))

        alarms = Alarms()
        alarm_panel = VerticalPanel()
        #alarm_panel.add(Label('Alarms:'))
        alarm_panel.add(alarms.table)
        alarm_panel.add(alarms.status)

        panel = VerticalPanel()
        panel.add(header)
        panel.add(alarm_panel)

        RootPanel().add(panel)

    def onModuleLoad(self):
        self.methods = [ "Echo", "Reverse", "UPPERCASE", "lowercase", "nonexistent" ]
        self.remote_rpc = EchoServiceRPC()
        self.make_gui()


    def onClick(self, sender):
        pass

    def onRemoteResponse(self, response, request_info):
        pass

    def onRemoteError(self, code, errobj, request_info):
        # onRemoteError gets the HTTP error code or 0 and
        # errobj is an jsonrpc 2.0 error dict:
        #     {
        #       'code': jsonrpc-error-code (integer) ,
        #       'message': jsonrpc-error-message (string) ,
        #       'data' : extra-error-data
        #     }
        message = errobj['message']
        if code != 0:
            print("HTTP error %d: %s" % (code, message))
        else:
            code = errobj['code']
            print("JSONRPC Error %s: %s" % (code, message))


class EchoServiceRPC(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/RPC2", ["echo", "reverse", "uppercase", "lowercase", "nonexistant"])


if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    #pyjd.setup("http://127.0.0.1/output/schoolbell.html")
    pyjd.setup("schoolbell")
    app = schoolbell()
    app.onModuleLoad()
    pyjd.run()
