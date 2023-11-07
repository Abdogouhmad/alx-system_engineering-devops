#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests, sys


import requests

def recurse(subreddit, hot_list=[], count=0, next_page=None):
    """
    Recursively fetches titles of hot articles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the titles of hot articles. Defaults to an empty list.
        count (int, optional): The count of articles fetched so far. Defaults to 0.
        next_page (str, optional): The next page token for pagination. Defaults to None.

    Returns:
        list: List containing titles of all hot articles.
    """
    # Set the User-Agent header for the request
    headers = {"User-Agent": "0x16. API_advanced-e_kiminza"}

    # Construct the URL for the API request
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set the parameters for the API request
    params = {"limit": 50, "next_page": next_page, "count": count}

    # Send the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Extract the response data
    response_data = response.json().get("data")
    next_page = response_data.get("next_page")
    count += response_data.get("dist")
    children = response_data.get("children")

    # Extract the titles of the articles and add them to the hot_list
    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    # If there is a next page, recursively call the function
    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)

    # Return the hot_list
    return hot_list


if __name__ == "__main__":
    recurse = __import__("2-recurse").recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
