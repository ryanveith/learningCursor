"""Unit tests for the converter hub (all format pairs via Arabic)."""

import unittest

import converter
import roman
from errors import NumberFormatError


class TestConvertPairs(unittest.TestCase):
    def test_roman_to_hex(self) -> None:
        self.assertEqual(converter.convert("roman", "hex", "XIV"), "E")
        self.assertEqual(converter.convert("roman", "hex", "MCMXCIV"), "7CA")

    def test_hex_to_roman(self) -> None:
        self.assertEqual(converter.convert("hex", "roman", "FF"), "CCLV")
        self.assertEqual(converter.convert("hex", "roman", "0x7CA"), "MCMXCIV")

    def test_roman_to_arabic(self) -> None:
        self.assertEqual(converter.convert("roman", "arabic", "XIV"), "14")

    def test_arabic_to_hex(self) -> None:
        self.assertEqual(converter.convert("arabic", "hex", "255"), "FF")

    def test_hex_to_arabic(self) -> None:
        self.assertEqual(converter.convert("hex", "arabic", "FF"), "255")

    def test_arabic_to_roman(self) -> None:
        self.assertEqual(converter.convert("arabic", "roman", "14"), "XIV")

    def test_arabic_to_binary(self) -> None:
        self.assertEqual(converter.convert("arabic", "binary", "10"), "1010")

    def test_binary_to_arabic(self) -> None:
        self.assertEqual(converter.convert("binary", "arabic", "11111111"), "255")

    def test_roman_to_binary(self) -> None:
        self.assertEqual(converter.convert("roman", "binary", "XIV"), "1110")

    def test_binary_to_roman(self) -> None:
        self.assertEqual(converter.convert("binary", "roman", "11111111"), "CCLV")

    def test_binary_out_of_roman_range(self) -> None:
        with self.assertRaises(NumberFormatError):
            converter.convert("binary", "roman", "0")

    def test_invalid_roman(self) -> None:
        with self.assertRaises(NumberFormatError):
            converter.convert("roman", "hex", "IIII")

    def test_invalid_hex(self) -> None:
        with self.assertRaises(NumberFormatError):
            converter.convert("hex", "roman", "xyz")

    def test_hex_out_of_roman_range(self) -> None:
        with self.assertRaises(NumberFormatError):
            converter.convert("hex", "roman", "0")

        with self.assertRaises(NumberFormatError) as ctx:
            converter.convert("hex", "roman", "2710")
        self.assertIn("1", str(ctx.exception))
        self.assertIn("3999", str(ctx.exception))


class TestToFromArabic(unittest.TestCase):
    def test_to_arabic_roman(self) -> None:
        self.assertEqual(converter.to_arabic("roman", "XIV"), 14)

    def test_from_arabic_hex(self) -> None:
        self.assertEqual(converter.from_arabic("hex", 255), "FF")

    def test_from_arabic_binary(self) -> None:
        self.assertEqual(converter.from_arabic("binary", 10), "1010")


class TestRoundTripViaHub(unittest.TestCase):
    def test_roman_hex_spot_check(self) -> None:
        for value in ("I", "XIV", "MCMXCIV", "MMMCMXCIX"):
            with self.subTest(value=value):
                self.assertEqual(
                    converter.convert("hex", "roman", converter.convert("roman", "hex", value)),
                    value,
                )

    def test_modest_range(self) -> None:
        for n in range(1, 101):
            roman_value = roman.to_roman(n)
            with self.subTest(n=n, roman=roman_value):
                self.assertEqual(
                    converter.convert(
                        "hex",
                        "roman",
                        converter.convert("roman", "hex", roman_value),
                    ),
                    roman_value,
                )


if __name__ == "__main__":
    unittest.main()
