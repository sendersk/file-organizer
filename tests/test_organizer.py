from pathlib import Path

from file_organizer.models import RulesConfig
from file_organizer.organizer import FileOrganizer


def create_config() -> RulesConfig:
    """Create sample configuration for organizer tests."""

    return RulesConfig(
        categories={
            "Images": [".jpg", ".png"],
            "Documents": [".pdf", ".docx"],
            "Videos": [".mp4"],
            "Other": [],
        }
    )


def test_should_recognize_image_file() -> None:
    """Should classify JPG files as Images."""

    organizer = FileOrganizer(create_config())

    assert organizer.get_category(Path("photo.jpg")) == "Images"


def test_should_recognize_document_file() -> None:
    """Should classify PDF files as Documents."""

    organizer = FileOrganizer(create_config())

    assert organizer.get_category(Path("invoice.pdf")) == "Documents"


def test_should_recognize_video_file() -> None:
    """Should classify MP4 files as Videos."""

    organizer = FileOrganizer(create_config())

    assert organizer.get_category(Path("movie.mp4")) == "Videos"


def test_should_assign_unknown_extension_to_other() -> None:
    """Unknown extensions should be placed in Others."""

    organizer = FileOrganizer(create_config())

    assert organizer.get_category(Path("archive.xyz")) == "Other"


def test_should_ignore_extension_case() -> None:
    """Extension matching should be case-insensitive."""

    organizer = FileOrganizer(create_config())

    assert organizer.get_category(Path("PHOTO.JPG")) == "Images"


def test_should_move_file_to_category_directory(tmp_path: Path) -> None:
    """Should move file into the correct category directory."""

    source_file = tmp_path / "photo.jpg"
    source_file.write_text("image")

    organizer = FileOrganizer(create_config())

    destination = organizer.move_file(source_file, tmp_path)

    assert destination.exists()
    assert destination.parent.name == "Images"
    assert destination.name == "photo.jpg"

    assert not source_file.exists()


def test_should_create_destination_directory(tmp_path: Path) -> None:
    """Should automatically create destination directory."""

    source_file = tmp_path / "document.pdf"
    source_file.write_text("content")

    organizer = FileOrganizer(create_config())

    destination = organizer.move_file(source_file, tmp_path)

    assert destination.parent.exists()
    assert destination.parent.name == "Documents"


def test_should_move_unknown_extension_to_other(tmp_path: Path) -> None:
    """Unknown extensions should be moved into Other directory."""

    source_file = tmp_path / "archive.xyz"
    source_file.write_text("content")

    organizer = FileOrganizer(create_config())

    destination = organizer.move_file(source_file, tmp_path)

    assert destination.parent.name == "Other"
    assert destination.exists()