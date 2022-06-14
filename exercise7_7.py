import socket
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
