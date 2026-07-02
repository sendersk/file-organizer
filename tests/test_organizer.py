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