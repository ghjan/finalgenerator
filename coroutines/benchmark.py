#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:47 PM
"""

import sys
import time
from corouting_decorator import coroutine
# Timing test
from timeit import timeit


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


class GrepHandler(object):
    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target

    def send(self, line):
        if self.pattern in line:
            self.target.send(line)


@coroutine
def null():
    while True: item = (yield)


if __name__ == '__main__':
    line = 'python is nice'
    p1 = grep('python', null())  # Coroutine
    p2 = GrepHandler('python', null())  # Object

    print((timeit("p1.send(line)",
                 "from __main__ import line,p1")))
    print((timeit("p2.send(line)",
                 "from __main__ import line,p2")))
    # 0.4181449390016496
    # 0.5490629359846935
