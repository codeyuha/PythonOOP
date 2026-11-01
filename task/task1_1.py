"""Module for string length checking."""


class StringLengthChecker:
    """Class to validate and check string lengths."""

    def __init__(self, min_length: int = 1, max_length: int = 255):
        """
        Initialize the checker.

        Args:
            min_length: Minimum allowed length (inclusive).
            max_length: Maximum allowed length (inclusive).
        """
        if min_length < 0:
            raise ValueError("min_length must be >= 0")
        if max_length < min_length:
            raise ValueError("max_length must be >= min_length")

        self.min_length = min_length
        self.max_length = max_length

    def check(self, value: str) -> bool:
        """Return True if the string length is within bounds."""
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        return self.min_length <= len(value) <= self.max_length

    def validate(self, value: str) -> str:
        """Return the value if valid, otherwise raise ValueError."""
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")

        length = len(value)
        if length < self.min_length:
            raise ValueError(
                f"String too short: {length} < {self.min_length}"
            )
        if length > self.max_length:
            raise ValueError(
                f"String too long: {length} > {self.max_length}"
            )
        return value

    def get_length(self, value: str) -> int:
        """Return the length of the string."""
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        return len(value)


if __name__ == "__main__":
    checker = StringLengthChecker(min_length=3, max_length=10)

    samples = ["hi", "hello", "this is too long"]
    for s in samples:
        print(f"{s!r:20} -> length={checker.get_length(s):2}, "
              f"valid={checker.check(s)}")
