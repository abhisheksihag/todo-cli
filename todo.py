import sys
from operations import add_task, list_tasks, mark_done, delete_task, edit_task

# ----CLI Logic----

# ----Validation----
if len(sys.argv) < 2:
    print("Please provide a Command: add / list / done / delete")
    sys.exit()

command = sys.argv[1]

valid_commands = ["add", "list", "done", "delete", "help", "edit"]

if command not in valid_commands:
    print("Invalid Command")
    sys.exit()

    # ----Command Handling----

if command == "add":
    if len(sys.argv) < 3:
        print("Please provide a task name")
        sys.exit()

    task_name = sys.argv[2]

    priority = sys.argv[3] if len(sys.argv) > 3 else "Medium"
    deadline = sys.argv[4] if len(sys.argv) > 4 else None
    add_task(task_name, priority, deadline)

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

elif command == "edit":
    if len(sys.argv) < 4:
        print("Usage: python3 todo.py edit <task_number> <new_name>")
        sys.exit()
    index = int(sys.argv[2]) - 1
    new_name = sys.argv[3]

    edit_task(index, new_name)

elif command == "help":
    print("""
    📌 Available Commands:

➤ Add task:
   python todo.py add "task" [priority] [deadline]

➤ List tasks:
   python todo.py list

➤ Mark done:
   python todo.py done <task_number>

➤ Delete task:
   python todo.py delete <task_number>

➤ Edit task:
   python todo.py edit <task_number> "new name"

📌 Priority:
   High / Medium / Low

📌 Example:
   python todo.py add "Learn FastAPI" High 2026-04-01                                      
    """)
