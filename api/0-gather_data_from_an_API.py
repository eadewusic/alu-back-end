#!/usr/bin/python3

"""
This script fetches and displays an employee's TODO list
progress using a REST API.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""

import requests
from sys import argv


def main():
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])

        base_url = "https://jsonplaceholder.typicode.com/users"
        user_url = f"{base_url}/{employee_id}"
        todos_url = f"{base_url}/{employee_id}/todos"

        # Fetch employee data and their tasks from the REST API
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200:
            print("User not found")
        elif todos_response.status_code != 200:
            print("Tasks not found")
        else:
            user_data = user_response.json()
            todo_data = todos_response.json()

            # Extract employee name
            employee_name = user_data.get("name")
            # Count the total number of tasks and completed tasks
            total_tasks = len(todo_data)
            done_tasks = sum(1 for task in todo_data if task.get("completed"))

            # Print the progress information in the required format
            progress_message = (
                f"Employee {employee_name} is done with tasks"
                f"({done_tasks}/{total_tasks}):"
            )
            print(progress_message)

            for task in todo_data:
                if task.get("completed"):
                   print(f"\t{task.get('title')}")

if __name__ == "__main__":
    main()
