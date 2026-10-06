def add_task(tasks, title):
    task = {
        "title": title,
        "status": "pending"
    }

    tasks.append(task)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Your Tasks:")

        for i in range(len(tasks)):
            print(
                i + 1,
                "-",
                tasks[i]["title"],
                "-",
                tasks[i]["status"]
            )