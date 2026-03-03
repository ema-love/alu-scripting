#!/usr/bin/python3
"""Recursively counts keywords in hot article titles for a subreddit"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    if not counts:
        for word in word_list:
            counts[word.lower()] = counts.get(word.lower(), 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "MyBot/1.0"}
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
                print(f"{word}: {count}")
        return

    return count_words(subreddit, word_list, counts, after)
