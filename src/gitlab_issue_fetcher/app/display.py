import questionary
from rich.console import Console
from rich.table import Table

console = Console()

_GROUP_BY = "project_id"


def _project_name(issue: dict) -> str:
    return issue["references"]["full"].split("#")[0].split("/")[-1]


def _group_issues(data: list[dict]) -> dict[int, tuple[str, list[dict]]]:
    projects: dict[int, tuple[str, list[dict]]] = {}
    for issue in data:
        p_id = issue[_GROUP_BY]
        if p_id not in projects:
            projects[p_id] = (_project_name(issue), [])
        projects[p_id][1].append(issue)
    return projects


def print_tables(data: list[dict]) -> None:
    for p_name, issues in _group_issues(data).values():
        table = Table(title=f"{p_name} issues")
        table.add_column("Title", justify="center")
        table.add_column("Description", justify="center")
        table.add_column("URL", justify="center")
        for issue in issues:
            table.add_row(issue["title"], issue["description"] or "", issue["web_url"])
        console.print(table)


def select_issues(data: list[dict]) -> list[str] | None:
    choices = [
        questionary.Choice(title=f"{p_name}: {issue['title']}", value=issue["web_url"])
        for p_name, issues in _group_issues(data).values()
        for issue in issues
    ]
    return questionary.checkbox("Select issues:", choices=choices).ask()
