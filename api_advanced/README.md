# API Advanced

This project contains Python scripts that interact with the Reddit API to query and process data from subreddits.

## Requirements

- Python 3
- `requests` module

## Files

### 0-subs.py
Returns the number of total subscribers for a given subreddit.
- Returns `0` if the subreddit is invalid.

```bash
python3 0-main.py programming
```

### 1-top_ten.py
Prints the titles of the first 10 hot posts for a given subreddit.
- Prints `None` if the subreddit is invalid.

```bash
python3 1-main.py programming
```

### 2-recurse.py
Recursively returns a list of titles of all hot articles for a given subreddit.
- Returns `None` if the subreddit is invalid or no results found.

```bash
python3 2-main.py programming
```

### 3-count.py
Recursively queries the Reddit API, parses hot article titles, and prints a sorted count of given keywords.
- Case-insensitive keyword matching.
- Results sorted by count (descending), then alphabetically (ascending) for ties.
- Words with no matches are not printed.
- Prints nothing if the subreddit is invalid.

```bash
python3 3-main.py programming 'python java javascript'
```

## Notes

- No authentication required for these Reddit API calls.
- All scripts set a custom `User-Agent` to avoid `Too Many Requests` errors.
- Redirects are not followed — invalid subreddits return `0` or `None` instead of search results.

## Repository

- GitHub: `alu-scripting`
- Directory: `api_advanced`
