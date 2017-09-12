#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:47 PM
"""
from __future__ import absolute_import
import sys
import time
from corouting_decorator import coroutine


# pipeline source
def follow(thefile, target):
    thefile.seek(0, 2)  # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        target.send(line)


# pipeline filter
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)  # Receive a line

        if pattern in line:
            target.send(line)  # Send to next stage


# pipeline sink
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


# Broadcast to multiple targets
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)


if __name__ == '__main__':
    print(sys.argv)
    filename = "access-log"
    pattern = 'python'
    if len(sys.argv) > 1:
        filename = sys.argv[1] or "access-log"

    # Set up a processing pipe : tail -f | grep python
    logfile = open(filename)

    follow(logfile, broadcast([grep('python', printer()),
                               grep('exception', printer()),
                               grep('error', printer())])
           )
