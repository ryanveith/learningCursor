"""Unit tests for roman numeral conversion."""

import unittest

from number_converter.errors import NumberFormatError
from number_converter.formats import roman


class TestArabicToRoman(unittest.TestCase):
    def test_subtractive_forms(self) -> None:
        self.assertEqual(roman.to_roman(4), "IV")
        self.assertEqual(roman.to_roman(9), "IX")
        self.assertEqual(roman.to_roman(14), "XIV")
        self.assertEqual(roman.to_roman(1994), "MCMXCIV")

    def test_boundaries(self) -> None:
        self.assertEqual(roman.to_roman(1), "I")
        self.assertEqual(roman.to_roman(3999), "MMMCMXCIX")

    def test_below_range(self) -> None:
        with self.assertRaises(NumberFormatError) as ctx:
            roman.to_roman(0)
        self.assertIn("1", str(ctx.exception))
        self.assertIn("3999", str(ctx.exception))

    def test_above_range(self) -> None:
        with self.assertRaises(NumberFormatError):
            roman.to_roman(4000)

    def test_non_integer(self) -> None:
        with self.assertRaises(NumberFormatError) as ctx:
            roman.to_roman(3.14)  # type: ignore[arg-type]
        self.assertIn("whole number", str(ctx.exception))

        with self.assertRaises(NumberFormatError) as ctx:
            roman.to_roman(True)
        self.assertIn("whole number", str(ctx.exception))


class TestRomanToArabic(unittest.TestCase):
    def test_known_values(self) -> None:
        self.assertEqual(roman.to_arabic("XIV"), 14)
        self.assertEqual(roman.to_arabic("MCMXCIV"), 1994)

    def test_case_insensitive_and_whitespace(self) -> None:
        self.assertEqual(roman.to_arabic("xiv"), 14)
        self.assertEqual(roman.to_arabic("  xiv  "), 14)

    def test_empty_and_whitespace(self) -> None:
        for value in ("", "   "):
            with self.subTest(value=repr(value)):
                with self.assertRaises(NumberFormatError):
                    roman.to_arabic(value)

    def test_unknown_letters(self) -> None:
        for value in ("abc", "X1V"):
            with self.subTest(value=value):
                with self.assertRaises(NumberFormatError):
                    roman.to_arabic(value)

    def test_non_canonical(self) -> None:
        for value in ("IIII", "VX"):
            with self.subTest(value=value):
                with self.assertRaises(NumberFormatError):
                    roman.to_arabic(value)


class TestRoundTripConversion(unittest.TestCase):
    def test_all_valid_range(self) -> None:
        for n in range(roman.MIN_ARABIC, roman.MAX_ARABIC + 1):
            with self.subTest(n=n):
                self.assertEqual(roman.to_arabic(roman.to_roman(n)), n)


if __name__ == "__main__":
    unittest.main()
