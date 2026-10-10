import json
import os


def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)

    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, title, priority):
    task = {
        "title": title,
        "status": "pending",
        "priority": priority
    }

    tasks.append(task)
    save_tasks(tasks)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")

        for i in range(len(tasks)):
            priority = tasks[i].get("priority", "Medium")

            print(
                i + 1,
                "-",
                tasks[i]["title"],
                "-",
                tasks[i]["status"],
                "- Priority:",
                priority
            )


def complete_task(tasks, number):
    if number >= 1 and number <= len(tasks):
        tasks[number - 1]["status"] = "done"
        save_tasks(tasks)
        print("Task completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks, number):
    if number >= 1 and number <= len(tasks):
        tasks.pop(number - 1)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")