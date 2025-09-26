'''
A buggy Task Manager that provides an opportunity to debug code by both reasoning about it and stepping through
The program has a number of bugs that are introduced one at a time.
The goal is to find and fix the bugs.
Ensure you step through this program in pdb only to understand how the program works and to find the bugs.
'''

# Once debugged add some documentation examples to help the next programmer!
import sys
import pdb
import random
import string
# import os

def add_task(tasks, task):
    # pdb.set_trace()
    tasks.append((task, False))

def mark_task_completed(tasks, index):
    # breakpoint()
    if 0 <= index < len(tasks):
        tasks[index] = True
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.remove(tasks[index])
    else:
        print("Invalid task index.")

def list_tasks(tasks):
    # pdb.set_trace()
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        print(f"{index}. {'[X]' if task[1] else '[ ]'} {task[0]}")

def sort_tasks(tasks):
    # pdb.set_trace()
    tasks.sort(key=lambda task: task[0])

def binary_search(tasks, target):
    # pdb.set_trace()
    # sort_tasks(tasks)
    time = 0
    low, high = 0, len(tasks) - 1
    while low <= high:
        mid = (low + high)
        if tasks[mid][0] == target:
            print(time)
            return mid
        elif tasks[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
        time += 1
    print(time)
    return -1

def generate_tasks(n=1000000):
    tasks = []
    for _ in range(n):
        # Generate a random string of length between 5 and 15, with lowercase letters
        name_length = random.randint(5, 15)
        name = ''.join(random.choices(string.ascii_lowercase, k=name_length))
        tasks.append((name, False))
    return tasks

def main():
    # pdb.set_trace()
    tasks = []

    tasks = generate_tasks(10_000_000)

    tasks.append(("aaaaaa", False))
    tasks.append(("mmmmmm", False))
    tasks.append(("zzzzzz", False))

    print("Starting sort")
    sort_tasks(tasks)
    print("Finished sorting")

    while True:
        print("\n1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Sort Tasks")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == "2":
            pdb.set_trace()
            index = int(input("Enter task index to mark as completed: "))
            mark_task_completed(tasks, index)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete_task(tasks, index)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            sort_tasks(tasks)
            print("Tasks sorted.")
        elif choice == "6":
            target = input("Enter task description to search: ")
            index = binary_search(tasks, target)
            if index != -1:
                print(f"Task '{target}' found at index {index}.")
            else:
                print(f"Task '{target}' not found.")
        elif choice == "7":
            sys.exit("Exiting program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
