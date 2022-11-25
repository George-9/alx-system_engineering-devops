#!/usr/bin/python3

# This script gets user name from an api
# shows the completed tasks

from sys import argv
import json
import urllib.request as request

user_request = request.urlopen('https://jsonplaceholder.typicode.com/users')
todos_request = request.urlopen('https://jsonplaceholder.typicode.com/todos')

def getEmployeeName(employees = [], id = 0):
    employeeName = ''
    for employee in employees:
        if employee.get('id') == id:
            employeeName = employee.get('name')
    return employeeName

def getCompletedTodos(todos = [], id = 0):
    count = 0
    done = 0
    done_list = []
    for todo in todos:
        if (todo.get('userId') == id):
            if (todo.get('completed') == True):
                done_list.append(todo.get('title'))
                done += 1
            count += 1
    return count, done, done_list;

employees = json.loads(user_request.read())
todos = json.loads(todos_request.read())

employeeId = int(argv[1])

employeeName = getEmployeeName(employees, employeeId)
totalTasks, totalDone, completedList = getCompletedTodos(todos, employeeId)

print(f'Employee {employeeName} is done with tasks ({totalDone}/{totalTasks}):')
for t in completedList:
    print(f'\t{t}')
