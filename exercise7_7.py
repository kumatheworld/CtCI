import socket
from argparse import ArgumentParser
from dataclasses import dataclass, field
from datetime import datetime


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
            while True:
                content = input().encode()
                s.sendall(content)


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
        bufsize = self.bufsize
        messages = self.messages
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(bufsize)
                    if not data:
                        break
                    content = data.decode()
                    try:
                        username = self.users[addr]
                    except KeyError:
                        self.users[addr] = content
                    else:
                        timestamp = datetime.now()
                        message = Message(username, content, timestamp)
                        messages.append(message)


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
