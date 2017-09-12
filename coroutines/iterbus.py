# iterbus.py
#
# An example of incremental XML parsing with the ElementTree library
from timeit import timeit
from xml.etree.cElementTree import iterparse


def use_iterparse():
    for event, elem in iterparse("./coroutines/allroutes.xml", ('start', 'end')):
        if event == 'start' and elem.tag == 'buses':
            buses = elem
        elif event == 'end' and elem.tag == 'bus':
            busdict = dict((child.tag, child.text)
                           for child in elem)
            if (busdict['route'] == '22' and
                        busdict['direction'] == 'North Bound'):
                print("%(id)s,%(route)s,\"%(direction)s\",\"%(latitude)s,%(longitude)s" % busdict)

            buses.remove(elem)




if __name__ == '__main__':
    p = use_iterparse()
    print(timeit('p', 'from __main__ import p'))
