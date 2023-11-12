#!/usr/bin/python3
"""
Defines a function that queries the Reddit API and returns the number of subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 for an invalid subreddit.
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Use f-string for better readability
    info = requests.get(f'{endpoint}/r/{subreddit}/about.json', headers=headers, allow_redirects=False)

    if info.status_code == 200:
        json_info = info.json()
        return json_info.get('data').get('subscribers')
    else:
        return 0
