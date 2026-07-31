# ToDoList-python
Simple CLI to-do list in Python with file-based persistence (add/delete tasks saved in t.txt).

# To-Do List (File-Based CLI) — Python

A simple command-line to-do list program written in Python. It lets you **add** new tasks and **delete** tasks by line number. Tasks are stored persistently in a text file (`t.txt`).

## Features
- Add a new task to the list
- Delete a task by its line number
- Saves tasks to `t.txt` so they remain after closing the program

## Requirements
- Python 3

## How It Works
The program uses a plain text file (`t.txt`) where each task is saved like this:

```text
1. Buy milk
2. Study Python
3. Workout
