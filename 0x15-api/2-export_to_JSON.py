#!/usr/bin/python3
""" This python script exports all data in json file """

import json
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    userdict = {}
    tasks = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskdict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')}
            tasks.append(taskdict)
    userdict[userId] = tasks

    filename = userId + ".json"
    with open(filename, 'w') as jsonf:
        json.dump(userdict, jsonf)
