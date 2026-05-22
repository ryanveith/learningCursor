"""Interactive CLI for the number converter.

Flow: pick input format → pick output format → enter values (repeat until the
user chooses not to). All conversions delegate to ``converter.convert``; see
format modules for per-notation input/output rules (prefixes, leading zeros, etc.).
"""

from number_converter import converter
from number_converter.errors import NumberFormatError

_FORMATS = {
    "1": "roman",
    "2": "arabic",
    "3": "hex",
    "4": "binary",
}

_FORMAT_LABELS = {
    "roman": "Roman",
    "arabic": "Arabic",
    "hex": "Hex",
    "binary": "Binary",
}

_INPUT_PROMPTS = {
    "roman": "Enter a Roman numeral (e.g. XIV): ",
    "arabic": "Enter an Arabic number (decimal): ",
    "hex": "Enter a hexadecimal value (e.g. FF or 0xFF): ",
    "binary": "Enter a binary value (e.g. 1010 or 0b1010): ",
}


def print_format_menu(title: str, *, allow_back: bool) -> None:
    print()
    print(title)
    print("  1 - Roman")
    print("  2 - Arabic (decimal)")
    print("  3 - Hex")
    print("  4 - Binary")
    if allow_back:
        print("  b - Back")
    print("  q - Quit")


def read_format(title: str, *, allow_back: bool) -> str | None:
    """Return format key, None to quit, or 'back'."""
    valid = "1, 2, 3, 4, b, or q" if allow_back else "1, 2, 3, 4, or q"
    while True:
        print_format_menu(title, allow_back=allow_back)
        choice = input(f"Choose an option ({valid}): ").strip().lower()
        if choice == "q":
            return None
        if choice == "b" and allow_back:
            return "back"
        if choice in _FORMATS:
            return _FORMATS[choice]
        print(f"Please enter {valid}.")


def run_conversion(from_fmt: str, to_fmt: str) -> None:
    value = input(_INPUT_PROMPTS[from_fmt]).strip()
    try:
        result = converter.convert(from_fmt, to_fmt, value)
    except NumberFormatError as e:
        print(e)
        return
    print(f"Result: {result}")


def ask_convert_again() -> bool:
    while True:
        answer = input("Convert another with the same formats? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main() -> None:
    print("Number Converter")
    while True:
        # First step has no "back" — nothing to return to yet.
        from_fmt = read_format("Input format", allow_back=False)
        if from_fmt is None:
            print("Goodbye.")
            break

        to_fmt = read_format("Output format", allow_back=True)
        if to_fmt is None:
            print("Goodbye.")
            break
        if to_fmt == "back":
            continue

        if from_fmt == to_fmt:
            print(
                f"Input and output cannot both be {_FORMAT_LABELS[from_fmt]}. "
                "Choose different formats."
            )
            continue

        print(
            f"\nConverting {_FORMAT_LABELS[from_fmt]} "
            f"→ {_FORMAT_LABELS[to_fmt]}"
        )
        while True:
            run_conversion(from_fmt, to_fmt)
            if not ask_convert_again():
                break
