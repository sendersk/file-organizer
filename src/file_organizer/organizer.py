import shutil

from pathlib import Path

from file_organizer.models import RulesConfig


class FileOrganizer:
    """Determine file categories based on configured rules."""

    def __init__(self, config: RulesConfig) -> None:
        self.config = config

    def get_category(self, file_path: Path) -> str:
        """
        Return category name for a given file.

        If no matching extension is found,
        the file is assigned to the 'Other' category.
        """

        extension = file_path.suffix.lower()

        for category, extensions in self.config.categories.items():
            normalized_extensions = {
                ext.lower() for ext in extensions
            }

            if extension in normalized_extensions:
                return category

        return "Other"

    def move_file(self, file_path: Path, destination_root: Path) -> Path:
        """
        Move a file into its target category directory.

        The destination directory is created automatically if it
        does not already exist.

        Args:
            file_path: File to move.
            destination_root: Root directory for organized files.

        Returns:
            Path to the moved file.
        """

        category = self.get_category(file_path)

        destination_directory = destination_root / category
        destination_directory.mkdir(parents=True, exist_ok=True)

        destination_file = destination_directory / file_path.name

        shutil.move(str(file_path), str(destination_file))

        return destination_file