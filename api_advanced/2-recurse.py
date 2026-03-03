#!/usr/bin/python3
"""Recursively returns list of all hot article titles for a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "MyBot/1.0"}
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
