#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: david
@file: bogus.py
@time: 9/11/17 4:33 PM
"""


def countdown(n):
    print(("Counting down from", n))

    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1
        print(("countdown received:{}".format(newvalue)))


if __name__ == '__main__':
    # gener = countdown(10)
    # next(gener)
    # for i in range(0, 10):
    #     print(gener.send(i))

    # Notice how a value got "lost" in the iteration protocol
    c = countdown(5)
    for n in c:
        print(n)
        if n == 5:
            c.send(3)
