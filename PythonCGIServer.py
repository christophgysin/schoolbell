#!/usr/bin/env python2
# run this in the output/ subdirectory to start a simple
# cgi server

from CGIHTTPServer import CGIHTTPRequestHandler
import BaseHTTPServer
import SimpleHTTPServer
import os

CGIHTTPRequestHandler.cgi_directories = ['/services']

if __name__ == '__main__':
    os.chdir('output')
    SimpleHTTPServer.test(CGIHTTPRequestHandler, BaseHTTPServer.HTTPServer)
