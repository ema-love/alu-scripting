#!/usr/bin/python3
"""Recursively retrieves all hot article titles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot articles for a subreddit."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "MyRedditBot/1.0 (by /u/ema_alx)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
