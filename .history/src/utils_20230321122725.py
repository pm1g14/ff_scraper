from typing import Optional


class NumUtils:

    def stringToFloat(self, value):
        try:
            return float(value)
            )
        except ValueError:
            raise ValueError("Passed value {} cannot be converted to float", value)