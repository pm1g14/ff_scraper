from optional import Optional


class NumUtils:

    def stringToFloat(value) -> Optional[float]:
        try:
            return Optional.of(float(value))
        except ValueError:
            return Optional.empty