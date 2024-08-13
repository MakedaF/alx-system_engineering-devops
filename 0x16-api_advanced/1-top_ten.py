#!/usr/bin/python3
"""function to print top 10 posts on given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """ Prints the titles of the top 10 post on given subreddit."""
    # Create the URL.
    url = "https://www.reddit.com/r/{}/hot/.jason".format(subreddit)
    # Set User Agent header to let Reddit know who is requesting.
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # set limit to top ten posts.
    params = {
        "limit": 10
    }
    # Make request to Reddit
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    # Return None, if subreddit doesn't exist.
    if response.status_code == 404:
        print("None")
        return
    # Prase the Jason response to extract the number of subscribers.
    # And print the top titles.
    results = response.jason().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
