"""Hub for converting between number formats via Arabic (integer).

Every conversion parses input to ``int``, then formats that integer for the
target type. Implications:

  - Cross-format pairs (hex ↔ binary, roman ↔ hex, etc.) need no separate logic.
  - Output width/prefix rules come from the *target* format module (e.g. hex →
    binary yields minimal binary with no leading zeros, not a digit-for-digit
    translation of the hex string).
  - Range limits apply when encoding: Roman output requires 1–3999 even if the
    input format allowed a wider value (e.g. hex ``2710`` → Roman raises).

To add a format: register a parser in ``_TO_ARABIC`` and a formatter in
``_FROM_ARABIC``.
"""

from collections.abc import Callable

from number_converter.errors import NumberFormatError
from number_converter.formats import binary, hexadecimal, roman

# Parsers: string in a given format → Arabic (int).
_TO_ARABIC: dict[str, Callable[[str], int]] = {
    "roman": roman.to_arabic,
    "hex": hexadecimal.from_hex,
    "binary": binary.from_binary,
}

# Formatters: Arabic (int) → string in a given format (minimal width / prefixes per module).
_FROM_ARABIC: dict[str, Callable[[int], str]] = {
    "roman": roman.to_roman,
    "hex": hexadecimal.to_hex,
    "binary": binary.to_binary,
}


def _parse_arabic(s: str) -> int:
    try:
        return int(s.strip())
    except ValueError:
        raise NumberFormatError("Please enter a whole number.") from None


def _format_arabic(n: int) -> str:
    return str(n)


_TO_ARABIC["arabic"] = _parse_arabic
_FROM_ARABIC["arabic"] = _format_arabic


def to_arabic(fmt: str, value: str) -> int:
    try:
        return _TO_ARABIC[fmt](value)
    except KeyError:
        raise ValueError(f"Unknown format: {fmt!r}") from None


def from_arabic(fmt: str, n: int) -> str:
    try:
        return _FROM_ARABIC[fmt](n)
    except KeyError:
        raise ValueError(f"Unknown format: {fmt!r}") from None


def convert(from_fmt: str, to_fmt: str, value: str) -> str:
    """Parse ``value`` as ``from_fmt``, then format the integer as ``to_fmt``."""
    return from_arabic(to_fmt, to_arabic(from_fmt, value))
