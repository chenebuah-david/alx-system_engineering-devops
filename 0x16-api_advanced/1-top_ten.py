#!/usr/bin/python3
'''
    Prints the titles of the first 10 hot posts listed for a given subreddit
'''
from requests import get


def top_ten(subreddit):
    '''
    Description:
        - Queries the Reddit API to print first 10 host posts
    Output:
        - Success: Prints first 10 host posts listed
          for a given subreddit
        - Failure: Print None
    '''
    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 10}
    res = get(endpoint, headers=headers, allow_redirects=False, params=params)

    if res.status_code != 200:
        print(None)
        return

    top_10 = res.json()['data']['children']
    [print(post['data']['title']) for post in top_10]
