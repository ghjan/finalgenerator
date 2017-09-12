# echoserver.py
#
# A concurrent echo server using coroutines

from pyos8 import *
from socket import *


def handle_client(client, addr):
    print("Connection from", addr)
    while True:
        data = yield Recv(client, 65536)
        if not data:
            break
        yield Send(client, data)
    print("Client closed")
    client.close()


def server(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(("", port))
    sock.listen(5)
    print("Server starting at port:{}".format(port))
    while True:
        client, addr = yield Accept(sock)
        yield NewTask(handle_client(client, addr))


if __name__ == '__main__':
    sched = Scheduler()
    sched.new(server(45000))
    sched.mainloop()
