#!/usr/bin/python3
"""
Exports employee TODO list data to CSV
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    emp_id = sys.argv[1]

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos").json()

    username = user.get("username")

    filename = f"{emp_id}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
