# learningCursor

Me playing around and experimenting with Cursor for the goal of becoming more comfortable with it.

## Getting started

This folder is the local workspace for [learningCursor](https://github.com/ryanveith/learningCursor).

Use Cursor's chat and agent features here to try prompts, edits, and small experiments. Add notes or sample files as you go.

### Project layout

```
number_converter/     # Python package (CLI, hub, format modules)
tests/                # Unit tests
README.md
```

## Number converter

Interactive CLI to convert between Roman, Arabic (decimal), hexadecimal, and binary numerals.

```bash
python -m number_converter
```

The CLI asks for an **input format** (Roman, Arabic, Hex, or Binary), then an **output format**. Pick different formats for each step. On the output step, use `b` to go back and change the input format; use `q` to quit at any prompt.

Conversions are implemented in [`number_converter/converter.py`](number_converter/converter.py): input is parsed to an Arabic (integer) value, then formatted to the output type. Invalid input raises `NumberFormatError` (defined in [`number_converter/errors.py`](number_converter/errors.py)) with a format-specific message.

### Format modules

| Module | Role |
|--------|------|
| [`number_converter/formats/roman.py`](number_converter/formats/roman.py) | Roman numerals (1–3999) |
| [`number_converter/formats/hexadecimal.py`](number_converter/formats/hexadecimal.py) | Hex (non-negative; optional `0x` on input; uppercase output without prefix) |
| [`number_converter/formats/binary.py`](number_converter/formats/binary.py) | Binary (non-negative; optional `0b` on input; output without prefix) |

### Conversion notes

| From → To | Notes |
|-----------|--------|
| Roman → Arabic / Hex / Binary | Integers 1–3999 |
| Arabic → Roman | Integers 1–3999 |
| Arabic → Hex / Binary | Non-negative integers |
| Hex → Arabic | Optional `0x` prefix on input |
| Hex → Roman | Must decode to 1–3999 |
| Binary → Arabic | Optional `0b` prefix on input |
| Binary → Roman | Must decode to 1–3999 |

All other pairs (e.g. Hex ↔ Binary, Roman ↔ Binary) work automatically via the hub.

### Tests

From the repo root:

```bash
python -m unittest discover -s tests -v
```

Shorthand (also discovers `tests/` when run from repo root):

```bash
python -m unittest
python -m unittest -v
```

All tests are non-interactive. CLI behavior is covered in `tests/test_cli.py` using mocked input. To try the real menus, run `python -m number_converter` manually.
