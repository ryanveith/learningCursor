"""Binary conversion (non-negative integers).

Input conventions:
  - Optional ``0b`` / ``0B`` prefix (e.g. ``0b1010`` or ``1010``).
  - Leading zeros in the digit string are allowed on input (``001010`` → 10).

Output conventions:
  - No ``0b`` prefix.
  - Minimal binary representation: no leading zeros (e.g. 15 → ``1111``, not ``00001111``).
    Only exception is zero itself, which is ``0``.
  - Cross-format conversions (e.g. hex → binary via the hub) use this same output
    rule because the value is normalized to an ``int`` first.
"""

from number_converter.errors import NumberFormatError

_BINARY_DIGITS = set("01")


def to_binary(n: int) -> str:
    if not isinstance(n, int) or isinstance(n, bool):
        raise NumberFormatError("Please enter a whole number.")
    if n < 0:
        raise NumberFormatError("Number must be non-negative.")

    # Minimal width: format(n, "b") never pads with leading zeros.
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

    # int(..., 2) ignores leading zeros in the digit string (e.g. "001010" → 10).
    return int(normalized, 2)
