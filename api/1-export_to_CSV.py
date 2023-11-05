#!/usr/bin/python3

"""
This script fetches and displays an employee's TODO
list and exports the data in CSV format.

Usage:
    ./1-export_to_CSV.py <employee_id>
"""

import csv
import requests
from sys import argv


def main():
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

            # Extract user information
            user_id = user_data.get("id")
            username = user_data.get("username")

            # Define the CSV filename based on user_id
            csv_filename = f"{user_id}.csv"

            # Open the CSV file for writing
            with open(csv_filename, mode="w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                # Write the header row to the CSV file
                writer.writerow([
                    "USER_ID",
                    "USERNAME",
                    "TASK_COMPLETED_STATUS",
                    "TASK_TITLE"
                ])
                # Write the task data to the CSV file
                for task in todo_data:
                    task_id = task.get("id")
                    task_title = task.get("title")
                    task_completed = task.get("completed")
                    writer.writerow([
                        user_id,
                        username,
                        task_completed,
                        task_title
                    ])

            print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    main()
