import selectors
import socket
from argparse import ArgumentParser
from dataclasses import dataclass, field
from datetime import datetime
from types import SimpleNamespace


@dataclass
class CommUnit:
    name: str
    host: str = "127.0.0.1"
    port: int = 65432


@dataclass
class User(CommUnit):
    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(self.name.encode())
            try:
                while True:
                    content = input().encode()
                    s.sendall(content)
            except KeyboardInterrupt:
                pass


@dataclass
class Message:
    sender: str
    content: str
    timestamp: datetime


@dataclass
class ChatServer(CommUnit):
    bufsize: int = 1024
    users: dict[tuple[str, int], str] = field(
        default_factory=dict, init=False, compare=False
    )
    messages: list[Message] = field(
        default_factory=list, init=False, repr=False, compare=False
    )

    def run(self) -> None:
        sel = selectors.DefaultSelector()
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((self.host, self.port))
        lsock.listen()
        lsock.setblocking(False)
        sel.register(lsock, selectors.EVENT_READ, data=None)

        bufsize = self.bufsize
        users = self.users
        try:
            while True:
                events = sel.select(timeout=None)
                for key, mask in events:
                    sock = key.fileobj
                    if (data := key.data) is None:
                        conn, addr = sock.accept()
                        conn.setblocking(False)
                        data = SimpleNamespace(addr=addr, inb=b"", outb=b"")
                        events = selectors.EVENT_READ | selectors.EVENT_WRITE
                        sel.register(conn, events, data=data)
                        username = conn.recv(bufsize).decode()
                        users[addr] = username
                        print(f"{username} entered the chat")
                    else:
                        if mask & selectors.EVENT_READ:
                            if recv_data := sock.recv(bufsize):
                                data.outb += recv_data
                            else:
                                print(f"{users[data.addr]} left the chat")
                                sel.unregister(sock)
                                sock.close()
                        if mask & selectors.EVENT_WRITE:
                            if recv_data := data.outb:
                                content = recv_data.decode()
                                print(f"{users[data.addr]}: {content}")
                                sent = sock.send(recv_data)
                                data.outb = recv_data[sent:]
        except KeyboardInterrupt:
            print("End of chat")
        finally:
            sel.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("name", type=str)
    parser.add_argument("--server", action="store_true")
    parser.add_argument("--host", default="127.0.0.1", type=str)
    parser.add_argument("--port", default=65432, type=int)
    parser.add_argument("--bufsize", default=1024, type=int)

    args = parser.parse_args()
    if args.server:
        server = ChatServer(args.name, args.host, args.port, args.bufsize)
        server.run()
    else:
        user = User(args.name, args.host, args.port)
        user.run()
