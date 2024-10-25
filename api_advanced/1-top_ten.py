#!/usr/bin/python3
"""
Module to get the top 10 hot posts from a subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid or does not exist, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit is valid and request succeeded
        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])
            
            # Print titles of the first 10 hot posts
            for post in posts:
                print(post["data"].get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
