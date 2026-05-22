"""Binary conversion (non-negative integers, optional 0b prefix on input)."""

from errors import NumberFormatError

_BINARY_DIGITS = set("01")


def to_binary(n: int) -> str:
    if not isinstance(n, int) or isinstance(n, bool):
        raise NumberFormatError("Please enter a whole number.")
    if n < 0:
        raise NumberFormatError("Number must be non-negative.")

    return format(n, "b")


def from_binary(s: str) -> int:
    if not s or not s.strip():
        raise NumberFormatError("Invalid binary: empty input.")

    normalized = s.strip()
    if normalized.lower().startswith("0b"):
        normalized = normalized[2:]

    if not normalized:
        raise NumberFormatError(f"Invalid binary: {s!r}")

    if any(ch not in _BINARY_DIGITS for ch in normalized):
        raise NumberFormatError(f"Invalid binary: {s!r}")

    return int(normalized, 2)
