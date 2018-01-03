#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:47 PM
"""

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


# pipeline sink
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)


if __name__ == '__main__':
    print((sys.argv))
    filename = "access-log"
    if len(sys.argv) > 1:
        filename = sys.argv[1] or "access-log"

    # Set up a processing pipe : tail -f | grep python
    logfile = open(filename)

    follow(logfile, printer())
