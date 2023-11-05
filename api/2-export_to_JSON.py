#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Construct the URLs for API requests
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Make API requests to fetch data
        response_todo = requests.get(todo_url)
        response_user = requests.get(user_url)

        response_todo.raise_for_status()
        response_user.raise_for_status()

        todo_data = response_todo.json()
        user_data = response_user.json()

        # Prepare the JSON filename based on user ID
        filename = f"{employee_id}.json"

        # Create a dictionary in the required format
        data_to_export = {employee_id: []}

        # Iterate through the tasks and add them to the dictionary
        for task in todo_data:
            data_to_export[employee_id].append({
                "task": task["title"],
                "completed": task["completed"],
                "username": user_data["username"]
            })

        # Write the data to a JSON file
        with open(filename, 'w') as jsonfile:
            json.dump(data_to_export, jsonfile, indent=4)

        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
