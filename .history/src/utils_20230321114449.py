from typing import Optional


class NumUtils:

    def stringToFloat(self, value):
        try:
            converted = float(value)
            return Optional.of(converted)
        except ValueError:
            return Optional.empty()