#!/usr/bin/python3
"""Module to recursively query Reddit API and count keywords."""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively query Reddit API and print sorted count of keywords.

    Args:
        subreddit: name of the subreddit
        word_list: list of keywords to count (case-insensitive)
        after: pagination token for next page
        word_count: dictionary to accumulate word counts
    """
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0)

    if not subreddit or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomBot/1.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            title = post.get('data', {}).get('title', '')
            if title:
                words = title.lower().split()
                for word in words:
                    clean_word = ''.join(c for c in word
                                         if c.isalnum() or c == '-')
                    if clean_word in word_count:
                        word_count[clean_word] += 1

        after = data.get('data', {}).get('after')

        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            print_results(word_count)

    except Exception:
        return


def print_results(word_count):
    """
    Print the word count results in the required format.

    Args:
        word_count: dictionary of word counts
    """
    filtered = {k: v for k, v in word_count.items() if v > 0}

    if not filtered:
        return

    sorted_words = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print("{}: {}".format(word, count))
