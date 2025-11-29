#!/usr/bin/python3
"""
Script that returns TODO list progress for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    emp_id = sys.argv[1]

    # Fetch employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed")]
    done_count = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
