#!/usr/bin/python3
"""Module that recursively queries the Reddit API for all hot article
titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return a list of titles of all hot articles for a given subreddit.

    If the subreddit is invalid, return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0 by cedrick13bienvenue"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
