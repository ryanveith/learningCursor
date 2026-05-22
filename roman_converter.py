"""Interactive Roman numeral converter."""

import roman


def print_menu() -> None:
    print()
    print("Roman Numeral Converter")
    print("  1 - Roman to Arabic")
    print("  2 - Arabic to Roman")
    print("  q - Quit")


def read_mode() -> str | None:
    while True:
        print_menu()
        choice = input("Choose an option (1, 2, or q): ").strip().lower()
        if choice in ("1", "2", "q"):
            return choice
        print("Please enter 1, 2, or q.")


def convert_roman_to_arabic() -> None:
    value = input("Enter a Roman numeral (e.g. XIV): ").strip()
    try:
        result = roman.to_arabic(value)
    except roman.RomanError as e:
        print(e)
        return
    print(f"Result: {result}")


def convert_arabic_to_roman() -> None:
    raw = input("Enter an Arabic number (1-3999): ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return
    try:
        result = roman.to_roman(n)
    except roman.RomanError as e:
        print(e)
        return
    print(f"Result: {result}")


def ask_convert_again() -> bool:
    while True:
        answer = input("Convert another? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main() -> None:
    while True:
        mode = read_mode()
        if mode == "q":
            print("Goodbye.")
            break
        while True:
            if mode == "1":
                convert_roman_to_arabic()
            else:
                convert_arabic_to_roman()
            if not ask_convert_again():
                break


if __name__ == "__main__":
    main()
