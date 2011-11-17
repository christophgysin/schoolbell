from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.Button import Button

from rpc import SchoolbellRPC

class TestHandler:
    def __init__(self, duration):
        self.duration = duration
        self.rpc = SchoolbellRPC()

    def func(self):
        # pylint: disable=E1101
        getSelectedValue = lambda widget: widget.getValue(widget.getSelectedIndex())
        duration = getSelectedValue(self.duration)
        self.rpc.test(duration)

class TestWidget:
    def __init__(self):
        self.panel = self.make_panel()

    def make_panel(self):
        duration = ListBox()
        duration.setVisibleItemCount(1)
        choices = [ 1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 30, 40, 50, 60 ]
        for seconds in choices:
            duration.addItem(
                    '%ds' % seconds if seconds < 60 else '%dm' % (seconds / 60),
                    seconds)
        duration.setSelectedIndex(2)

        button = Button('test')
        handler = TestHandler(duration)
        button.addClickListener(handler.func)

        panel = HorizontalPanel()
        panel.add(duration)
        panel.add(button)
        return panel
