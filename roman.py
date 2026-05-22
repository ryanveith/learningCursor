"""Roman numeral conversion (1-3999, standard subtractive notation)."""

MIN_ARABIC = 1
MAX_ARABIC = 3999

VALUES = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

SYMBOL_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
VALID_SYMBOLS = set(SYMBOL_VALUES)


class RomanError(ValueError):
    """Raised when Roman numeral input or Arabic range is invalid."""


def to_roman(n: int) -> str:
    if not isinstance(n, int) or isinstance(n, bool):
        raise RomanError("Please enter a whole number.")
    if n < MIN_ARABIC or n > MAX_ARABIC:
        raise RomanError(f"Number must be between {MIN_ARABIC} and {MAX_ARABIC}.")

    result: list[str] = []
    remaining = n
    for value, symbol in VALUES:
        while remaining >= value:
            result.append(symbol)
            remaining -= value
    return "".join(result)


def to_arabic(s: str) -> int:
    if not s or not s.strip():
        raise RomanError("Invalid Roman numeral: empty input.")

    normalized = s.strip().upper()
    if any(ch not in VALID_SYMBOLS for ch in normalized):
        raise RomanError(f"Invalid Roman numeral: {s!r}")

    total = 0
    prev = 0
    for ch in reversed(normalized):
        value = SYMBOL_VALUES[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    if total < MIN_ARABIC or total > MAX_ARABIC:
        raise RomanError(f"Invalid Roman numeral: {s!r}")

    if to_roman(total) != normalized:
        raise RomanError(f"Invalid Roman numeral: {s!r}")

    return total
