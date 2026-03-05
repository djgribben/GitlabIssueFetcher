import os

import httpx


def fetch_issues(user: str) -> list[dict]:
    pat = os.getenv("PAT")
    if not pat:
        raise SystemExit("Error: PAT environment variable is not set.")

    issues: list[dict] = []
    page = 1

    while True:
        response = httpx.get(
            "https://gitlab.com/api/v4/issues",
            params={"assignee_username": user, "state": "opened", "per_page": 100, "page": page},
            headers={"PRIVATE-TOKEN": pat},
        )
        response.raise_for_status()

        batch: list[dict] = response.json()
        issues.extend(batch)

        if len(batch) < 100:
            break
        page += 1

    return issues
