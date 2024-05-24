#!/usr/bin/python3

"""
This is a recursive function that queries the Reddit API
and returns a list containing the titles of
all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the Reddit API
    and returns a list containing the titles of
    all hot articles for a given subreddit
    """
    headers = {'User-Agent': 'CustomClient/1.0'}
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    params = {'after': after}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    response = response.json()
    children = response['data']['children']

    if not children:
        return hot_list
    for post in children:
        hot_list.append(post['data']['title'])

    after = response['data']['after']
    return recurse(subreddit, hot_list, after)
