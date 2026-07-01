from pydantic import BaseModel, ConfigDict


class RulesConfig(BaseModel):
    """Configuration describing file organization rules."""

    model_config = ConfigDict(frozen=True)

    categories: dict[str, list[str]]