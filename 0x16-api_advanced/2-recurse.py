#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recursively query the reddit API, and fetch all hot posts
    title for a subreddit
    """

    headers = {
            "Accept": "*/*",
            "User-Agent": "ALX student script",
    }
    api_url = 'https://www.reddit.com/r'
    type_ = 'hot'
    url = '{}/{}/{}.json?raw_json=1&after={}'.format(
        api_url, subreddit, type_, after
    )
    res = requests.get(url, headers=headers)
    if not res.ok:
        return None
    data = res.json()
    data = data.get("data")
    posts = data["children"]
    for post in posts:
        title = post["data"]["title"]
        hot_list.append(title)

    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
