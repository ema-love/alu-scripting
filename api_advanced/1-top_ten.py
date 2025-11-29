#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts.

    Args:
        subreddit: name of the subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:0-subs:v1.0.0 (by /u/yourusername)'
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            children = data.get('data', {}).get('children', [])

            if not children:
                print("None")
                return

            for child in children:
                post_data = child.get('data', {})
                title = post_data.get('title')
                print(title)
        else:
            print("None")

    except (requests.RequestException, ValueError, KeyError):
        print("None")
