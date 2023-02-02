'''
Session 4
Task 1:
    Write a python code that manage a database for employees.
    Each employee has a unique ID and has the following data:
    Name, Job and Salary. The system shall allow:
        1-Add new employee
        2-Print employee data
        3-remove employee from the system
'''

import mylib.employee as employee

def printAvailableOperations():
    print("1) add \n2) print\n3) remove")


while True:
    printAvailableOperations()
    operation = str(input('Choose an operation : '))
    print(end="\n")
    if operation.lower().strip() == 'add' or operation.lower().strip() == '1':
        employee.GetThenAdd()
    elif operation.lower().strip() == 'print' or operation.lower().strip() == '2':
        employee.printById()
    elif operation.lower().strip() == 'remove' or operation.lower().strip() == '3':
        employee.removeById()
    else:
        break

print(end="\n")
print(employee.myCompany)