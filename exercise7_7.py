import socket
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    name: str


@dataclass
class Message:
    sender: User
    content: str
    timestamp: datetime


@dataclass
class ChatServer:
    users: dict[socket._RetAddress, User]
    host: str = "127.0.0.1"
    port: int = 65432
    bufsize: int = 1024
    messages: list[Message] = field(
        default_factory=list, init=False, repr=False, compare=False
    )
