# tasks/github_integration.py
import requests
from config.settings import GITHUB_TOKEN


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

def fetch_repositories(username):
    repos_response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers=headers
    )
    if repos_response.status_code == 200:
        return repos_response.json()
    else:
        print(f"Error fetching repositories: {repos_response.status_code}")
        return []

def fetch_all_issues(username):
    repositories = fetch_repositories(username)
    all_issues = []
    for repo in repositories:
        issues = fetch_github_issues(username, repo['name'])
        all_issues.extend(issues)
    return all_issues

def fetch_all_events(events_url):
    events_response = requests.get(
    events_url,
    headers=headers
)
    if events_response.status_code == 200:
        return events_response.json()
    else:
        print(f"Error fetching repositories: {events_response.status_code}")
        return []