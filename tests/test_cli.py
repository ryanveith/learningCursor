"""Automated CLI tests (mocked input; no human interaction required)."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from number_converter.cli import main


class TestCliAutomated(unittest.TestCase):
    def _run_main(self, inputs: list[str]) -> str:
        with patch("number_converter.cli.input", side_effect=inputs):
            buf = io.StringIO()
            with redirect_stdout(buf):
                main()
            return buf.getvalue()

    def test_quit_on_first_prompt(self) -> None:
        out = self._run_main(["q"])
        self.assertIn("Goodbye.", out)

    def test_roman_to_hex_conversion_then_quit(self) -> None:
        out = self._run_main(["1", "3", "XIV", "n", "q"])
        self.assertIn("Converting Roman → Hex", out)
        self.assertIn("Result: E", out)
        self.assertIn("Goodbye.", out)

    def test_same_format_rejected(self) -> None:
        out = self._run_main(["1", "1", "q"])
        self.assertIn("cannot both be Roman", out)
        self.assertNotIn("Result:", out)

    def test_back_on_output_format(self) -> None:
        out = self._run_main(["1", "b", "q"])
        self.assertIn("Input format", out)
        self.assertIn("Goodbye.", out)

    def test_invalid_input_then_valid_choice(self) -> None:
        out = self._run_main(["9", "q"])
        self.assertIn("Please enter", out)
        self.assertIn("Goodbye.", out)


if __name__ == "__main__":
    unittest.main()
