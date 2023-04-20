from typing import Optional


class NumUtils:

    def stringToFloat(self, value):
        try:
            converted = float(value)
            return converted)
        except ValueError:
            return 0.0