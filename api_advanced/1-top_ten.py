#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Fetch and print the titles of the top 10 hot posts in a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post['data']['title'])
