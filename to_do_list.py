# To do list project.
# User can create his own To-Do list and add, delete, or complete tasks from it. Future updates. Load from file, save to file. and interactive buttons.

tasks = []


def main_menu():
    print('')
    print("==== TODO LIST ====")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display all tasks")
    print("4. Mark a task as completed")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_task():
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task():
    index = int(input("Enter index of task to remove: "))
    if index >= 0 and index < len(tasks):
        task = tasks.pop(index)
        print(f"Task '{task}' removed successfully.")
    else:
        print("Invalid index. Please try again.")

def display_tasks():
    print('')
    print("==== TASKS ====")
    for index, task in enumerate(tasks):
        print(f"{index+1}. {task}")
        

def mark_completed():
    index = int(input("Enter index of task to mark as completed: "))
    if index >= 0 and index < len(tasks):
        tasks[index] = f"[completed] {tasks[index]}"
        print("Task marked as completed.")
    else:
        print("Invalid index. Please try again.")


while True:
    choice = main_menu()
    if choice == '0':
        # Exit the application
        break
    elif choice == '1':
        # Add a task to the list
        add_task()
    elif choice == '2':
        # Remove a task from the list
        remove_task()
    elif choice == '3':
        # Display all tasks in the list
        display_tasks()
        break
    elif choice == '4':
        # Mark a task as completed
        mark_completed()
    else:
        print("Invalid choice. Please try again.")


def exit_menu():
    print ('')
    print('==== ====')
    print ('1. Back to main menu.')
    print ('2. Delete list and restart menu.')
    print ('0. Exit.')
    choice = input('Enter your choice: ')
    return choice

def delete_and_restart():
    global tasks
    tasks = []
    print ('To-do list deleted')
    main_menu()

import sys

while True:
    choice = exit_menu()
    if choice == '0':
        # Exit the application
        sys.exit()
    elif choice == '1':
        # Add a task to the list
        while True:
            choice = main_menu()
            if choice == '0':
                # Exit the application
                break
            elif choice == '1':
                # Add a task to the list
                add_task()
            elif choice == '2':
            # Remove a task from the list
                remove_task()
            elif choice == '3':
            # Display all tasks in the list
                display_tasks()
                break
            elif choice == '4':
            # Mark a task as completed
                mark_completed()
            else:
                print("Invalid choice. Please try again.")
    elif choice == '2':
        # Delete the whole list and restart
        delete_and_restart()
else:
        print("Invalid choice. Please try again.")