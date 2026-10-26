#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0 by cedrick13bienvenue"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
