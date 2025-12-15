# Project: Arnav's To Do List

A simple command-line To-Do List app built in Python that lets users add, view, and delete tasks. It uses a list to store tasks and runs in a continuous menu loop until the user exits.

## Features

- Users can input a new task, which is stored in a list.
- Users can see all current tasks, each labeled with a task number.
- Tasks can be removed by entering their corresponding number.

## How it works

- The program stores all tasks in a Python list called tasks.
- When launched, it displays a menu of options (add, delete, list, quit).
- Option 1 calls addTask() to get user input and append it to the list.
- Option 2 calls deleteTask() to remove a specific task (after showing all tasks).
- Option 3 calls listTasks() to print existing tasks.
- Option 4 ends the program loop and prints a goodbye message.
- Input validation ensures errors are caught, such as entering text when a number is expected.

## What I learned

- How to store and manage data in a list.
- Using loops and conditionals for menu-driven programs.

## Future improvements

- Add timestamps.
- Add a status for tasks, wether its completed or not

