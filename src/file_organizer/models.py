from pydantic import BaseModel, ConfigDict


class RulesConfig(BaseModel):
    """Configuration describing file organization rules."""

    model_config = ConfigDict(frozen=True)

    categories: dict[str, list[str]]


class OrganizationReport(BaseModel):
    """Summary of the file organization process."""

    model_config = ConfigDict(frozen=True)

    processed: int
    categorized: dict[str, int]