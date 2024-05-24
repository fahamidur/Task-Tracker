import os
import argparse
from datetime import datetime
from task_tracker.database import TaskDatabase
from task_tracker.report import generate_report
from tkinter import Tk, filedialog

import os

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')  # Command to clear screen on Windows
    else:
        os.system('clear')  # Command to clear screen on Unix-based systems


def welcome_art():
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

def welcome_screen():
    print("Please choose an option:")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Show last 7 added tasks")
    print("4. Filter tasks by date")
    print("5. Generate report")
    print("6. Edit an existing task")
    print("7. Show Menu")
    print("8. Exit")

def get_task_details():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    while True:
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    while True:
        deadline = input("Enter the deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    status_options = ["pending", "in-progress", "completed"]
    while True:
        status = input("Enter the status (pending, in-progress, completed): ").lower()
        if status in status_options:
            break
        else:
            print("Invalid status. Please choose from 'pending', 'in-progress', or 'completed'.")
    while True:
        try:
            priority = int(input("Enter the priority (integer): "))
            break
        except ValueError:
            print("Priority must be an integer.")
    while True:
        try:
            payment = float(input("Enter the payment: "))
            break
        except ValueError:
            print("Payment must be a number.")
    return title, description, start_date, deadline, status, priority, payment

def get_edited_task_details(task_details):

    # Unpack task details
    _ , title, description, start_date, deadline, status, priority, payment = task_details

    # Prompt the user for new values, if any
    new_title = input(f"Enter the task title ({title}): ").strip() or title
    new_description = input(f"Enter the task description ({description}): ").strip() or description
    new_start_date = input(f"Enter the start date (YYYY-MM-DD) ({start_date}): ").strip() or start_date
    new_deadline = input(f"Enter the deadline (YYYY-MM-DD) ({deadline}): ").strip() or deadline
    new_status = input(f"Enter the status (pending, in-progress, completed) ({status}): ").strip().lower() or status
    new_priority = input(f"Enter the priority (integer) ({priority}): ").strip() or priority
    new_payment = input(f"Enter the payment ({payment}): ").strip() or payment

    # Validate start_date and deadline
    while True:
        try:
            if new_start_date:
                datetime.strptime(new_start_date, "%Y-%m-%d")
            if new_deadline:
                datetime.strptime(new_deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            new_start_date = input(f"Enter the start date (YYYY-MM-DD) ({start_date}): ").strip() or start_date
            new_deadline = input(f"Enter the deadline (YYYY-MM-DD) ({deadline}): ").strip() or deadline

    # Validate priority
    if new_priority:
        while True:
            try:
                new_priority = int(new_priority)
                break
            except ValueError:
                print("Priority must be an integer.")
                new_priority = input(f"Enter the priority (integer) ({priority}): ").strip() or priority

    # Validate payment
    if new_payment:
        while True:
            try:
                new_payment = float(new_payment)
                break
            except ValueError:
                print("Payment must be a number.")
                new_payment = input(f"Enter the payment ({payment}): ").strip() or payment

    return new_title, new_description, new_start_date, new_deadline, new_status, new_priority, new_payment


def select_directory():
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    return directory

def main():
    db = TaskDatabase('tasks.db')
    welcome_art()
    welcome_screen()
    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            title, description, start_date, deadline, status, priority, payment = get_task_details()
            db.add_task(title, description, start_date, deadline, status, priority, payment)
            temp = input("Press Enter to continue........")

        elif choice == '2':
            tasks = db.get_all_tasks()
            # Define a format string for the header and the tasks
            header = "{:<15} {:<20} {:<40} {:<12} {:<10} {:<15} {:<14} {:<12}"
            task_format = "{:<15} {:<20} {:<40} {:<12} {:<10} {:<15} {:<14} {:<12}"

            # Print the header
            print(header.format("ID","Title", "Description", "Start Date", "Deadline", "Status", "Priority", "Payment"))

            # Print a separator line
            print("="*140)

            # Print each task
            for task in tasks:
                print(task_format.format(*task))  # Unpack the tuple elements

            temp = input("Press Enter to continue........")
        elif choice == '3':
            tasks = db.get_last_n_tasks(7)

            # Define a format string for the header and the tasks
            header = "{:<15} {:<20} {:<40} {:<12} {:<10} {:<15} {:<14} {:<12}"
            task_format = "{:<15} {:<20} {:<40} {:<12} {:<10} {:<15} {:<14} {:<12}"

            # Print the header
            print(header.format("ID","Title", "Description", "Start Date", "Deadline", "Status", "Priority", "Payment"))

            # Print a separator line
            print("="*140)

            # Print each task
            for task in tasks:
                print(task_format.format(*task))  # Unpack the tuple elements

            temp = input("Press Enter to continue........")
        elif choice == '4':
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            tasks = db.filter_tasks_by_date(start_date, end_date)
            for task in tasks:
                print(task)
            temp = input("Press Enter to continue........")
        elif choice == '5':
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            output_file_name = input("Enter the output file name (e.g., report.xlsx): ")
            output_directory = select_directory()
            if output_directory:
                output_path = os.path.join(output_directory, output_file_name)
            else:
                output_path = output_file_name
            tasks = db.filter_tasks_by_date(start_date, end_date)
            generate_report(tasks, output_path)
            print(f"Report generated: {output_path}")
            temp = input("Press Enter to continue........")
        elif choice == '6':
            task_id_input = input("Enter the task ID to edit: ")
            if task_id_input.isdigit():
                task_id = int(task_id_input)
                # Fetch existing task details
                task_details = db.get_task_by_id(task_id)
                if task_details:
                    # Prompt user for updated task details
                    updated_details = get_edited_task_details(task_details)
                    # Update task with new details
                    db.update_task(task_id, *updated_details)
                    print("Task updated successfully.")
                else:
                    print("Task not found.")
            else:
                print("Invalid task ID. Please enter a number.")
            temp = input("Press Enter to continue........")
        elif choice == '7':
            clear_screen()
        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")


