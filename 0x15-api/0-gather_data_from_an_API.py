#!/usr/bin/python3
"""Returns to do list info"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ).json()

    task_completed = [
        task.get("title") for task in todos if task.get("completed") is True
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(task_completed), len(todos)
        )
    )
    [print("\t {}".format(task)) for task in task_completed]
