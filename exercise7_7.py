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
    pass


@dataclass
class Message:
    sender: User
    content: str
    timestamp: datetime


@dataclass
class ChatServer(CommUnit):
    bufsize: int = 1024
    messages: list[Message] = field(
        default_factory=list, init=False, repr=False, compare=False
    )
