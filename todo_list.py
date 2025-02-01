# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:00:13 2025

@author: Ella
"""

def display_menu():
    print("\n-- To-Do List Menu --")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete Task")
    
def add_task(tasks):
    task = input("Enter a new task: ")
    new_task = {"task": task, "completed": False}
    tasks = tasks + [new_task]
    print("Task added successfully.")
    return tasks

def view_tasks(tasks):
    print("\n--- To-Do List ---")
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        for i in range(len(tasks)):
            task = tasks[i]
            if task["completed"]:
                status = "Completed"
            else:
                status = "Incomplete"
            print(str(i + 1) + ". " + task["task"] + " - " + status)

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    return tasks

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    return tasks


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            tasks = add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
        

if __name__ == "__main__":
    main()