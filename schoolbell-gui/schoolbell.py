#!/usr/bin/env python2
import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Image import Image
from pyjamas.ui.Button import Button

from alarmwidget import AlarmWidget
from testwidget import TestWidget

class schoolbell:

    def __init__(self):
        pass

    def make_gui(self):
        panel = VerticalPanel(StyleName='mainpanel')
        panel.add(self.make_header())
        panel.add(self.make_tabs())
        RootPanel().add(panel)

    def make_header(self):
        header = HorizontalPanel(StyleName='header')
        header.add(Image('icons/bell.png', StyleName='logo'))
        header.add(Label('Schoolbell', StyleName='title'))
        return header

    def make_tabs(self):
        tabs = TabPanel()
        tabs.add(self.make_alarm_widget(), 'alarms')
        tabs.add(self.make_test_widget(), 'test')
        tabs.selectTab(0)
        return tabs

    def make_alarm_widget(self):
        alarms = AlarmWidget()
        return alarms.panel

    def make_test_widget(self):
        test = TestWidget()
        return test.panel

    def onModuleLoad(self):
        self.make_gui()

if __name__ == '__main__':
    #pyjd.setup("http://127.0.0.1/output/schoolbell.html")
    pyjd.setup("schoolbell")
    app = schoolbell()
    app.onModuleLoad()
    pyjd.run()
