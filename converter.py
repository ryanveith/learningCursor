"""Hub for converting between number formats via Arabic (integer)."""

from collections.abc import Callable

import binary
import hexadecimal
import roman
from errors import NumberFormatError

_TO_ARABIC: dict[str, Callable[[str], int]] = {
    "roman": roman.to_arabic,
    "hex": hexadecimal.from_hex,
    "binary": binary.from_binary,
}

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
    return from_arabic(to_fmt, to_arabic(from_fmt, value))
