def main():
    # Store tasks as dictionaries containing text and completion status
    tasks = []

    print("--- PYTHON TO-DO LIST ---")

    while True:
        #Task Options
        print("\nMain Options:")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Mark Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        #View tasks
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, start=1):
                    status = "✓" if task["completed"] else " "
                    print(f"{index}. [{status}] {task['text']}")

        #Add a new task
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append({"text": new_task, "completed": False})
                print(f"Added task: '{new_task}'")
            else:
                print("Task description cannot be empty!")

        #Mark a task as complete
        elif choice == "3":
            if not tasks:
                print("\nNo tasks available to complete.")
                continue
                
            try:
                task_num = int(input("Enter the task number to complete: "))
                if 1 <= task_num <= len(tasks):
                    task = tasks[task_num - 1]
                    if task["completed"]:
                        print(f"'{task['text']}' is already completed.")
                    else:
                        task["completed"] = True
                        print(f"✓ '{task['text']}' marked as complete.")  
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        #Delete a task
        elif choice == "4":
            if not tasks:
                print("\nNo tasks available to delete.")
                continue

            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"✗ '{removed_task['text']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        #Exit program
        elif choice == "5":
            print("\nGoodbye! Have a productive day!")
            break

        #Invalid menu entries
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()