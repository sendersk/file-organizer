import yaml

from pathlib import Path

from .models import RulesConfig


CONFIG_PATH = Path("config/rules.yaml")


def load_config(config_path: Path = CONFIG_PATH) -> RulesConfig:
    """
    Load and validate file organization rules from a YAML file.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Validated application configuration.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        yaml.YAMLError: If the YAML file is invalid.
    """

    with config_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return RulesConfig.model_validate(data)