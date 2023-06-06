#!/usr/bin/python3
"""
module contains function to get no. of reddit's
subreddit subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    query the reddit API, and fetch data about a
    reddit's subreddit
    """

    headers = {
            "Accept": "*/*",
            "User-Agent": "ALX student script",
    }
    api_url = 'https://www.reddit.com/r'
    url = '{}/{}/about.json?raw_json=1'.format(api_url, subreddit)
    res = requests.get(url, headers=headers)
    if not res.ok:
        return 0
    data = res.json().get("data")
    subscribers = data.get("subscribers")
    return subscribers
