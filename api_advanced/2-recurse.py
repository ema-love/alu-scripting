#!/usr/bin/python3
"""
Export employee TODO list data to a JSON file
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    emp_id = sys.argv[1]

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos").json()

    username = user.get("username")

    data = {
        emp_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    filename = f"{emp_id}.json"

    with open(filename, "w") as f:
        json.dump(data, f)
