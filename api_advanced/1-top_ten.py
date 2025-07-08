#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    If the subreddit is invalid or there's an error, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python/requests:top_ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return
        for post in data:
            print(post["data"]["title"])
    except Exception:
        print(None)
