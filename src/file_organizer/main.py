import typer

app = typer.Typer(
    help="Automatically organize files into categorized directories."
)


@app.command()
def organize() -> None:
    """Organize files inside a directory."""

    typer.echo("Organizer is not implemented yet.")


def main() -> None:
    """Application entry point."""

    app()


if __name__ == "__main__":
    main()