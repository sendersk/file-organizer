import json

from pathlib import Path

from file_organizer.models import OrganizationReport
from file_organizer.reporter import JsonReporter


def test_should_generate_json_report(tmp_path: Path) -> None:
    """Should generate a JSON report."""

    report = OrganizationReport(
        processed=5,
        categorized={
            "Images": 2,
            "Documents": 2,
            "Other": 1,
        },
    )

    output_file = tmp_path / "reports" / "report.json"

    reporter = JsonReporter(output_file)

    reporter.generate(report)

    assert output_file.exists()


def test_should_save_correct_report_content(tmp_path: Path) -> None:
    """Should save report content as valid JSON."""

    report = OrganizationReport(
        processed=3,
        categorized={
            "Images": 1,
            "Documents": 1,
            "Other": 1,
        },
    )

    output_file = tmp_path / "reports" / "report.json"

    reporter = JsonReporter(output_file)

    reporter.generate(report)

    with output_file.open(encoding="utf-8") as file:
        data = json.load(file)

    assert data["processed"] == 3
    assert data["categorized"]["Images"] == 1
    assert data["categorized"]["Documents"] == 1
    assert data["categorized"]["Other"] == 1


def test_should_create_output_directory(tmp_path: Path) -> None:
    """Should automatically create output directory."""

    report = OrganizationReport(
        processed=1,
        categorized={
            "Other": 1,
        },
    )

    output_file = tmp_path / "nested" / "reports" / "report.json"

    reporter = JsonReporter(output_file)

    reporter.generate(report)

    assert output_file.parent.exists()
    assert output_file.exists()