#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0 by cedrick13bienvenue"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get("data", {}).get("subscribers", 0)
