#!/usr/bin/env python2
import pyjd # dummy in pyjs

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.Image import Image
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.ListBox import ListBox
from pyjamas.JSONService import JSONProxy

class schoolbell:

    def make_gui(self):
        self.status = Label()
        self.text_area = TextArea()
        self.text_area.setText("""foobar""")
        self.text_area.setCharacterWidth(80)
        self.text_area.setVisibleLines(8)

        self.method_list = ListBox()
        self.method_list.setName("hello")
        self.method_list.setVisibleItemCount(1)
        for method in self.methods:
            self.method_list.addItem(method)
        self.method_list.setSelectedIndex(0)

        method_panel = HorizontalPanel()
        method_panel.add(Label("Remote string method to call: "))
        method_panel.add(self.method_list)
        method_panel.setSpacing(8)

        self.button_cgi = Button("Send to CGI", self)
        self.button_server = Button("Send to Server", self)

        buttons = HorizontalPanel()
        buttons.add(self.button_cgi)
        buttons.add(self.button_server)
        buttons.setSpacing(8)

        panel = VerticalPanel()

        header = HorizontalPanel()
        header.add(Image('icons/bell.png', StyleName='logo'))
        header.add(Label('Schoolbell', StyleName='title'))
        panel.add(header)
#            HTML("""
#            <div id="header">
#                <img id="logo" src="icons/bell.png"/>
#                <span id="title">Schoolbell</span>
#            </div>
#            """))
        panel.add(self.text_area)
        panel.add(method_panel)
        panel.add(buttons)
        panel.add(self.status)

        RootPanel().add(panel)


    def onModuleLoad(self):
        self.methods = [ "Echo", "Reverse", "UPPERCASE", "lowercase", "nonexistent" ]
        self.remote_cgi = EchoServiceCGI()
        self.remote_server = EchoServiceServer()
        self.make_gui()


    def onClick(self, sender):
        self.status.setText("Waiting for response...")
        method = self.methods[self.method_list.getSelectedIndex()]
        text = self.text_area.getText()

        if sender == self.button_cgi:
            remote = self.remote_cgi
        elif sender == self.button_server:
            remote = self.remote_server

        if method == "Echo":
            id = remote.echo(text, self)
        elif method == "Reverse":
            id = remote.reverse(text, self)
        elif method == "UPPERCASE":
            id = remote.uppercase(text, self)
        elif method == "lowercase":
            id = remote.lowercase(text, self)
        elif method == "nonexistent":
            id = remote.nonexistant(text, self)

    def onRemoteResponse(self, response, request_info):
        self.status.setText(response)

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
            self.status.setText("HTTP error %d: %s" % 
                                (code, message))
        else:
            code = errobj['code']
            self.status.setText("JSONRPC Error %s: %s" %
                                (code, message))


class EchoServiceCGI(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/services/EchoService.py", ["echo", "reverse", "uppercase", "lowercase", "nonexistant"])

class EchoServiceServer(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "http://localhost:8080", ["echo", "reverse", "uppercase", "lowercase", "nonexistant"])

if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    #pyjd.setup("http://127.0.0.1/output/schoolbell.html")
    pyjd.setup("schoolbell")
    app = schoolbell()
    app.onModuleLoad()
    pyjd.run()
