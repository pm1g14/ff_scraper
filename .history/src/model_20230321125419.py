from typing import Optional

@dataclass(frozen=True)
class RowParameters:

    date: str
    time: str
    currency: str
    event: str
    actual: Optional[float]
    forecast: Optional[float]
    previous: Optional[float]
