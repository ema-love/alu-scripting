#!/usr/bin/python3
"""Recursively counts keyword occurrences in hot article titles."""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print sorted keyword counts from hot article titles of a subreddit."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = counts.get(word.lower(), 0)
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "MyRedditBot/1.0 (by /u/ema_alx)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] += title.count(w)
    if after is None:
        results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in results:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, after)
