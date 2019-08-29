task_array = ["Clean house", "wash dog", "clean car"]

def main():
    userInput = print("What would you like to do next? ")
    taskInput = ''
    while userInput != 0:
        userInput = int(input("1. List all tasks.\n"
                              "2. Add a task to the list.\n"
                              "3. Delete a task.\n"
                              "0. To quit the program\n"))
        if userInput == 1:
            for arrayT in task_array:
                print(arrayT)
        elif userInput == 2:
            taskInput = input("Enter a new task ")
            task_array.append(taskInput)
            print("Success task added ")
        elif userInput == 3:
            taskInput = input("Enter a task to delete ")
            task_array.remove(taskInput)
            print("Task Deleted")
main()


# To list all items in an array:
# ```python
# for itemInArray in arrayOfTasks:
# ```
# To add an item to an array
# ```python
# arrayOfTasks.append(newTask)
# ```
# To check if an item is in an array
# ```python
# if deleteTask in arrayOfTasks:
# ```
# To delete a task
# ```python
# arrayOfTasks.remove(deleteTask)
