# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program.
# Do NOT use Google. Do NOT use other students. Try to do this on your own.

# Congratulations! You're running [YOUR NAME]'s Task List program.

# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program

# class Task:
#     def __init__(self, task):

userName = input("Enter your name: ")
print(f"Congratulations! You are running {userName}'s Task List program.")

class Task:
    def __init__(self, task):
        self.task = task

    def allTasks(self):
        print(f"{self.task}")

newTask1 = Task("1. Wash Car")
newTask2 = Task("2. Clean Floors")
newTask3 = Task("3. Walk Dogs")

def main():
    userInput = print("What would you like to do next? ")
    while userInput != 0:
        userInput = int(input("1. List all tasks.\n"
                              "2. Add a task to the list.\n"
                              "3. Delete a task.\n"
                              "0. To quit the program\n"))
        if userInput == 1:
            newTask1.allTasks()
        elif userInput == 2:
            print("Add a task to the list")
        elif userInput == 3:
            print("Delete a task")
main()
