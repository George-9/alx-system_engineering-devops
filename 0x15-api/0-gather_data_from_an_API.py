#!/usr/bin/python3
"""
    This script gets user name from an api
    shows the completed tasks
"""

import json
from sys import argv
from urllib import request as request

user_request = request.urlopen('https://jsonplaceholder.typicode.com/users')
todos_request = request.urlopen('https://jsonplaceholder.typicode.com/todos')

employeeId = int(argv[1])
employees = json.loads(user_request.read())

"""employee name"""
e = ''
for employee in employees:
    if employee.get('id') == id:
        e = employee.get('name')

count = 0
done = 0
done_list = []

todos = json.loads(todos_request.read())

for todo in todos:
    if (employeeId == todo.get('userId')):
        if (todo.get('completed') is True):
            done_list.append(todo.get('title'))
            done += 1
        count += 1

if __name__ == '__main__':
    print(f'Employee {e} is done with tasks ({done}/{count}):')
    for t in done_list:
        print(f'\t{t}')
