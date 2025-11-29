#!/usr/bin/python3
"""
Module to query Reddit API for top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If invalid subreddit, prints None.
    
    Args:
        subreddit: name of the subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        else:
            print(None)
    except Exception:
        print(None)
