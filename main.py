import os

from dotenv import load_dotenv

from tasks import load_tasks
from tasks import add_task
from tasks import show_tasks
from tasks import complete_task
from tasks import delete_task


load_dotenv()

name = input("Enter your name: ")

print("Welcome", name)

tasks = load_tasks()

admin_answer = input("Do you want to enter Admin Mode? (yes/no): ")

if admin_answer.lower() == "yes":
    password = input("Enter admin password: ")

    admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

    if password == admin_password:
        print("Admin Mode enabled.")
    else:
        print("Wrong password.")

while True:
    print("\nPersonal Task Manager")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        add_task(tasks, title)
        print("Task added.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)

        number = int(input("Enter task number: "))
        complete_task(tasks, number)

    elif choice == "4":
        show_tasks(tasks)

        number = int(input("Enter task number: "))
        delete_task(tasks, number)

    elif choice == "5":
        print("Goodbye", name)
        break

    else:
        print("Invalid option.")