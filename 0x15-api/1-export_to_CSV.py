#!/usr/bin/python3
"""Exports to-do list information to a CSV file"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [
            writer.writerow(
                [
                    user_id, username, task.get("completed"), task.get("title")
                ]
            ) for task in todos
        ]
