"""Shared errors for number format conversion."""


class NumberFormatError(ValueError):
    """Invalid input or out-of-range value for a specific notation.

    Message text is format-specific (Roman, hex, binary, etc.) so the CLI can
    show one ``except`` block while still giving useful feedback.
    """
