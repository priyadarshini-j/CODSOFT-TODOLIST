class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            f.write('\n'.join(self.tasks))

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added.")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{task}' removed.")
        except IndexError:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks.")

def main():
    todo_list = TodoList("todo.txt")

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
            task_index = input("Enter index of task to remove: ")
            todo_list.remove_task(int(task_index) - 1)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
