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
    users: list[User]
    messages: list[Message] = field(init=False, default_factory=list)
