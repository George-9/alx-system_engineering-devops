#!/usr/bin/python3

"""
    This script gets user name from an api
    shows the completed tasks
"""

from sys import argv
import json
import urllib.request as request

user_request = request.urlopen('https://jsonplaceholder.typicode.com/users')
todos_request = request.urlopen('https://jsonplaceholder.typicode.com/todos')


def getEmployeeName(employees=[], id=0):
    """gets the given employer name by id

       Args:
        employees: The list of employees
        id: The employee's id

       Returns:
         employee's name(str)

       Raises:
         no error
    """
    employeeName = ''
    for employee in employees:
        if employee.get('id') == id:
            employeeName = employee.get('name')
    return employeeName


def getCompletedTodos(todos=[], id=0):
    """gets the tasks' info of the employee
       Args:
        todos: list of employees
        id: The employee's id

       Returns:
         number of taks(int),
         number of completed tasks(int),
         list of the completed tasks

       Raises:
         no error
    """
    count = 0
    done = 0
    done_list = []
    for todo in todos:
        if (todo.get('userId') == id):
            if (todo.get('completed') is True):
                done_list.append(todo.get('title'))
                done += 1
            count += 1
    return count, done, done_list


employees = json.loads(user_request.read())
todos = json.loads(todos_request.read())

employeeId = int(argv[1])

"""employee name"""
e = getEmployeeName(employees, employeeId)
totalTasks, totalDone, completedList = getCompletedTodos(todos, employeeId)

print(f'Employee {e} is done with tasks ({totalDone}/{totalTasks}):')
for t in completedList:
    print(f'\t{t}')
