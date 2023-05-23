#!/usr/bin/python3
"""export data as JSON"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        employee = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        response = requests.get("{}users/{}".format(url, employee))
        data = response.json()
        username = data.get("username")
        response = requests.get(
             "{}todos?userId={}".format(url, employee))
        todos = response.json()

        task_list = []

        for todo in todos:
            object = {}
            object["task"] = todo["title"]
            object["completed"] = todo["completed"]
            object["username"] = username

            task_list.append(object)

        output = {employee: task_list}

        with open("{}.json".format(employee), "w") as jsonfile:
            json.dump(output, jsonfile)
