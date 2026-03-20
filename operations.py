from storage import load_tasks, save_tasks
from colorama import Fore, Style, init

init()


def add_task(task_name, priority="Medium", deadline=None):

    tasks = load_tasks()

    task = {
        "name": task_name,
        "done": False,
        "priority": priority,
        "deadline": deadline
    }

    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + "✔ Task added successfully" + Style.RESET_ALL)


def list_tasks():

    tasks = load_tasks()

    if not tasks:
        print(Fore.YELLOW + "No tasks found" + Style.RESET_ALL)
        return

    print("="*40)
    print(Fore.CYAN + "             Your Tasks" + Style.RESET_ALL)
    print("="*40)

    # Priority order
    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    # Sort tasks
    tasks.sort(key=lambda task: priority_order.get(
        task.get("priority", "Medium"), 2))

    for index, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"

        color = Fore.GREEN if task["done"] else Fore.RED

        # ----Safe Access by using get()----
        priority = task.get("priority", "Medium")
        deadline = task.get("deadline", "No deadline")

        print(color + f"{index+1}. {task["name"]} {status}" + Style.RESET_ALL)
        print(f" priority: {priority} || deadline: {deadline}")
        print("-"*40)


def mark_done(index):
    tasks = load_tasks()

    # Error Handling
    if index < 0 or index >= len(tasks):
        print(Fore.RED + "Invalid task number" + Style.RESET_ALL)
        return

    tasks[index]["done"] = True

    save_tasks(tasks)

    print(Fore.GREEN + "✔ Task marked as done" + Style.RESET_ALL)


def delete_task(index):
    tasks = load_tasks()

    # Error Handling
    if index < 0 or index >= len(tasks):
        print(Fore.RED + "Invalid task number" + Style.RESET_ALL)
        return

    tasks.pop(index)

    save_tasks(tasks)

    print(Fore.GREEN + "✔ Task deleted successfully" + Style.RESET_ALL)


def edit_task(index, new_name):
    tasks = load_tasks()

    if index < 0 or index >= len(tasks):
        print("Invalid task number")
        return

    tasks[index]["name"] = new_name

    save_tasks(tasks)

    print("✔ Task updated successfully")
