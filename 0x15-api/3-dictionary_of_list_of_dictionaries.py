#!/usr/bin/python3
"""export data as JSON"""

import json
import requests
from sys import argv


def fetch_employee_data(id):
    """function to get an employee tasks"""
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get("{}users/{}".format(url, id))
    data = user.json()
    username = data.get("username")
    todos = requests.get(
         "{}todos?userId={}".format(url, id))
    todos = todos.json()

    tasks = []

    for todo in todos:
        object = {}
        object["username"] = username
        object["task"] = todo["title"]
        object["completed"] = todo["completed"]
        tasks.append(object)

    return tasks


if __name__ == '__main__':
    no_employee = 10
    dict_employees = {}

    filename = "todo_all_employees.json"

    for id in range(1, no_employee + 1):
        data = fetch_employee_data(id)
        dict_employees[str(id)] = data

    with open(filename, "w") as jsonfile:
        json.dump(dict_employees, jsonfile)
