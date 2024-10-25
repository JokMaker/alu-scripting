#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the request was successful
        if RESPONSE.status_code != 200:
            print(None)
            return

        HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
        
        # Print the titles if available
        if HOT_POSTS:
            [print(post.get('data').get('title')) for post in HOT_POSTS]
        else:
            print(None)
    except Exception:
        print(None)
