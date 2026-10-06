from tasks import add_task, show_tasks

name = input("Enter your name: ")

print("Welcome", name)

tasks = []

task1 = input("Enter your first task: ")
add_task(tasks, task1)

task2 = input("Enter your second task: ")
add_task(tasks, task2)

task3 = input("Enter your third task: ")
add_task(tasks, task3)

show_tasks(tasks)