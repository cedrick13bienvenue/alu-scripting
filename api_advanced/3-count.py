#!/usr/bin/python3
"""Module that recursively queries the Reddit API and counts keywords
in hot article titles.
"""
import requests


def count_words(subreddit, word_list, after="", counts=None):
    """Print a sorted count of given keywords found in hot article titles.

    Matching is case-insensitive and limited to whole words. If the
    subreddit is invalid or no keywords match, nothing is printed.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0 by cedrick13bienvenue"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        tokens = title.lower().split()
        for word in word_list:
            keyword = word.lower()
            counts[keyword] = counts.get(keyword, 0) + tokens.count(keyword)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = [(word, total) for word, total in counts.items() if total > 0]
    results.sort(key=lambda pair: (-pair[1], pair[0]))
    for word, total in results:
        print("{}: {}".format(word, total))
