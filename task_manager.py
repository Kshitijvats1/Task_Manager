import os

# Task class to represent a single task
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description}"

# TaskManager class to handle tasks
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    description, completed = line.strip().split(",")
                    self.tasks.append(Task(description, completed == "True"))

# Console UI for TaskManager
def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Show Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            manager.display_tasks()
            index = int(input("Enter task number to edit: ")) - 1
            new_description = input("Enter new description: ")
            manager.edit_task(index, new_description)
        elif choice == "3":
            manager.display_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)
        elif choice == "4":
            manager.display_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            manager.mark_task_complete(index)
        elif choice == "5":
            manager.display_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
