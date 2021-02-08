import requests

GIT_REPO_URL = "https://api.github.com/repos/"
VALID_STATUS_CODE1 = 200
VALID_STATUS_CODE2 = 299

def talkToAPI(msg):
    repos = msg
    stars = {}

    for repo in repos:
        url = GIT_REPO_URL + repo
        r = requests.get(url)
        if VALID_STATUS_CODE1 <= r.status_code <= VALID_STATUS_CODE2:
            repo_data = r.json()
            if repo not in stars:
                stars[repo] = repo_data['watchers']
        else:
            print(f"[ERROR] {repo} not a valid GitHub Repository")
            print(f"[ERROR] get status {r.status_code} received")
    return stars
