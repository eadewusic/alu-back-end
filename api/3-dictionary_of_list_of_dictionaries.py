#!/usr/bin/python3

"""
Script to export data of all tasks from all employees in JSON format.

Requirements:
- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json
"""

import json
import requests

if __name__ == "__main__":
    # Initialize an empty dictionary to store employee data
    employee_data = {}
    
    # URL to fetch user data
    users_url = "https://jsonplaceholder.typicode.com/users"
    
    # Fetch the list of users
    users = requests.get(users_url).json()

    # Iterate through each user to collect their tasks
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # URL to fetch tasks for the current user
        tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        tasks = requests.get(tasks_url).json()

        # Create a list of task dictionaries for the current user
        tasks_list = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in tasks
        ]

        # Store the tasks list in the employee_data dictionary
        employee_data[user_id] = tasks_list

    # Write the employee_data dictionary to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employee_data, json_file)
