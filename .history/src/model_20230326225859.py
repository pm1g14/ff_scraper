from optional import Optional

from attr import dataclass
from typing import List

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

    def __init__(self, rows: List[RowParameters], timestamp: str):
        self.__rows =  rows
        self.__timestamp = timestamp
    