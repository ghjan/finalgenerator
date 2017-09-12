#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 3:05 PM
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


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            # yield statement
            yield line


def grep2(pattern):
    print("Looking for %s" % pattern)
    while True:
        # yield expression
        line = (yield)
        if line:
            if pattern in line:
                print("line:{}".format(line))


if __name__ == '__main__':
    print(sys.argv)
    filename = "access-log"
    pattern = 'python'
    grep_no = 0
    if len(sys.argv) > 1:
        filename = sys.argv[1] or "access-log"
    if len(sys.argv) > 2:
        pattern = sys.argv[2] or 'python'
    if len(sys.argv) > 3:
        grep_no = sys.argv[3] or 0

    # Set up a processing pipe : tail -f | grep python
    logfile = open(filename)
    loglines = follow(logfile)
    grep_method = grep if not grep_no else grep2
    if not grep_no:
        pylines = grep_method(pattern, loglines)
        if pylines:
            for line in pylines:
                if line:
                    print("in pylines:{}".format(line))
    else:
        gen = grep_method(pattern)
        # This advances execution to the location of the first yield expression.
        next(gen) or gen.send(None)
        [gen.send(logline) for logline in loglines]
        # Pull results out of the processing pipeline
