#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to a JSON format"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos?userId={}".format(user_id)).json()

    with open("{}.json".format(user_id), "w") as file:
        json.dump(
            {
                user_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username,
                    }
                    for task in todos
                ]
            },
            file,
        )
