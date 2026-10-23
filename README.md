# logtrace

Count ERROR and WARN lines in a log file with one command.

## Problem

When a service misbehaves the first question is crude: how many errors, and did it get worse? Tail, grep and eyeballing work until the log is long or the format drifts. `logtrace analyze` gives a count you can read in a second and repeat across files.

## Features

- Counts lines containing `ERROR` and `WARN` in one pass
- No regular expressions and no log-format assumptions
- Works on any line-oriented log, from syslog to application output
- Ships `examples/app.log` so the README command reproduces exactly
- Captured run committed at `results/demo-output.txt`

## Example

```shell
PYTHONPATH=src python3 -m logtrace.cli analyze --file examples/app.log
```

```text
Errors: 2, Warnings: 1
```

A captured run of the same command is committed at `results/demo-output.txt`.

## Architecture

One module, `src/logtrace/cli.py`:

- a `click` group with a single `analyze` command taking `--file`
- the command reads the file once and counts lines containing the two level
  substrings
- output is rendered with `rich`

## Requirements

- Python 3.10 or newer
- `click`, `rich`

## Installation

```shell
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows activate the environment with `.venv/Scripts/activate` instead.

## Quick start

```shell
PYTHONPATH=src python3 -m logtrace.cli analyze --file examples/app.log

# after `pip install -e .`:
logtrace analyze --file /var/log/app.log
```

## Configuration

No configuration file. The only input is `--file`; the level substrings are the literals `ERROR` and `WARN`.

## Testing

```shell
python3 -m pytest -q
```

Tests run from a clean clone: `pyproject.toml` sets pytest's `pythonpath` to
`src`, so no install step is needed to run them.

## Project structure

```text
logtrace/
|-- src/logtrace/
|   `-- cli.py            # analyze command
|-- tests/
|   |-- test_log.py       # import check
|   `-- test_cli.py       # counting behaviour end to end
|-- examples/app.log      # fixture used by the README command
|-- results/              # captured demo output
|-- docs/                 # ARCHITECTURE.md, USAGE.md
`-- pyproject.toml
```

## Limitations

- Substring matching, case sensitive: `error` in lowercase is not counted.
- Counts lines, not occurrences - five errors on one line count as one.
- No time windows, rates or trend detection, and no JSON output.
- The whole file is read into memory, so multi-gigabyte logs are out of
  scope.

## Roadmap

- `--level` flag for arbitrary level names
- Per-minute rate table and simple spike highlighting
- `--json` output for CI
- Multi-file and glob input

## Security notes

Reads only the file you name and prints counters. No network access, no state written to disk. Log files often contain personal data: the tool prints counts, not lines.

## License

MIT - see [LICENSE](LICENSE).
