# streaming-02-multiple-processes
## Github link: https://github.com/julia-fangman/streaming-02-multiple-processes 

## Overview
In this project, we'll look at what happens with concurrent processes are accessing a shared resource.  A shared resource could be a SQLite database, a queue (first-in, first-out, like a grocery store line), a deque ("deck") if working with sliding time windows (which we'll do later), an office printer, or more. 

I also:
review how one multiprocessing example behaves when tasks are quick and sharing goes well (generally),
change to using longer-running concurrent tasks and explore what happens,
implement a scaffolded process that streams from a csv file, &
write my own streaming process that reads from a unique csv data source of my choice. 

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)


## Julia's Machine: 
 Welcome to the Python Debugging Information Utility ABOUT.PY
 Date and Time: 2024-05-02 at 10:33 AM
 Operating System: posix Darwin 23.4.0
 System Architecture: 64bit
 Number of CPUs: 4
 Machine Type: x86_64
 Python Version: 3.12.2
 Python Build Date and Compiler: v3.12.2:6abddd9f6a with Feb  6 2024 17:02:06
 Python Implementation: CPython
 Active pip environment: None
 Path to Interpreter:         /usr/local/bin/python3
 Path to virtual environment: /Library/Frameworks/Python.framework/Versions/3.12
 Current Working Directory:   /Users/juliafangman/Documents/streaming-02-multiple-processes
 Path to source directory:    /Users/juliafangman/Documents/streaming-02-multiple-processes/streaming-02-multiple-processes
 Path to script file:         /Users/juliafangman/Documents/streaming-02-multiple-processes/streaming-02-multiple-processes/about.py
 User's Home Directory:       /Users/juliafangman
 Terminal Environment:        VS Code
 Terminal Type:               zsh
 Git available in PATH:       True 


## Task 1. Fork 

Fork this repository ("repo") into **your** GitHub account. 

## Task 2. Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. 

## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information.

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

In general, we're successful and six new records get inserted. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: TODO.
Run the script again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with errors. 

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.


### Select All, Copy, Paste

On a Mac the select all, copy, paste hotkeys are:

- Command a
- Command c
- Command v


### Reading Error Messages

Python has pretty helpful error messages. 
When you get an error, read them carefully. 

- What error do you get?

### Database Is Locked Error

Do a web search on the sqlite3 'database is locked' error.

- What do you learn?
- Once a process fails, it crashes the main process and everything stops. 

### Deadlock

Deadlock is a special kind of locking issue where a process 
is waiting on a resource or process, that is waiting also. 

Rather than crashing, a system in deadlock may wait indefinitely, 
with no process able to move forward and make progress.

### Learn More

Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 
