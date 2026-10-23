# Usage

## Commands

| Command | Purpose |
|---|---|
| `logtrace analyze --file FILE` | Print `ERROR` and `WARN` line counts for `FILE` |
| `logtrace --help` | Show available commands |

## Examples

```shell
logtrace analyze --file examples/app.log
logtrace analyze --file /var/log/syslog
```

## Exit codes

- `0` - the command completed successfully
- `1` - click reported a usage error (missing or invalid option)
- `2` - click could not parse the command line

## Output

Output is rendered with `rich` and written to stdout, so it can be captured or
piped. Example runs are committed under `results/`.
