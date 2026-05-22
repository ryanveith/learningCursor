"""Hexadecimal conversion (non-negative integers, optional 0x prefix on input)."""

from errors import NumberFormatError

_HEX_DIGITS = set("0123456789ABCDEFabcdef")


def to_hex(n: int) -> str:
    if not isinstance(n, int) or isinstance(n, bool):
        raise NumberFormatError("Please enter a whole number.")
    if n < 0:
        raise NumberFormatError("Number must be non-negative.")

    return format(n, "X")


def from_hex(s: str) -> int:
    if not s or not s.strip():
        raise NumberFormatError("Invalid hexadecimal: empty input.")

    normalized = s.strip()
    if normalized.lower().startswith("0x"):
        normalized = normalized[2:]

    if not normalized:
        raise NumberFormatError(f"Invalid hexadecimal: {s!r}")

    if any(ch not in _HEX_DIGITS for ch in normalized):
        raise NumberFormatError(f"Invalid hexadecimal: {s!r}")

    return int(normalized, 16)
