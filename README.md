# learningCursor

Me playing around and experimenting with Cursor for the goal of becoming more comfortable with it.

## Getting started

This folder is the local workspace for [learningCursor](https://github.com/ryanveith/learningCursor).

Use Cursor's chat and agent features here to try prompts, edits, and small experiments. Add notes or sample files as you go.

## Number converter

Interactive CLI to convert between Roman, Arabic (decimal), hexadecimal, and binary numerals.

```bash
python number_converter.py
```

The CLI asks for an **input format** (Roman, Arabic, Hex, or Binary), then an **output format**. Pick different formats for each step. On the output step, use `b` to go back and change the input format; use `q` to quit at any prompt.

Conversions are implemented in [`converter.py`](converter.py): input is parsed to an Arabic (integer) value, then formatted to the output type. Invalid input raises `NumberFormatError` (defined in [`errors.py`](errors.py)) with a format-specific message.

### Format modules

| Module | Role |
|--------|------|
| [`roman.py`](roman.py) | Roman numerals (1–3999) |
| [`hexadecimal.py`](hexadecimal.py) | Hex (non-negative; optional `0x` on input; uppercase output without prefix) |
| [`binary.py`](binary.py) | Binary (non-negative; optional `0b` on input; output without prefix) |

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

```bash
python -m unittest
python -m unittest -v
```
