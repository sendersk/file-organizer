import typer

from pathlib import Path

from file_organizer.config import load_config
from file_organizer.models import OrganizationReport
from file_organizer.organizer import FileOrganizer
from file_organizer.reporter import JsonReporter
from file_organizer.scanner import FileScanner


app = typer.Typer(
    help="Automatically organize files into categorized directories."
)


@app.command()
def organize(directory: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Directory containing files to organize.",
    ),
) -> None:
    """
    Full file organization pipeline.
    """

    # Load configuration
    config = load_config()

    # Initialize services
    scanner = FileScanner(directory)
    organizer = FileOrganizer(config)

    # Scan files
    files = scanner.scan()

    categorized: dict[str, int] = {}

    # Process files
    for file in files:
        category = organizer.get_category(file)

        if category not in categorized:
            categorized[category] = 0

        categorized[category] += 1

        organizer.move_file(file, directory)

    # Create report
    report = OrganizationReport(
        processed=len(files),
        categorized=categorized,
    )

    reporter = JsonReporter(directory / "reports" / "report.json")
    reporter.generate(report)

    typer.echo("Organization completed successfully.")
    typer.echo(f"Processed files: {len(files)}")
    typer.echo(f"Report saved to: {directory / 'reports' / 'report.json'}")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()