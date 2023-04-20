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

class Event:
    rows: list[RowParameters]
    timestamp: str