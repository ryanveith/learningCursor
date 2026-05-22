"""Unit tests for binary conversion."""

import unittest

from number_converter.errors import NumberFormatError
from number_converter.formats import binary


class TestArabicToBinary(unittest.TestCase):
    def test_known_values(self) -> None:
        self.assertEqual(binary.to_binary(0), "0")
        self.assertEqual(binary.to_binary(10), "1010")
        self.assertEqual(binary.to_binary(255), "11111111")
        self.assertEqual(binary.to_binary(16), "10000")

    def test_negative(self) -> None:
        with self.assertRaises(NumberFormatError):
            binary.to_binary(-1)

    def test_non_integer(self) -> None:
        with self.assertRaises(NumberFormatError) as ctx:
            binary.to_binary(3.14)  # type: ignore[arg-type]
        self.assertIn("whole number", str(ctx.exception))

        with self.assertRaises(NumberFormatError) as ctx:
            binary.to_binary(True)
        self.assertIn("whole number", str(ctx.exception))


class TestBinaryToArabic(unittest.TestCase):
    def test_known_values(self) -> None:
        self.assertEqual(binary.from_binary("11111111"), 255)
        self.assertEqual(binary.from_binary("1010"), 10)

    def test_prefix_and_whitespace(self) -> None:
        self.assertEqual(binary.from_binary("0b1010"), 10)
        self.assertEqual(binary.from_binary("0B11111111"), 255)
        self.assertEqual(binary.from_binary("  0b10000  "), 16)

    def test_empty_and_whitespace(self) -> None:
        for value in ("", "   "):
            with self.subTest(value=repr(value)):
                with self.assertRaises(NumberFormatError):
                    binary.from_binary(value)

    def test_invalid_digits(self) -> None:
        for value in ("102", "2", "10 10"):
            with self.subTest(value=value):
                with self.assertRaises(NumberFormatError):
                    binary.from_binary(value)


class TestRoundTripConversion(unittest.TestCase):
    def test_spot_check(self) -> None:
        for n in (0, 1, 255, 256, 4096, 1_000_000):
            with self.subTest(n=n):
                self.assertEqual(binary.from_binary(binary.to_binary(n)), n)

    def test_modest_range(self) -> None:
        for n in range(1001):
            with self.subTest(n=n):
                self.assertEqual(binary.from_binary(binary.to_binary(n)), n)


if __name__ == "__main__":
    unittest.main()
