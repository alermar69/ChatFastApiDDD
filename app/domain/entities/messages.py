import uuid
from dataclasses import dataclass, field
from datetime import datetime

from domain.entities.base import BaseEntity
from domain.values.messages import Text, Title


@dataclass
class Message(BaseEntity):
    text: Text

    oid: str = field(
        default_factory=lambda: str(uuid.uuid4()),
        kw_only=True,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(),
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: "Message") -> bool:
        return self.oid == other.oid


@dataclass
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    oid: str = field(
        default_factory=lambda: str(uuid.uuid4()),
        kw_only=True,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(),
        kw_only=True,
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: "Chat") -> bool:
        return self.oid == other.oid

    def add_message(self, message: Message):
        self.messages.add(message)
