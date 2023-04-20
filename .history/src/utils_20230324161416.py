from optional import Optional
from model import Event
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

    def convertListToJson(list:list) -> dict:
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        array = []
        for element in list:
            array.append(element.__dict__)
        return Event(rows= json.dumps(array), timestamp= time_stamp).__dict__