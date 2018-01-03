# coprocess.py
#
# An example of running a coroutine in a subprocess connected by a pipe
try:
    import pickle
except:
    import pickle as pickle
import traceback

from .coroutine import *


@coroutine
def sendto(f):
    try:
        while True:
            item = (yield)
            if item is not None:
                pickle.dump(item, f)
                if f:
                    f.flush()
            else:
                f.close()
                break
    except StopIteration:
        f.close()
    except Exception as e:
        print(e)

        traceback.print_exc()


def recvfrom(f, target):
    item = None
    try:
        while True:
            item = pickle.load(f)
            target.send(item)
    except EOFError:
        target.close()
    except StopIteration:
        return
    except Exception as e:
        print(e)


# Example use
if __name__ == '__main__':
    import xml.sax
    from .cosax import EventHandler
    from .buses import *

    import subprocess

    p = subprocess.Popen(['python', 'busproc.py'],
                         stdin=subprocess.PIPE)

    xml.sax.parse("allroutes.xml",
                  EventHandler(
                      buses_to_dicts(
                          sendto(p.stdin))))
