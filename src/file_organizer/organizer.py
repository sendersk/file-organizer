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