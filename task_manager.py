# # # Code that manages user and tasks.

""" Pseudo code 

First the code initialises constant and libaries 
    imports exisiting libarys and sets the format as "%Y-%m-%d"

Define Function: read_tasks_from_file(file_path)
    Initialises an empty list task_list.
    Open the task file and read its contents line by line.
    for each string/line in task_data, split the lines into components and create a dictionary representing a task.
    Appends the task dictionary to task_list.
    Returns task_list.  

Define Function: register_user(username_password)
    The code will loop until a unique username is provided:
    Prompt for a new username.
        If the username already exists, ask for another one.
        Loop until passwords match:
    Prompt for a password and confirmation.
        If they match, add the new user to username_password.
        Append the new username and password to user.txt.

Define Function: add_task(task_list, username_password)
    Prompt for the username to assign the task to.
        If the username does not exist, display an error and return.
    Prompt for the task title, description, and due date.
    Create a dictionary representing the new task with the current date as the assigned date.
    Append the task to task_list.
    Write the new task to tasks.txt.

Define Function: view_all(task_list)
    If task_list is empty, display "No tasks found".
    Loop through task_list and display each task's details.

Define Function: view_mine(task_list, curr_user)
    Filter task_list to find tasks assigned to curr_user.
    If no tasks are found, display "No tasks assigned to you".
    Display the list of tasks and prompt the user to select a task.
    If the user selects a task:
        Display task details.
        Prompt to either edit the task or mark it as complete.
        If marked as complete, update the task's status.

Dfine Function: generate_task_overview_report(task_list)
    Calculate the total number of tasks, completed tasks, incomplete tasks, and overdue tasks.
    Calculate percentages of incomplete and overdue tasks.
    Write these statistics to task_overview.txt.

Define Function: generate_user_overview_report(username_password, task_list)
    Write the total number of users and tasks to user_overview.txt.
    For each user, calculate and write:
        Number of tasks assigned.
        Number and percentage of completed tasks.
        Number and percentage of incomplete and overdue tasks.

Define Function: display_statistics()
    Try to open and read user_overview.txt and task_overview.txt.
    Display the contents.
    If files are not found, display an error message.

Main Function: main()
    Initialize file paths for tasks.txt and user.txt.
    If tasks.txt does not exist, create it.
    Read tasks from the file into task_list.
    Initialize logged_in as False.
    Loop until the user successfully logs in:
        If user.txt does not exist, create it with the admin credentials.
        Read user data from user.txt into username_password.
        Prompt for username and password.
        If login is successful, set logged_in to True.
    Once logged in, loop to display the main menu and handle user input:
        If the user selects 'r', call register_user().
        If the user selects 'a', call add_task().
        If the user selects 'va', call view_all().
        If the user selects 'vm', call view_mine().
        If the user selects 'gr', call report generation functions.
        If the user selects 'ds', call display_statistics() (admin only).
        If the user selects 'e', exit the loop.
        If the input is invalid, prompt the user again.

"""
     


# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
# Importing libraries
import os
from datetime import datetime, date

# Constants
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Reads data from files
def read_tasks_from_file(file_path):
    """Reads task data from a file and constructs a list of dictionaries
    representing tasks."""
    task_list = []
    with open(file_path, 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    for t_str in task_data:
        curr_t = {}
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(curr_t)
    return task_list

# Define registering a user 
def register_user(username_password):
    """Allows registration of new users."""
    while True:
        new_username = input("Enter a new username: ")
        if new_username in username_password:
            print("Username already exists. Please choose another username.")
        else:
            break
    
    while True:
        new_password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            username_password[new_username] = new_password
            with open("user.txt", "a") as user_file:
                user_file.write(f"\n{new_username};{new_password}")
            print("User registered successfully.")
            break

# Define add task using task list and username and password
def add_task(task_list, username_password):
    """Allows addition of a new task."""
    task_username = input("Enter the username of the person the task is assigned to: ")
    if task_username not in username_password:
        print("Error: User does not exist.")
        return

    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    while True:
        task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
        try:
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid date format. Please use the format YYYY-MM-DD.")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "a") as task_file:
        task_str = ";".join([
            new_task['username'],
            new_task['title'],
            new_task['description'],
            new_task['due_date'].strftime(DATETIME_STRING_FORMAT),
            new_task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
            "No"  # Initially task is not completed
        ])
        task_file.write(f"\n{task_str}")
    
    print("Task added successfully.")

# Define view all using task list
def view_all(task_list):
    """Displays all tasks stored in task_list."""
    if not task_list:
        print("No tasks found.")
        return

    for index, task in enumerate(task_list, start=1):
        print(f"Task {index}:")
        print(f"Title: {task['title']}")
        print(f"Assigned to: {task['username']}")
        print(f"Date Assigned: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Description: {task['description']}")
        print(f"Completed: {'Yes' if task['completed'] else 'No'}")
        print()

# Defines view_mine using paramaters of task list and current user 
def view_mine(task_list, curr_user):
    """Displays tasks assigned to the current user and allows for editing or
    marking tasks as complete."""
    my_tasks = [task for task in task_list if task['username'] == curr_user]

    if not my_tasks:
        print("No tasks assigned to you.")
        return

    while True:
        print("Tasks assigned to you:")
        for index, task in enumerate(my_tasks, start=1):
            print(f"Task {index}: {task['title']}")
        
        print("\nEnter the number of the task you want to edit or mark as complete.")
        print("Enter -1 to return to the main menu.")
        choice = input("Your choice: ")

        if choice == '-1':
            return
        
        try:
            choice = int(choice)
            if choice < 1 or choice > len(my_tasks):
                print("Invalid task number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or -1.")
            continue

        selected_task = my_tasks[choice - 1]
        
        print("\nSelected Task:")
        print(f"Title: {selected_task['title']}")
        print(f"Assigned to: {selected_task['username']}")
        print(f"Date Assigned: {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Due Date: {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
        print(f"Description: {selected_task['description']}")
        print(f"Completed: {'Yes' if selected_task['completed'] else 'No'}")
        
        action = input("\nDo you want to (e)dit or mark as (c)omplete? (Enter 'e', 'c', or '-1' to return): ").lower()
        
        if action == 'e':
            print("Editing task...")
        
        elif action == 'c':
            selected_task['completed'] = True
            print("Task marked as complete.")
        
        elif action == '-1':
            return
        
        else:
            print("Invalid choice. Please enter 'e', 'c', or '-1'.")

# Define the task overview report
def generate_task_overview_report(task_list):
    """Generates a task overview report."""
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task['completed'])
    incomplete_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'] < datetime.today())
    percentage_incomplete = (incomplete_tasks / total_tasks) * 100 if total_tasks != 0 else 0
    percentage_overdue = (overdue_tasks / total_tasks) * 100 if total_tasks != 0 else 0
    
    with open('task_overview.txt', 'w') as file:
        file.write("Task Overview\n")
        file.write("-------------\n")
        file.write(f"Total Number of Tasks: {total_tasks}\n")
        file.write(f"Total Number of Completed Tasks: {completed_tasks}\n")
        file.write(f"Total Number of Incomplete Tasks: {incomplete_tasks}\n")
        file.write(f"Total Number of Overdue Tasks: {overdue_tasks}\n")
        file.write(f"Percentage of Incomplete Tasks: {percentage_incomplete:.2f}%\n")
        file.write(f"Percentage of Overdue Tasks: {percentage_overdue:.2f}%\n")

    print("Task overview report generated successfully.")

# Define the user overview report
def generate_user_overview_report(username_password, task_list):
    """Generates a user overview report."""
    with open('user_overview.txt', 'w') as file:
        file.write("User Overview\n")
        file.write("-------------\n")
        file.write(f"Total Number of Users: {len(username_password)}\n")
        file.write(f"Total Number of Tasks: {len(task_list)}\n\n")

        for username in username_password.keys():
            num_tasks_assigned = sum(1 for task in task_list if task['username'] == username)
            num_completed_tasks = sum(1 for task in task_list if task['username'] == username and task['completed'])
            percentage_tasks_assigned = (num_tasks_assigned / len(task_list)) * 100
            percentage_completed_tasks = (num_completed_tasks / num_tasks_assigned) * 100 if num_tasks_assigned != 0 else 0
            num_incomplete_tasks = sum(1 for task in task_list if task['username'] == username and not task['completed'])
            percentage_incomplete_tasks = (num_incomplete_tasks / num_tasks_assigned) * 100 if num_tasks_assigned != 0 else 0
            num_overdue_tasks = sum(1 for task in task_list if task['username'] == username and not task['completed'] and task['due_date'] < datetime.today())
            percentage_overdue_tasks = (num_overdue_tasks / num_tasks_assigned) * 100 if num_tasks_assigned != 0 else 0

            file.write(f"User: {username}\n")
            file.write(f"Total Number of Tasks Assigned: {num_tasks_assigned}\n")
            file.write(f"Total Number of Completed Tasks: {num_completed_tasks}\n")
            file.write(f"Percentage of Tasks Assigned: {percentage_tasks_assigned:.2f}%\n")
            file.write(f"Percentage of Completed Tasks: {percentage_completed_tasks:.2f}%\n")
            file.write(f"Percentage of Incomplete Tasks: {percentage_incomplete_tasks:.2f}%\n")
            file.write(f"Percentage of Incomplete and Overdue Tasks: {percentage_overdue_tasks:.2f}%\n\n")

    print("User overview report generated successfully.")

# Displaying the statistics 
def display_statistics():
    """Displays statistics from the generated overview text files."""
    try:
        with open('user_overview.txt', 'r') as user_file, open('task_overview.txt', 'r') as task_file:
            user_overview = user_file.read()
            task_overview = task_file.read()
            print(user_overview)
            print(task_overview)
    except FileNotFoundError:
        print("Overview files not found. Please generate reports first.")

# Main Function
def main():
    # Initialize variables
    task_file_path = "tasks.txt"
    user_file_path = "user.txt"

    # Create tasks.txt if it doesn't exist
    if not os.path.exists(task_file_path):
        with open(task_file_path, "w"):
            pass

    # Read tasks from file
    task_list = read_tasks_from_file(task_file_path)

    # Login
    logged_in = False
    while not logged_in:
        if not os.path.exists("user.txt"):
            with open("user.txt", "w") as default_file:
                default_file.write("admin;password")

        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")

        username_password = {}
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password

        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

        task_file_path = "tasks.txt"
        task_list = read_tasks_from_file(task_file_path)

        while True:
            print()
            menu = input('''Select one of the following Options below:
             r -  Registering a user
             a - Adding a task
             va - View all tasks
             vm - View my task
             gr - Generate reports
             ds - Display statistics
             e - Exit
             : ''').lower()
             
            if menu == 'r':
                register_user(username_password)

            elif menu == 'a':
                add_task(task_list, username_password)
        
            elif menu == 'va':
                view_all(task_list)

            elif menu == 'vm':
                view_mine(task_list, curr_user)

            elif menu == 'gr':
                generate_task_overview_report(task_list)
                generate_user_overview_report(username_password, task_list)

            elif menu == 'ds':
                if curr_user == 'admin':
                    display_statistics()
                else:
                    print("You don't have permission to access this functionality.")
        
            elif menu == 'e':
                break
        
            else:
                print("Invalid input, Please try again.")

if __name__ == "__main__":
    main()
