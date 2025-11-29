#!/usr/bin/python3
"""
Module to query Reddit API for subreddit subscriber count
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If invalid subreddit, returns 0.
    
    Args:
        subreddit: name of the subreddit
        
    Returns:
        Number of subscribers or 0 if invalid
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0

