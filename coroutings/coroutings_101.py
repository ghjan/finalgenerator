#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 9/11/17 11:59 AM
"""


def receiver():
    while True:
        item = (yield)
        print('Got', item)


if __name__ == '__main__':
    recv = receiver()
    next(recv)  # Advance to first yield
    recv.send('Hello')
    recv.send('World')
