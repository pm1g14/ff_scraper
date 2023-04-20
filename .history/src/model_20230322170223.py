from optional import Optional

from attr import dataclass

@dataclass(frozen=True)
class RowParameters:

    date: str
    time: str
    currency: str
    event: str
    actual: Optional
    forecast: Optional
    previous: Optional

@dataclass(frozen=True)
class Event:
    rows: list
    timestamp: str