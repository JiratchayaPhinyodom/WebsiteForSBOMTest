import requests

def get_github_api_status():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API is reachable!")
    else:
        print("Failed to reach GitHub API")

if __name__ == "__main__":
    get_github_api_status()