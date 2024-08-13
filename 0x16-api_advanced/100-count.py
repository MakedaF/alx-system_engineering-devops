#!/usr/bin/python3
""" function to count words in all hot posts of given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    # Creates URL
    url = "https://www.reddit.com/r/{}/hot/.jason".format(subreddit)
    # Creates user agent header to let Reddit know who is requesting
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # Setting query parameters
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    # making a request
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    # Error handling of response
    if response.status_code == 404:
        print("")
        return
    try:
        results = response.json()
    except ValueError:
        print("")
        return
    # prase the Jason response to extract data
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times
    # recurse if there are more pages: else print results
    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
