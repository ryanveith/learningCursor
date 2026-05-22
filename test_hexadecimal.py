"""Unit tests for hexadecimal conversion."""

import unittest

from errors import NumberFormatError

import hexadecimal


class TestArabicToHex(unittest.TestCase):
    def test_known_values(self) -> None:
        self.assertEqual(hexadecimal.to_hex(0), "0")
        self.assertEqual(hexadecimal.to_hex(10), "A")
        self.assertEqual(hexadecimal.to_hex(255), "FF")
        self.assertEqual(hexadecimal.to_hex(4096), "1000")

    def test_negative(self) -> None:
        with self.assertRaises(NumberFormatError):
            hexadecimal.to_hex(-1)

    def test_non_integer(self) -> None:
        with self.assertRaises(NumberFormatError) as ctx:
            hexadecimal.to_hex(3.14)  # type: ignore[arg-type]
        self.assertIn("whole number", str(ctx.exception))

        with self.assertRaises(NumberFormatError) as ctx:
            hexadecimal.to_hex(True)
        self.assertIn("whole number", str(ctx.exception))


class TestHexToArabic(unittest.TestCase):
    def test_known_values(self) -> None:
        self.assertEqual(hexadecimal.from_hex("FF"), 255)
        self.assertEqual(hexadecimal.from_hex("a"), 10)

    def test_prefix_and_whitespace(self) -> None:
        self.assertEqual(hexadecimal.from_hex("0xFF"), 255)
        self.assertEqual(hexadecimal.from_hex("0Xff"), 255)
        self.assertEqual(hexadecimal.from_hex("  0x10  "), 16)

    def test_empty_and_whitespace(self) -> None:
        for value in ("", "   "):
            with self.subTest(value=repr(value)):
                with self.assertRaises(NumberFormatError):
                    hexadecimal.from_hex(value)

    def test_invalid_digits(self) -> None:
        for value in ("xyz", "0xG1", "12 34"):
            with self.subTest(value=value):
                with self.assertRaises(NumberFormatError):
                    hexadecimal.from_hex(value)


class TestRoundTripConversion(unittest.TestCase):
    def test_spot_check(self) -> None:
        for n in (0, 1, 255, 256, 4096, 1_000_000):
            with self.subTest(n=n):
                self.assertEqual(hexadecimal.from_hex(hexadecimal.to_hex(n)), n)

    def test_modest_range(self) -> None:
        for n in range(1001):
            with self.subTest(n=n):
                self.assertEqual(hexadecimal.from_hex(hexadecimal.to_hex(n)), n)


if __name__ == "__main__":
    unittest.main()
