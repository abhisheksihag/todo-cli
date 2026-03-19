import sys
from operations import add_task, list_tasks, mark_done, delete_task

# ----CLI Logic----

# ----Validation----
if len(sys.argv) < 2:
    print("Please provide a Command: add / list / done / delete")
    sys.exit()

command = sys.argv[1]

valid_commands = ["add", "list", "done", "delete", "help"]

if command not in valid_commands:
    print("Invalid Command")
    sys.exit()

    # ----Command Handling----

if command == "add":
    if len(sys.argv) < 3:
        print("Please provide a task name")
        sys.exit()

    task_name = sys.argv[2]
    add_task(task_name)

elif command == "list":
    list_tasks()

elif command == "done":
    if len(sys.argv) < 3:
        print("Please provide task number")
        sys.exit()

    index = int(sys.argv[2]) - 1
    mark_done(index)

elif command == "delete":
    if len(sys.argv) < 3:
        print("Please provide task number")
        sys.exit()

    index = int(sys.argv[2]) - 1
    delete_task(index)

elif command == "help":
    print("""
    Available commands:
          
    python3 todo.py add "task name"
    python3 todo.py list
    python3 todo.py done <task number>
    python3 todo.py delete <task number>
    python3 todo.py help                                        
    """)
