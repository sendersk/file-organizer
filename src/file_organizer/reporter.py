import json

from pathlib import Path

from file_organizer.models import OrganizationReport


class JsonReporter:
    """Generate JSON reports for completed organization jobs."""

    def __init__(self, output_file: Path) -> None:
        self.output_file = output_file

    def generate(self, report: OrganizationReport) -> None:
        """
        Save organization report as JSON.

        Args:
            report: Organization summary.
        """

        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.output_file.open("w", encoding="utf-8") as file:
            json.dump(
                report.model_dump(),
                file,
                indent=4,
                ensure_ascii=False,
            )