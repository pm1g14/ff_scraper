from optional import Optional
import json

class NumUtils:

    def stringToFloat(value) -> Optional:
        try:
            return Optional.of(float(value))
        except ValueError:
            return Optional.empty
        

class JsonUtils:

    def convertListToJson(self, list:list):
        array = []
        for element in list:
            array.append(element.__dict__)
        return json.dumps(array)