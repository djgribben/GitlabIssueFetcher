import typer

from .display import print_tables, select_issues
from .gitlab import fetch_issues

app = typer.Typer()


@app.command()
def main(user: str) -> None:
    issues = fetch_issues(user)
    print_tables(issues)
    selected_issues = select_issues(issues)
    typer.echo(f"Selected: {selected_issues}")


if __name__ == "__main__":
    app()
