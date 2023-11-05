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

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Construct the URLs for API requests
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Make API requests to fetch data
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)

        todos_response.raise_for_status()
        user_response.raise_for_status()

        todos_data = todos_response.json()
        user_data = user_response.json()

        # Prepare the CSV filename based on user ID
        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, 'w', newline='') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)

            # Write the CSV header
            data_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Iterate through TODO list data and write to CSV
            for todo in todos_data:
                data_writer.writerow([employee_id, user_data["username"], todo["completed"], todo["title"]])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
