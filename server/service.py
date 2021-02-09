import requests

GIT_REPO_URL = "https://api.github.com/repos/"
VALID_STATUS_CODE1 = 200
VALID_STATUS_CODE2 = 299
BAD_RESPONSE = "[ERROR] Bad Response. Unable to connect to GitHub Repositories"


def callAPI(url):
    print("inside call")
    try:
        r = requests.get(url)
    except requests.exceptions.Timeout:
        r = BAD_RESPONSE
    except requests.exceptions.TooManyRedirects:
        r = BAD_RESPONSE
    finally:
        return r

def talkToAPI(msg):
    repos = msg
    stars = {}
    error_code = []
    
    for repo in repos:
        url = GIT_REPO_URL + repo
        r = callAPI(url)
        if VALID_STATUS_CODE1 <= r.status_code <= VALID_STATUS_CODE2:
            repo_data = r.json()
            if repo not in stars:
                print(f"finding the stars for {repo} now")
                stars[repo] = repo_data['watchers']
                error_code.append(f"[SUCCESS] {repo} is a valid Repository")
                print(f"found the stars for {repo} now - {stars[repo]}")
        else:
            error_code.append(f"[ERROR] {repo} not a valid GitHub Repository")
            print(f"[ERROR] get status {r.status_code} received for {repo}")
    return stars,error_code