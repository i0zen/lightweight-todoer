import os
import os.path
from os import path

if os.name == "nt":
    clear = lambda: os.system("cls")
elif os.name == "posix":
    clear = lambda: os.system("clear")
else:
    raise SystemError


def info():
    print('''
    1.To list tasks
    2.To append a task
    3.To delete a task
    4.Clear all tasks
    5.Exit''')

def listingtasks():
    with open("todos.txt", "r") as f:
        clear()
        temp = f.read().splitlines()
        for count, line in enumerate(temp, 1):
            print(count, line)
        print("#PRESS ANY KEY TO CONTINUE")

def appendingtasks():
    with open("todos.txt", "a") as f:
        print("Task:")
        appendabletask = str(input())
        f.write("\n" + appendabletask)

def deletingtasks(tasktodel):
    with open("todos.txt", "r") as f:
        lines = f.readlines()
    with open("todos.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != tasktodel:
                f.write(line)

def cleantasks():
    with open("todos.txt", "w")as f:
            print("All tasks are gone")
            input()


def main():
    while True:
        deletingtasks("")
        clear()
        info()
        control = str(input())
        if control == "1":
            listingtasks()
            input()
        elif control == "2":
            appendingtasks()
        elif control == "3":
            ttd = str(input("task you want to delete(full name needed)"))
            deletingtasks(ttd)
        elif control == "4":
            if str(input("Are you sure you want to delete all tasks?[y to continue]")) == "y":
                cleantasks()
        elif control == "5":
            break
        else:
            print("Didn't recognize control function")
        del control

if __name__ == "__main__":
    if path.exists("todos.txt"):
        main()
    else:
        with open("todos.txt", "w")as f:
            print("Created .txt file")
        main()
