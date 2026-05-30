import requests
import os 


def fetch_github_data(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token : 
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(url, headers=headers)

    print(f"DEBUG: Status de la requête : {response.status_code}")
    print(f"DEBUG: Données reçues : {response.text}")
    
    response.raise_for_status()
    return response.json()