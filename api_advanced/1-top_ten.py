#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    PARAMS = {"limit": 10}
    RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS, allow_redirects=False)
    if RESPONSE.status_code == 404:
        print("None")
        return
    HOT_POSTS = RESPONSE.json().get("data").get("children")
    [print(post.get('data').get('title')) for post in HOT_POSTS]
