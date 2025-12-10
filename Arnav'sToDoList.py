tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)  # Fixed
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
        

def deleteTask():
    listTasks()  # Fixed
    try:
        taskToDelete = int(input("Enter the number to delete: "))
        if 0 <= taskToDelete < len(tasks):  # Cleaner range check
            removed = tasks.pop(taskToDelete)
            print(f"Task '{removed}' has been removed")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input - enter a number.")


if __name__ == "__main__":

    print("Welcome to Arnav's To Do List App 🙂: ")
    while True:
        print("\n")
        print("Please select one of these options")
        print("\n")
        print("----------------------------------")
        print("1) Add a new task 👀 ")
        print("2) Delete a task ❌ ")
        print("3) List tasks 📙 ")
        print("4) Quit 👋")


        choice = int(input("Enter your choice: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            deleteTask()
        elif choice == 3:
            listTasks()
        elif choice == 4:
            break
        else:
            print("invalid input. Please try again")
            
    print("Goodbye 👋👋")

