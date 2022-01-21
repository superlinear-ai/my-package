"""Test My Package CLI."""

from typer.testing import CliRunner

from my_package.cli import app

runner = CliRunner()


def test_say() -> None:
    """Test that the say command works as expected."""
    message = "Hello world"
    result = runner.invoke(app, ["--message", message])
    assert result.exit_code == 0
    assert message in result.stdout
