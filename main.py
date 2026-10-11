from tasks import add_task, show_tasks

import os

from dotenv import load_dotenv





name = input("Hello what your name:    ") 
print(f"WELCOME {name}")

load_dotenv()

admin_answer = input("Do you want to enter Admin Mode? (yes/no): ")



if admin_answer.lower() == "yes":
    password = input("Enter admin password: ")

    admin_password = os.getenv("MANAGER_ADMIN_MODE")

    if password == admin_password:
        print("Admin Mode enabled.")
    else:
        print("Wrong password.")



tasks = []
while True:
    task = input("Enter a task (or type 'done' to finish the code):   ")

    if task.lower() == "done":
        break

    priority = input("Enter priority (low/medium/high):  ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    add_task(tasks, task, priority)

    

show_tasks(tasks)

file = open("results.txt", "a")
file.write(f"{name} -  {tasks}")

file.close()
