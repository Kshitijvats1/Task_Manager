# Task Manager

A simple command-line application to manage tasks. This program allows users to add, edit, delete, and mark tasks as complete. Tasks are stored in a text file for persistence.

## Features

- **Add Task**: Create a new task with a description.
- **Edit Task**: Modify the description of an existing task.
- **Delete Task**: Remove a task from the list.
- **Mark Task Complete**: Mark a task as completed.
- **Show Tasks**: Display all current tasks with their completion status.

## Code Overview

### Classes

- **Task**: Represents a single task with a description and completion status.
    - `__init__(self, description, completed=False)`: Initializes a task with a description and a completion status.
    - `__str__(self)`: Returns a string representation of the task.

- **TaskManager**: Manages a list of tasks and handles task operations.
    - `__init__(self, filename="tasks.txt")`: Initializes the task manager and loads tasks from a file.
    - `add_task(self, description)`: Adds a new task.
    - `edit_task(self, index, new_description)`: Edits an existing task.
    - `delete_task(self, index)`: Deletes a task.
    - `mark_task_complete(self, index)`: Marks a task as complete.
    - `display_tasks(self)`: Displays all tasks.
    - `save_tasks(self)`: Saves tasks to a file.
    - `load_tasks(self)`: Loads tasks from a file.

### Main Functionality

The `main()` function provides a console user interface for interacting with the task manager. Users can choose options to manage their tasks through a simple menu system.

## Requirements

- Python 3.x


