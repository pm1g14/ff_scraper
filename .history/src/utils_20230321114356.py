class NumUtils:

    def stringToFloat(self, value):
        try:
            converted = float(value)
            return converted
        except ValueError:
            return None