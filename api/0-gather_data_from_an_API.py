#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    # Check for the correct number of command-line arguments and whether the argument is a valid integer
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1]

        # Fetch employee data and their tasks from the REST API
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

        # Check if user data is found
        if user_response.status_code != 200:
            print("User not found")
        # Check if task data is found
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
            print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
            for task in todo_data:
                if task.get("completed"):
                    print(f"\t {task.get('title')}")
