#!/usr/bin/python3
"""function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Create the URL.
    url = "https://www.reddit.com/r/{}/about.jason".format(subreddit)
    # Sets User-Agent header to let Reddit know who is requesting.
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Make Get request to Reddit.
    response = requests.get(url, headers=headers, allow_redirects=False)
    # return 0, if subreddit doesn't exist
    if response.status_code == 404:
        return 0
    # Prase the Jason response to extract the number of subscribers.
    results = response.jason().get("data")
    # Return the number of subscribers.
    return results.get("subscribers")
