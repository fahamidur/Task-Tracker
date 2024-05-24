import os
import argparse
from task_tracker.database import TaskDatabase
from task_tracker.report import generate_report

def welcome_screen():
    welcome_art = """
    _______        _        _      _______             _             
    |__   __|      | |      | |    |__   __|           | |            
        | | ___  ___| |_ __ _| |__     | | __ _ _ __ ___| | _____ _ __ 
        | |/ _ \/ __| __/ _` | '_ \    | |/ _` | '__/ __| |/ / _ \ '__|
        | |  __/\__ \ || (_| | | | |   | | (_| | | | (__|   <  __/ |   
        |_|\___||___/\__\__,_|_| |_|   |_|\__,_|_|  \___|_|\_\___|_|   
                                                                    
    """
    print(welcome_art)
    print("Welcome to the Task Tracker CLI Tool!")
    print("Please choose an option:")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Show last 7 added tasks")
    print("4. Filter tasks by date")
    print("5. Generate report")
    print("6. Edit an existing task")
    print("7. Exit")

def get_task_details():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    deadline = input("Enter the deadline (YYYY-MM-DD): ")
    status = input("Enter the status (pending, in-progress, completed): ")
    priority = int(input("Enter the priority (integer): "))
    payment = float(input("Enter the payment: "))
    return title, description, start_date, deadline, status, priority, payment

def main():
    db = TaskDatabase('tasks.db')

    while True:
        welcome_screen()
        choice = input("Enter your choice: ")

        if choice == '1':
            title, description, start_date, deadline, status, priority, payment = get_task_details()
            db.add_task(title, description, start_date, deadline, status, priority, payment)
        elif choice == '2':
            tasks = db.get_all_tasks()
            for task in tasks:
                print(task)
        elif choice == '3':
            tasks = db.get_last_n_tasks(7)
            for task in tasks:
                print(task)
        elif choice == '4':
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            tasks = db.filter_tasks_by_date(start_date, end_date)
            for task in tasks:
                print(task)
        elif choice == '5':
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            output_file_name = input("Enter the output file name (e.g., report.xlsx): ")
            output_directory = input("Enter the directory to save the file (press Enter for current directory): ")
            if output_directory:
                output_path = os.path.join(output_directory, output_file_name)
            else:
                output_path = output_file_name
            tasks = db.filter_tasks_by_date(start_date, end_date)
            generate_report(tasks, output_path)
            print(f"Report generated: {output_path}")
        elif choice == '6':
            task_id = int(input("Enter the task ID to edit: "))
            title, description, start_date, deadline, status, priority, payment = get_task_details()
            db.update_task(task_id, title, description, start_date, deadline, status, priority, payment)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")