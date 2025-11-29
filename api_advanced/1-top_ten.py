#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts.

    Args:
        subreddit: name of the subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)

        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])

            if len(children) == 0:
                print("None")
            else:
                for child in children:
                    title = child.get('data', {}).get('title')
                    if title:
                        print(title)
        else:
            print("None")
    except Exception:
        print("None")
