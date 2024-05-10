#!/usr/bin/python3
"""
This function queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces)
"""

import json
import requests


def count_words(subreddit, word_list, after="", counter=[]):
    """this function counts all words"""

    if after == "":
        counter = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
            url, params={'after': after},
            allow_redirects=False, headers={'user-agent': 'bhalut'})
    if response.status_code == 200:
        data = response.json()
        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        counter[i] += 1
        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        counter[i] += counter[j]
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (counter[j] > counter[i] or
                            (word_list[i] > word_list[j] and
                             counter[j] == counter[i])):
                        aux = counter[i]
                        counter[i] = counter[j]
                        counter[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux
            for i in range(len(word_list)):
                if (counter[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), counter[i]))
        else:
            count_words(subreddit, word_list, after, counter)
