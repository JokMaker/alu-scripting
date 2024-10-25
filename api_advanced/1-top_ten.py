#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    """Fetches and prints the first 10 hot post titles of a subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            
            # Check if posts exist, if so, print them and return "OK"
            if hot_posts:
                for post in hot_posts:
                    print(post.get("data", {}).get("title"))
                return "OK"  # Return "OK" when posts are found and printed
            else:
                print("None")
                return "None"
        else:
            # Print and return "None" if the subreddit is invalid or other error occurs
            print("None")
            return "None"
    except Exception as e:
        print("None")
        return "None"
