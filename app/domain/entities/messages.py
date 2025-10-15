import uuid
from dataclasses import dataclass, field

from domain.values.messages import Text


@dataclass
class Message:
    oid: str = field(
        default_factory=lambda: str(uuid.uuid4()),
        kw_only=True,
    )
    text: Text
