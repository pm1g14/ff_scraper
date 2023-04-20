from optional import Optional
from model import Event
from model import RowParameters
import calendar
import time
import json
import dataclasses

class NumUtils:

    def stringToFloat(value) -> Optional:
        try:
            return Optional.of(float(value))
        except ValueError:
            return Optional.empty
        

class JsonUtils:

    def convertListToJson(self, elements:list[RowParameters]) -> dict:
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        array = []
        for element in elements:
            array.append(element.__dict__)
        return Event(rows= array, timestamp= time_stamp).__dict__
    
class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            return super().default(o)