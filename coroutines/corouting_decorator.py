#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 4:05 PM
"""
import sys
import time


def follow(thefile):
    thefile.seek(0, 2)  # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield line


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def grep(pattern):
    print(("Looking for %s" % pattern))
    try:
        while True:
            # yield expression
            line = (yield)
            if line:
                if pattern in line:
                    print(("line:{}".format(line)))
    except GeneratorExit:
        print("Going away. Goodbye")


if __name__ == '__main__':
    print((sys.argv))
    filename = "access-log"
    pattern = 'python'
    if len(sys.argv) > 1:
        filename = sys.argv[1] or "access-log"
    if len(sys.argv) > 2:
        pattern = sys.argv[2] or 'python'
    # Set up a processing pipe : tail -f | grep python
    logfile = open(filename)
    loglines = follow(logfile)

    gen = grep(pattern)
    [gen.send(logline) for logline in loglines]
