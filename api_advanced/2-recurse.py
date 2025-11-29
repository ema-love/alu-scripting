#!/usr/bin/python3
"""
Module to recursively query Reddit API for all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries Reddit API and returns list of titles of all hot
    articles for a given subreddit.
    
    Args:
        subreddit: name of the subreddit
        hot_list: list to accumulate hot post titles
        after: pagination token for next page
        
    Returns:
        List of all hot article titles or None if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code != 200:
            return None
        
        data = response.json()
        posts_data = data.get('data', {})
        posts = posts_data.get('children', [])
        
        if not posts:
            return hot_list if hot_list else None
        
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                hot_list.append(title)
        
        after = posts_data.get('after')
        
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
            
    except Exception:
        return None
