# Architecture

## Modules

- `logtrace.cli` - `click` group whose `analyze` command opens `--file`,
  counts lines containing `ERROR` / `WARN`, and prints the two numbers.

## Data flow

`--file` path -> read lines -> count `ERROR` and `WARN` lines -> `rich` console output.

## Design decisions

- Line-substring counting rather than a regular expression: it is
  predictable across formats and cannot silently mis-parse a timestamp.
- A single input file keeps the tool usable in pipelines and shell
  one-liners.

## Testing strategy

- Unit tests cover the core logic (line counting and CLI argument handling).
- CLI tests use `click.testing.CliRunner`, so command wiring is exercised
  without a real terminal or subprocess.
- `pyproject.toml` sets `pythonpath = ["src"]`, so `python3 -m pytest -q` works
  from a fresh clone.
