#!/usr/bin/python3

"""
Using what you did in the task #0,
extend your Python script to export
data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    # Define the base URLs for API requests
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    # Create a payload with the 'userId' query parameter
    payload = {"userId": sys.argv[1]}

    # Make API requests to fetch data
    response_todo = requests.get(todo_url, params=payload)
    response_user = requests.get(user_url)

    # Convert API responses to JSON format
    data_todo = response_todo.json()
    data_user = response_user.json()

    # Define the CSV filename based on user ID
    filename = f"{sys.argv[1]}.csv"

    # Open the CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        data_writer = csv.writer(
            csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL
        )
        
        data_writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        
        # Iterate through the tasks and write to the CSV file
        for task in data_todo:
            data_writer.writerow([task["userId"], data_user["username"], task["completed"], task["title"]])
