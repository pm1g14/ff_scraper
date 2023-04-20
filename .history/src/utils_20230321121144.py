from typing import Optional


class NumUtils:

    def stringToFloat(self, value):
        try:
            converted = float(value)
            return converted)
        except ValueError:
            raise ValueError("Passed value {} cannot be converted to float", value)