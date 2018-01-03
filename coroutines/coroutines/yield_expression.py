# coding=utf-8

def h():
    print('Wen Chuan', end=' ')
    m = yield 5  # Fighting!
    print(m)
    d = yield 12
    print('We are together!')


c = h()
next(c)  # 相当于c.send(None)
c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'
