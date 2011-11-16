#!/usr/bin/env python2
import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Image import Image

from alarmwidget import AlarmWidget

class schoolbell:

    def __init__(self):
        pass

    def make_gui(self):
        header = HorizontalPanel(StyleName='header')
        header.add(Image('icons/bell.png', StyleName='logo'))
        header.add(Label('Schoolbell', StyleName='title'))

        alarms = AlarmWidget()

        panel = VerticalPanel()
        panel.add(header)
        panel.add(alarms.panel)

        RootPanel().add(panel)

    def onModuleLoad(self):
        self.make_gui()

if __name__ == '__main__':
    #pyjd.setup("http://127.0.0.1/output/schoolbell.html")
    pyjd.setup("schoolbell")
    app = schoolbell()
    app.onModuleLoad()
    pyjd.run()
