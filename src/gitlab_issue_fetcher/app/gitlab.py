import httpx
import os


def fetch_issues(user: str):
    pat = os.environ["PAT"]
    response = httpx.get(f"https://gitlab.com/api/v4/issues?assignee_username={user}&state=opened", headers={"PRIVATE-TOKEN": pat})
    return response.json() 
