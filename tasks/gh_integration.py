# tasks/github_integration.py
import requests
from config import GITHUB_TOKEN

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def fetch_github_issues(repo_owner, repo_name):
    response = requests.get(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues",
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching issues: {response.status_code}")
        return []
