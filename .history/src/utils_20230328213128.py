from optional import Optional
from model import Event
from model import RowParameters
from model import MyEncoder
from typing import List
import calendar
import time
import json

class NumUtils:

    def stringToFloat(value) -> Optional:
        try:
            return Optional.of(float(value))
        except ValueError:
            return Optional.empty
        

class JsonUtils:

    def convertListToJson(self, elements:List[RowParameters]):
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        array = []
        for element in elements:
            array.append(element.__dict__)
        return json.dumps(Event(rows=array, timestamp=time_stamp).__dict__, cls=MyEncoder, indent=4)
