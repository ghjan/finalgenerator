# echogood2.py
#
# A working concurrent echo server

from socket import *
from pyos7 import *


def handle_client(client, addr):
    print("Connection from", addr)
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print("Client closed")


def server(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(("", port))
    sock.listen(1024)
    print("Server starting at port:{}".format(port))
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))


if __name__ == '__main__':
    sched = Scheduler()
    sched.new(server(45000))
    sched.mainloop()
