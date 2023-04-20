from typing import Optional

from attr import dataclass

@dataclass(frozen=True)
class RowParameters:

    date: str
    time: str
    currency: str
    event: str
    actual: Optional[float]
    forecast: Optional[float]
    previous: Optional[float]
