#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()

    dictionary = {employee_Id: []}
    for task in tasks:
        dictionary[employee_Id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_Id), 'w') as filename:
        json.dump(dictionary, filename)
