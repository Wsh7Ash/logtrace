# Results

## Environment

- OS: Windows 10 (MINGW64_NT-10.0-19044, MSYS2 shell)
- Runtime: CPython 3.14.3
- Dependency manager: pip 25.3 (virtualenv)
- Test runner: pytest 9.1.1

## Validation performed

- install: PASS - editable install into a fresh virtualenv, console script resolves
- unit tests: PASS - 2 passed
- integration tests: N/A - no network or service integration in this project
- lint: N/A - no linter configured for this project
- type check: N/A - no type checker configured for this project
- demo run: PASS - every documented command below exited 0

## Commands executed

```shell
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/python -m pytest -q
PYTHONPATH=src python3 -m logtrace.cli analyze --file examples/app.log
```

The host system interpreter is PEP 668 externally managed, so installation was
verified inside a virtualenv, which is the flow the README documents. Tests also
pass on a clean clone without installing, because `pyproject.toml` sets pytest's
`pythonpath` to `src`.

## Observed result

- test run: 2 passed
- demo output, exactly as captured in `results/demo-output.txt`:

```text
$ PYTHONPATH=src python3 -m logtrace.cli analyze --file examples/app.log
Errors: 2, Warnings: 1
[exit 0]
```

## Generated artifacts

- `results/demo-output.txt` - captured demo transcript

## Known limitations

See the Limitations section of [README.md](README.md).
