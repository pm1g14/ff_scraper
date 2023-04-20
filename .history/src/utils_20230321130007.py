from typing import Optional


class NumUtils:

    def stringToFloat(self, value) -> Optional[float]:
        try:
            return Optional.of(float(value))
    
        except ValueError:
            return Optional.empty