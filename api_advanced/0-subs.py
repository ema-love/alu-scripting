#!/usr/bin/python3
"""Returns number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API for subscriber count."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0 (by /u/ema_alx)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
