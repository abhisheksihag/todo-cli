import json

# ----File Handling----

# JSON to Python data


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []

# Python to JSON data


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
