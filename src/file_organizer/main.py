import typer

from pathlib import Path

from file_organizer.scanner import FileScanner


app = typer.Typer(
    help="Automatically organize files into categorized directories."
)


@app.command()
def organize(directory: Path = typer.Argument(
    exists=True,
    file_okay=False,
    dir_okay=True,
    readable=True,
    resolve_path=True,
    help="Directory containing files to organize.",
),
) -> None:
    """
    Scan the selected directory and display discovered files.
    """

    scanner = FileScanner(directory)

    files = scanner.scan()

    typer.echo(f"Found {len(files)} file(s).")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()