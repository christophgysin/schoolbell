from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.CheckBox import CheckBox
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.Image import Image
from pyjamas.ui.FlexTable import FlexTable
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.RowFormatter import RowFormatter
from pyjamas.ui.Grid import Grid
from pyjamas import DOM

from alarms import Alarms

class AlarmWidget:
    weekday_name = { 0: 'Mo', 1: 'Di', 2: 'Mi', 3: 'Do', 4: 'Fr', 5: 'Sa', 6: 'So' }

    def __init__(self):
        self.alarms = Alarms(self)
        self.make_table()
        self.fill_table()
        self.status = Label()
        self.panel = self.make_panel()

    def make_panel(self):
        message = Label(
            'The configuration has been changed.\n'
            'You must apply the changes in order for them to take effect.')
        DOM.setStyleAttribute(message.getElement(), "whiteSpace", 'pre')

        msgbox = Grid(1, 2, StyleName='changes')
        msgbox.setWidget(0, 0, Image('icons/exclam.png'))
        msgbox.setWidget(0, 1, message)
        msgbox.getCellFormatter().setStyleName(0, 0, 'changes-image')
        msgbox.getCellFormatter().setStyleName(0, 1, 'changes-text')

        button = Button('apply changes')
        button.addClickListener(self.apply_clicked)

        self.changes = VerticalPanel()
        self.changes.setHorizontalAlignment('right')
        self.changes.setVisible(False)
        self.changes.add(msgbox)
        self.changes.add(button)

        panel = VerticalPanel()
        panel.setSpacing(10)
        panel.add(self.table)
        panel.add(self.status)
        panel.add(self.changes)

        return panel

    def make_table(self):
        self.table = FlexTable(StyleName='alarms')
        self.table.setBorderWidth(1)
        self.make_header()
        self.make_footer()

    def make_header(self):
        headers = [ 'Time', 'Days', 'Duration' ]
        for col, text in enumerate(headers):
            self.table.setText(0, col, text)
            self.table.getCellFormatter().setStyleName(0, col, 'tablecell header')

    def make_footer(self):
        self.time = {}

        self.time['hour'] = ListBox()
        self.time['hour'].setVisibleItemCount(1)
        for hour in range(24):
            self.time['hour'].addItem('%02d' % hour)
        self.time['hour'].setSelectedIndex(12)

        self.time['minute'] = ListBox()
        self.time['minute'].setVisibleItemCount(1)
        for minute in range(0, 60, 5):
            self.time['minute'].addItem('%02d' % minute)
        self.time['minute'].setSelectedIndex(0)

        time_panel = HorizontalPanel()
        time_panel.setVerticalAlignment('center')
        time_panel.add(self.time['hour'])
        time_panel.add(Label(':'))
        time_panel.add(self.time['minute'])
        self.table.setWidget(1, 0, time_panel)

        weekdays_panel = HorizontalPanel()
        weekdays_panel.setSpacing(5)
        self.weekdays = {}
        for i in range(7):
            self.weekdays[i] = CheckBox(AlarmWidget.weekday_name[i])
            self.weekdays[i].setChecked(i < 6)
            weekdays_panel.add(self.weekdays[i])
        self.table.setWidget(1, 1, weekdays_panel)

        self.duration = ListBox()
        self.duration.setVisibleItemCount(1)
        choices = [ 1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 30, 40, 50, 60 ]
        for seconds in choices:
            self.duration.addItem(
                    '%ds' % seconds if seconds < 60 else '%dm' % (seconds / 60),
                    seconds)
        self.duration.setSelectedIndex(2)
        self.table.setWidget(1, 2, self.duration)

        image = Image('icons/plus.png')
        image.setTitle('add');
        image.addClickListener(self.plus_clicked)
        self.table.setWidget(1, 3, image)

        for col in range(4):
            self.table.getCellFormatter().setStyleName(1, col, 'tablecell noborder')

    def fill_table(self):
        for idx, alarm in enumerate(self.alarms.get()):
            self.add(alarm['time'], alarm['weekdays'], alarm['duration'])

    def add(self, time, weekdays=range(5), duration=3):
        row = self.table.getRowCount()-1
        self.table.insertRow(row)
        self.table.setText(row, 0, time)
        weekdays_str = []
        for weekday in weekdays:
            weekdays_str.append(AlarmWidget.weekday_name[weekday])

        self.table.setText(row, 1, ', '.join(weekdays_str))
        self.table.setText(row, 2, str(duration) + 's')

        image = Image('icons/x.png')
        image.setTitle('delete');
        image.addClickListener(lambda x: self.x_clicked(row-1))
        self.table.setWidget(row, 3, image)

        for col in range(3):
            self.table.getCellFormatter().setStyleName(row, col, 'tablecell')
        self.table.getCellFormatter().setStyleName(row, 3, 'tablecell noborder')

    def remove(self, idx):
        if idx >= 0 and idx < self.table.getRowCount()-2:
            #self.status.setText('removing idx: %d' % idx)
            self.table.removeRow(idx+1)
        else:
            #self.status.setText('tried to remove idx: %d' % idx)
            pass

    def plus_clicked(self):
        self.changes.setVisible(True)
        getSelectedValue = lambda widget: widget.getValue(widget.getSelectedIndex())
        hour = getSelectedValue(self.time['hour'])
        minute = getSelectedValue(self.time['minute'])
        time = '%02d:%02d:%02d' % ( hour, minute, 0 )
        weekdays = [ i for i in range(7) if self.weekdays[i].isChecked() ]
        duration = getSelectedValue(self.duration)

        self.add(time, weekdays, duration)
        self.alarms.add({'time': time, 'weekdays': weekdays, 'duration': duration})

    def x_clicked(self, idx):
        self.changes.setVisible(True)
        self.remove(idx)
        #self.alarms.remove(idx)

    def apply_clicked(self):
        self.alarms.save()
        self.changes.setVisible(False)
