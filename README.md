# 📝 Advanced CLI To-Do Manager (Python)

A professional command-line To-Do manager built using Python with clean architecture, modular design, and real-world features.

---

## 🚀 Features

- ✅ Add tasks with priority & deadline
- 📋 List tasks (sorted by priority)
- ✔ Mark tasks as completed
- 🗑 Delete tasks
- ✏ Edit tasks
- 🎨 Colored CLI output
- 💾 Persistent storage using JSON
- 🧠 Input validation & error handling
- 🧱 Modular code structure

---

## 🛠 Tech Stack

- Python
- JSON (data storage)
- Colorama (CLI styling)

---

## 📦 Installation

```bash
git clone <your-repo-link>
cd todo-cli
pip install colorama
```

---

## ▶️ Usage

### Add task

```bash
python todo.py add "Learn FastAPI" High 2026-04-01
```

### List tasks

```bash
python todo.py list
```

### Mark task as done

```bash
python todo.py done 1
```

### Delete task

```bash
python todo.py delete 1
```

### Edit task

```bash
python todo.py edit 1 "Master Python"
```

### Help

```bash
python todo.py help
```

---

## 📂 Project Structure

```
todo-cli/
│
├── todo.py          # CLI entry point
├── operations.py    # business logic
├── storage.py       # data handling
└── tasks.json       # local storage
```

---

## 🧠 Key Learnings

- CLI application development
- Modular Python architecture
- File handling & JSON storage
- Input validation & error handling
- Clean code practices

---

## 🔮 Future Improvements

- Task deadlines reminders
- Search & filter tasks
- GUI version
- Web app (FastAPI backend)

---

⭐ If you like this project, give it a star!
