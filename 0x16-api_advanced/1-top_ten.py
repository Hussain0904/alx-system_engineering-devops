#!/usr/bin/python3
"""Module that consumes the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    If not a valid subreddit, print None.
    Invalid subreddits may return a redirect to search results. Ensure that
    you are not following redirects.

    Args:
        subreddit (str): subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {
        'User-Agent': 'MyAPI/0.0.1'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
