#!/usr/bin/python3
"""
Module to recursively query Reddit API and count keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries Reddit API, parses titles of all hot articles,
    and prints a sorted count of given keywords.
    
    Args:
        subreddit: name of the subreddit
        word_list: list of keywords to count (case-insensitive)
        after: pagination token for next page
        word_count: dictionary to accumulate word counts
    """
    if word_count is None:
        word_count = {}
        # Normalize word_list to lowercase
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_count:
                word_count[word_lower] = 0
    
    if subreddit is None or not isinstance(subreddit, str):
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'limit': 100}
    
    if after:
        params['after'] = after
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code != 200:
            return
        
        data = response.json()
        posts_data = data.get('data', {})
        posts = posts_data.get('children', [])
        
        if not posts:
            # Base case: print results
            if after is None:
                print_results(word_count)
            return
        
        # Count words in titles
        for post in posts:
            title = post.get('data', {}).get('title', '')
            # Split title into words and clean them
            words = title.lower().split()
            
            for word in words:
                # Remove punctuation from the word
                cleaned_word = ''.join(c for c in word if c.isalnum())
                
                if cleaned_word in word_count:
                    word_count[cleaned_word] += 1
        
        after = posts_data.get('after')
        
        if after:
            # Recursive case: continue to next page
            count_words(subreddit, word_list, after, word_count)
        else:
            # Base case: no more pages, print results
            print_results(word_count)
            
    except Exception:
        return


def print_results(word_count):
    """
    Prints sorted word count results.
    
    Args:
        word_count: dictionary of word counts
    """
    # Filter out words with 0 count
    filtered = {k: v for k, v in word_count.items() if v > 0}
    
    if not filtered:
        return
    
    # Sort by count (descending) then by word (ascending)
    sorted_words = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        print(f"{word}: {count}")
