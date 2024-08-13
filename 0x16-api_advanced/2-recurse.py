#!/usr/bin/python3
""" function to query a list of all hot posts
on a given Reddit subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ returns a list of all hot post titles on a given subreddit."""
    # Create URL
    url = "https://www.reddit.com/r/{}/hot/.jason".format(subreddit)
    # sets user agent header to let Reddit know who is requesting.
    headers = {
        "User-Agent": "linux:016.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # sets restrictions
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    # return None if subreddit doesn't exist
    if response.status_code == 404:
        return None
    # Prase the Jason respose to extract data
    results = response.jason().get("data")
    # Extract pagination token and post count
    after = results.get("after")
    count += results.get("dist")
    # Add each post title to hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))
    # If there's more data to fetch, recurse; else, return the list
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
