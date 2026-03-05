import questionary

from rich.table import Table
from rich.console import Console

console = Console()

def print_tables(data: list, group_by: str):
    tables = {}
    for r in data:
        p_id = r[group_by]
        if p_id not in tables:
            p_name = r["references"]["full"].split("#")[0].split("/")[-1]
            tables[p_id] = Table(title=f"{p_name} issues")
            tables[p_id].add_column("Title", justify="center")
            tables[p_id].add_column("Description", justify="center")
            tables[p_id].add_column("URL", justify="center")

        tables[p_id].add_row(r["title"], r["description"], r["web_url"])

    for table in tables.values():
        console.print(table)

def select_issues(data: list, group_by: str):
    projects = {}
    for r in data:
        p_id = r[group_by]
        p_name = r["references"]["full"].split("#")[0].split("/")[-1]
        if p_id not in projects:
            projects[p_id] = []

        projects[p_id].append((f'{p_name}: {r["title"]}', r['web_url']))
    choices = []
    for project in projects.values():
        choices.extend([questionary.Choice(title=issue[0], value=issue[1]) for issue in project])
    print(choices)
    return questionary.checkbox(
        "Select issues:",
        choices = choices,
        ).ask()

