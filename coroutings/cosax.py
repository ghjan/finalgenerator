#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:47 PM
"""
from __future__ import absolute_import
import xml.sax


class MyHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target

    def startElement(self, name, attrs):
        self.target.send(('start', (name, attrs._attrs)))

    def characters(self, text):
        self.target.send(('text', text))

    def endElement(self, name):
        self.target.send(('end', name))


if __name__ == '__main__':
    xml.sax.parse("somefile.xml", MyHandler())
