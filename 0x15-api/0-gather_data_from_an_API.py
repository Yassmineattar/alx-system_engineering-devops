#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests # type: ignore
import sys

if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"

    url = base_Url + "/" + employee_Id
    response = requests.get(url)
    employee_Name = response.json()['name']

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_Name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
