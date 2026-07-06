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
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Simulate organization without moving files."
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

    typer.echo("Starting organization...\n")

    # Process files
    for file in files:
        category = organizer.get_category(file)

        categorized[category] = categorized.get(category, 0) + 1

        target_path = directory / category / file.name

        if dry_run:
            typer.echo(f"[DRY-RUN] {file} -> {target_path}")
        else:
            organizer.move_file(file, directory)
            typer.echo(f"MOVED: {file} -> {target_path}")

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


@app.command()
def version() -> None:
    """Display application version."""
    typer.echo("File Organizer 0.1.0")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()