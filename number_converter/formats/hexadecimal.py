"""Hexadecimal conversion (non-negative integers).

Input conventions:
  - Optional ``0x`` / ``0X`` prefix (e.g. ``0xFF`` or ``FF``).
  - Leading zeros in the digit string are allowed on input (``00FF`` → 255).

Output conventions:
  - Uppercase A–F, no ``0x`` prefix.
  - Minimal width: no leading zeros (e.g. 15 → ``F``, not ``0F``).
    Only exception is zero itself, which is ``0``.
"""

from number_converter.errors import NumberFormatError

_HEX_DIGITS = set("0123456789ABCDEFabcdef")


def to_hex(n: int) -> str:
    if not isinstance(n, int) or isinstance(n, bool):
        raise NumberFormatError("Please enter a whole number.")
    if n < 0:
        raise NumberFormatError("Number must be non-negative.")

    # Uppercase, minimal width (no leading zeros except n == 0 → "0").
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

    # int(..., 16) ignores leading zeros (e.g. "00FF" → 255).
    return int(normalized, 16)
