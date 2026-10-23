from click.testing import CliRunner
from logtrace.cli import main


def test_analyze_counts(tmp_path):
    log = tmp_path / "app.log"
    log.write_text(
        "2026-10-23T00:00:00Z INFO started\n"
        "2026-10-23T00:00:01Z WARN slow\n"
        "2026-10-23T00:00:02Z ERROR boom\n"
    )
    res = CliRunner().invoke(main, ["analyze", "--file", str(log)])
    assert res.exit_code == 0, res.output
    assert "Errors: 1" in res.output
    assert "Warnings: 1" in res.output
