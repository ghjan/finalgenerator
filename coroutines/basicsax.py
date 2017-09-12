#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:47 PM
"""
from __future__ import absolute_import
import xml.sax


class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print("startElement", name)

    def endElement(self, name):
        print("endElement", name)

    def characters(self, text):
        print("characters", repr(text)[:40])


if __name__ == '__main__':
    xml.sax.parse("somefile.xml", MyHandler())
