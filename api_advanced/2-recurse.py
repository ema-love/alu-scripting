#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return all hot article titles.

    Args:
        subreddit: name of the subreddit
        hot_list: list to accumulate hot article titles
        after: pagination token for next page

    Returns:
        List of all hot article titles, or None if subreddit is invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomBot/1.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        after = data.get('data', {}).get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None

    except Exception:
        return None
