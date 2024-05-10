#!/usr/bin/python3

"""
This function queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
    """
    headers = {'User-Agent': 'CustomClient/1.0'}
    url = f"https://api.reddit.com/r/{subreddit}?sort=hot&limit=10"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    response = response.json()
    if 'data' in response:
        for post in response['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
