from pathlib import Path

from file_organizer.config import load_config


def test_load_config_from_custom_file(tmp_path: Path) -> None:
    """Should load configuration from a custom YAML file."""

    config_file = tmp_path / "rules.yaml"

    config_file.write_text(
        """
    categories:
        Images:
            - .jpg
            - .png
            
        Documents:
            - .pdf    
        """,
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert "Images" in config.categories
    assert ".jpg" in config.categories["Images"]
    assert ".pdf" in config.categories["Documents"]