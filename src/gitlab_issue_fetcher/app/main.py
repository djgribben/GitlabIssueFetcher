import typer

from .gitlab import fetch_issues
from .display import print_tables, select_issues

app = typer.Typer()

@app.command()
def main(user: str):
    issues = fetch_issues(user)
    print_tables(issues, group_by="project_id")
    selected_issues = select_issues(issues, group_by="project_id")
    typer.echo(f"Selected: {selected_issues}")

if __name__ == "__main__":
    app()
