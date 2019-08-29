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
            print("blank")
        elif userInput == 2:
            taskInput = input("Enter a new task ")
            # taskInput = str(task_array) + taskInput
            print(str(task_array) + str(taskInput))
            print("Success task added ")
        elif userInput == 3:
            print("DeleteTask")
main()
