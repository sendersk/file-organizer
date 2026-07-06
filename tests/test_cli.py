from pathlib import Path

from typer.testing import CliRunner

from file_organizer.main import app


runner = CliRunner()


def test_cli_dry_run(tmp_path: Path) -> None:
    """Should simulate file organization without moving files."""

    # Arrange
    file = tmp_path / "photo.jpg"
    file.write_text("data")

    # Act
    result = runner.invoke(app, [app, str(tmp_path), "--dry-run"])

    print(result.output)
    print(result.exception)

    # Assert
    assert result.exit_code == 0
    assert "[DRY-RUN]" in result.output
    assert file.exists()


def test_cli_organize_moves_files(tmp_path: Path) -> None:
    """Should move files when not in dry-run mode."""

    # Arrange
    file = tmp_path / "doc.pdf"
    file.write_text("data")

    # Act
    result = runner.invoke(app, [str(tmp_path)])

    print(result.output)
    print(result.exception)

    # Assert
    assert result.exit_code == 0
    assert "MOVED" in result.output or "Organization completed" in result.output
    assert not file.exists()