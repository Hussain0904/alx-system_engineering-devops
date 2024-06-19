#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit.

    The Reddit API uses pagination for separating pages of responses.
    If not a valid subreddit, return None.

    Args:
        subreddit (str): subreddit.
        hot_list (list, optional): list of titles. Defaults to [].

    Returns:
        list: list of titles.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))
            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
