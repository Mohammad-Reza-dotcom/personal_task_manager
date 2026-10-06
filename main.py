name = input("Enter your name: ")

print("Welcome", name)

tasks = []

task1 = input("Enter your first task: ")
tasks.append(task1)

task2 = input("Enter your second task: ")
tasks.append(task2)

task3 = input("Enter your third task: ")
tasks.append(task3)

print("Your Tasks:")

print("1.", tasks[0])
print("2.", tasks[1])
print("3.", tasks[2])