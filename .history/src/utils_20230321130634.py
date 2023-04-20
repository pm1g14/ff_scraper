from optional import Optional


class NumUtils:

    def stringToFloat(value) -> Optional:
        try:
            return Optional.of(float(value))
        except ValueError:
            return Optional.empty