from pathlib import Path


class FileScanner:
    """
    Scans a directory and returns all files for processing.

    This module is responsible ONLY for discovering files.
    It does NOT move or modify anything.
    """

    def __init__(self, root_path: Path) -> None:
        self.root_path = root_path

    def scan(self) -> list[Path]:
        """
        Recursively scan directory and return list of files.

        Returns:
            List of file paths (excluding directories).
        """

        if not self.root_path.exists():
            raise FileNotFoundError(f"Directory not found: {self.root_path}")

        if not self.root_path.is_dir():
            raise ValueError(f"Path is not a directory: {self.root_path}")

        files: list[Path] = []

        for path in self.root_path.rglob("*"):
            if path.is_file():
                files.append(path)

        return files