#!/usr/bin/python3
"""
module contains function to list top 10 hot posts of reddit's
subreddit subscribers.
"""

import requests


def top_ten(subreddit):
    """
    query the reddit API, and fetch data about a
    reddit's subreddit
    """

    headers = {
            "Accept": "*/*",
            "User-Agent": "ALX student script",
    }
    api_url = 'https://www.reddit.com/r'
    type_ = 'hot'
    url = '{}/{}/{}.json?raw_json=1'.format(
        api_url, subreddit, type_
    )
    res = requests.get(url, headers=headers)
    if not res.ok:
        print(None)
        pass
    posts = res.json().get("data")["children"]
    posts = posts[:10]
    for post in posts:
        title = post.get('data')["title"]
        print(title)
