myCompany = {
    '32018043' : {
        'id': '32018043',
        'name':'Ahmad Tohamy',
        'job':'Embedded Linux Developer',
        'salary':'10,000'
    },

    '32018122' : {
        'id': '32018122',
        'name':'Abdulrahman',
        'job':'Networking Engineer',
        'salary':'9,000'
    },


    '32018103' : {
        'id': '32018103',
        'name':'Seif',
        'job':'Embedded Software',
        'salary':'19,000'
    }
}

def add (**employee):
    new_employee = {
        'id' : employee['id'],
        'name' : employee['name'],
        'job' : employee['job'],
        'salary': employee['salary']
    }
    myCompany.update( {str(employee['id']) : new_employee } )

def GetThenAdd ():
    print('Please entre the following ')
    id = str(input('Employee ID : '))
    name = str(input("Name : "))
    job = str(input('Job : '))
    salary = str(input('Salary : '))

    new_employee = {
        'id' : str(id),
        'name' : str(name),
        'job' : str(job),
        'salary': str(salary)
    }
    myCompany.update( {str(id) : new_employee } )

def printById():
    id = input("Employee's ID : ")
    print(myCompany.get(str(id)))

def removeById():
    id = input("Employee's ID : ")
    myCompany.pop(str(id))