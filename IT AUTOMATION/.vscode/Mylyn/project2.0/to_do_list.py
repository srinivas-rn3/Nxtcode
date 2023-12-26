import os
path_file = r"C:\Users\srini\OneDrive\Documents\to-do-list.txt"
path_file1 = r"C:\Users\srini\OneDrive\Documents\completed.txt"

def display_menu():
    print("1.View To-Do List")
    print("2.Add Task")
    print("3.Mark task as Completed")
    print("4.Exit")

def view_todo_list():
    if os.path.exists(path_file):
        with open(path_file,"r") as file:
            tasks = file.readlines()
            if tasks:
                print("To-Do-List:")
                for index,task in  enumerate(tasks,start=1):
                    print("\n")
                    print(f"{index}.{task.strip()}",end="\n")
                    print("\n")
            else:
                print("To-Do-List is empty!!")
    else:
        print("To Do list does not exit.Create new one")

def add_task():
    task = input("Enter the task: ")
    with open(path_file,"a") as file:
        file.write(task +"\n")
    print("Task added successfully")

def mark_completed():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open(path_file,'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number -1)
            with open(path_file,'w') as file:
                file.writelines(tasks)
            with open(path_file1,"a") as file:
                file.write(completed_task)
            print("Task marked as completed")
        else:
            print("Invalid  task number!!!")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice  == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting the to-do-list application.GoodBye!!")
            break
        else:
            print("Invaid  choice.please enter a number between  1 and 4.")
if __name__ == "__main__":
    main()
    
        