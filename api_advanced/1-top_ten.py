#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        
    
        if response.status_code == 200:
            hot_posts = response.json().get("data", {}).get("children", [])
            
    
            if hot_posts:
                for post in hot_posts:
                    print(post.get("data", {}).get("title"))
                return "OK"  
            else:
                print("None")
                return "None"
        else:
            print("None")
            return "None"
    except Exception as e:
        print("None")
        return "None"
