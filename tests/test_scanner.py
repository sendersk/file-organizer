import pytest

from pathlib import Path

from file_organizer.scanner import FileScanner


def test_scanner_finds_files(tmp_path: Path) -> None:
    """Should find all files in directory tree."""

    # Arrange
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("test")
    file2.write_text("test")

    subdir = tmp_path / "subdir"
    subdir.mkdir()
    file3 = subdir / "file3.txt"
    file3.write_text("test")

    scanner = FileScanner(tmp_path)

    # Act
    result = scanner.scan()

    # Assert
    assert file1 in result
    assert file2 in result
    assert file3 in result
    assert len(result) == 3


def test_scanner_ignores_directories(tmp_path: Path) -> None:
    """Should return only files, not directories."""

    (tmp_path / "dir1").mkdir()
    file1 = tmp_path / "file1.txt"
    file1.write_text("test")

    scanner = FileScanner(tmp_path)

    result = scanner.scan()

    assert all(path.is_file() for path in result)


def test_scanner_empty_directory(tmp_path: Path) -> None:
    """Should return empty list for empty directory."""

    scanner = FileScanner(tmp_path)

    result = scanner.scan()

    assert result == []


def test_scanner_non_existing_path() -> None:
    """Should raise FileNotFoundError for invalid path."""

    scanner = FileScanner(Path("this_path_does_not_exist"))

    with pytest.raises(FileNotFoundError):
        scanner.scan()