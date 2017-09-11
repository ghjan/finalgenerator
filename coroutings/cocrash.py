# cocrash.py
#
# An example of hooking coroutines up in a way that might cause a potential
# crash.   Basically, there are two threads feeding data into the
# printer() coroutine.    

from cobroadcast import *
from cothread import threaded

'''
If you call send() on an already-executing
coroutine, your program will crash
For Ex:
Multiple threads sending data into
the same target coroutine
'''
print("-------1111-----")
p = printer()
target = broadcast([threaded(grep('foo', p)),
                    threaded(grep('bar', p))])

print("------2222------")
# Adjust the count if this doesn't cause a crash
for i in range(10):
    target.send("foo is nice\n")
    target.send("bar is bad\n")
print("------3333------")

del target
del p
