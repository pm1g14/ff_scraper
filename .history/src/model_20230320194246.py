@dataclass(frozen=True)
class RowParameters:

    date: str
    time: str
    currency: str
    impact: str
    event: str
    actual: float
    forecast: float
    previous: float