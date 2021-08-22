# This project is made for practicing and gaining experience with Python basics and Python OOP
# The Project is an IT Company that has different types of employees and projects
# The goal of this project is to make something simple but effective project
# This Project is designed as resume Project
# With this Project I want to try some basic Python stuff, loops, conditions,
# playing with functions, basic OOP concepts, Inheritance, Polymorphism.
# Maybe this Project is missing destructors and when I delete Teams, Employees, Projects
# They need to be also destructed with a destructor so the memory can be freed
# Maybe this Project can be upgraded or better optimised but I'm satisfied
import random

class Project:

    def __init__(self, name, pfield, grade):
        self.name = name
        self.pfield = pfield
        self.grade = grade

    def get_name(self):
        return self.name

    def get_pfield(self):
        return self.pfield

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_pfield(self, pfield):
        self.pfield = pfield

    def set_grade(self, grade):
        self.grade = grade

    def printProject(self):
        print('| Name of the Project: ' + self.get_name() + ' || Field of the Project: ' + self.get_pfield() + ' |')

class Employee:

    def __init__(self, name, address, pin, dateworking, title, salary):
        self.name = name
        self.address = address
        self.pin = pin
        self.dateworking = dateworking
        self.title = title
        self.salary = salary

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_pin(self):
        return self.pin

    def get_dateworking(self):
        return self.dateworking

    def get_title(self):
        return self.title

    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_pin(self, pin):
        self.pin = pin

    def set_dateworking(self, dateworking):
        self.dateworking = dateworking

    def set_title(self, title):
        self.title = title

    def set_salary(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return int(self.salary * 1.2)

    def printEmployee(self):
        print('| Name of the Employee: ' + self.get_name() + ' || Title of the Employee: ' + self.get_title() + ' |')

class Secretary(Employee):

    def __init__(self, name, address, pin, dateworking, title, salary, bonus):
        super(Secretary, self).__init__(name, address, pin, dateworking, title, salary)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, bonus):
        self.bonus = bonus

    def calculate_pay(self):
        return int(self.salary * 1.2 + self.bonus)

class Technician(Employee):

    def __init__(self, name, address, pin, dateworking, title, salary, area):
        super(Technician, self).__init__(name, address, pin, dateworking, title, salary)
        self.area = area

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def calculate_pay(self):
        return int(self.salary * 1.5)

class Engineer(Employee):

    def __init__(self, name, address, pin, dateworking, title, salary, type):
        super(Engineer, self).__init__(name, address, pin, dateworking, title, salary)
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def calculate_pay(self):
        return int(self.salary * 1.7)

class Manager(Employee):

    def __init__(self, name, address, pin, dateworking, title, salary):
        super(Manager, self).__init__(name, address, pin, dateworking, title, salary)

    def calculate_pay(self):
        return int(self.salary * 1.8)

class Engineer_Menager(Engineer, Manager):

    def __init__(self, name, address, pin, dateworking, title, salary, type):
        super(Engineer_Menager, self).__init__(name, address, pin, dateworking, title,  salary, type)

    def calculate_pay(self):
        return int(self.salary * 1.7 + self.salary * 1.8)

#Sum of all salaries in a Team
def teamPay(team):
    s = 0
    for m in team[0]:
       s = s + m.calculate_pay()
    return s

#Sum of all salaries in a Company
def comPay(com):
    s = 0
    for t in com:
        s = s + teamPay(t)
    print('The sum of all salaries is {}'.format(s))

#It adds project to the team(used in makeTeam)
def addProject():

    print("Enter the information of the Project: ")
    p = Project(input('Name of the Project: '), input('Field of the Project: '), float(input('Grade of the Project: ')))
    return p

#It adds project to a specific team in a Company
def addProjectTeam(com,posT):
    t=com[posT]
    t[1].append(addProject())
    print('Project added !')

#It adds employee to the team(used in makeTeam)
def addEmployee():

    i = input('What kind of Employee does your team need ? (S for Secretary, T for Technician, E for Engineer, M for Manager) ').upper()
    if i == 'S':
        print("Enter the information of team's Secretary: ")
        s = Secretary(input('Name: '), input('Address: '), random.randint(100000, 999999),
                      input('Date of Employment: '),
                      'Secretary', int(input('Salary: ')), random.uniform(1000, 2000))
        return s

    elif i == 'T':
        print("Enter the information of team's Technician: ")
        t = Technician(input('Name: '), input('Address: '), random.randint(100000, 999999),
                       input('Date of Employment: '),
                       'Technician', int(input('Salary: ')), input('Area: '))
        return t

    elif i == 'E':
        print("Enter the information of team's Engineer: ")
        e = Engineer(input('Name: '), input('Address: '), random.randint(100000, 999999),
                      input('Date of Employment: '),
                      'Engineer', int(input('Salary: ')), input('Type: '))
        return e

    elif i == 'M':
        print("What kind of Manager the team has: (M for normal Manager or E for Engineer Manager) ")
        if (input().upper() == 'M'):
            m = Manager(input('Name: '), input('Address: '), random.randint(100000, 999999),
                        input('Date of Employment: '),
                        'Manager', int(input('Salary: ')))
            return m
        elif (input().upper() == 'E'):
            m = Engineer_Menager(input('Name: '), input('Address: '), random.randint(100000, 999999),
                                 input('Date of Employment: '),
                                 'Manager', int(input('Salary: ')), 'Senior')
            return m
        else:
            print("You entered a wrong letter !!!")
            exit()
    else:
        print('You entered a wrong letter !!!')
        exit()

#It adds employee to a specific team in a Company
def addEmployeeTeam(com, posT):
    t=com[posT]
    t[0].append(addEmployee())
    print('Employee added !')

#It makes a Team
def makeTeam():

    team = []
    mem = []
    proj = []

    n_mem=int(input('How many members has your team: '))
    n_proj=int(input('How many project has your team: '))

    i = 0
    while i < n_mem:
        m=addEmployee()
        mem.append(m)
        i+=1

    j = 0
    while j < n_proj:
        p = addProject()
        proj.append(p)
        j+=1

    team.append(mem)
    team.append(proj)

    return team

#It adds a Team to a Company
def addTeam(com):
    com.append(makeTeam())
    print('Team added !')

#It shows the Team
def printTeam(team):
    for m in team[0]:
        print('Employee: ')
        m.printEmployee()
    for p in team[1]:
        print('Project: ')
        p.printProject()

#It creates a company
def makeCompany():
    comp = []
    n = int(input('Enter how many teams has your company: '))
    i = 0
    while i < n:
        t = makeTeam()
        comp.append(t)
        i+=1
    return comp

#It prints the Company
def printCompany(comp):
    i=1
    for c in comp:
        print('Team number: {}'.format(i))
        printTeam(c)
        i+=1

#It deletes the Company
def deleteCompany(comp):
    comp.clear()
    print('Company is deleted !')

#It deletes a Team in a Company
def deleteTeam(comp,pos):
    comp.pop(pos)
    print('Team deleted !')

#It deletes project from a team(with given position)
def deleteProject(comp, posT, posP):
    t=comp[posT]
    t[1].pop(posP)
    print('Project deleted !')

#It deletes a Employee from a team(with given position)
def deleteEmployee(comp, posT, posE):
    t=comp[posT]
    t[0].pop(posE)
    print('Employee deleted !')

print('Welcome to the IT Company System !!!')
print()
print('If you want to create a Company, write COMPANY !')
print('If you want to add a Team to a Company, write ATEAM !')
print('If you want to add an Employee to a Team, write AEMPLOYEE !')
print('If you want to add a Project to a Team, write APROJECT !')
print('If you want to delete a Company, write DCOMPANY !')
print('If you want to delete a Team from a Company, write DTEAM !')
print('If you want to delete an Employee from a Team, write DEMPLOYEE')
print('If you want to delete a Project from a Team, write DPROJECT !')
print('If you want to calculate the sum of all salaries the Company gets, write PAY !')
print('If you want to exit the System, write EXIT')
print()

while True:

    i=input().upper()
    comp=[]
    if i == 'COMPANY':
        comp = makeCompany()
        printCompany(comp)
        print()
    elif i == 'ATEAM':
        addTeam(comp)
        printCompany(comp)
        print()
    elif i == 'AEMPLOYEE':
        if len(comp):
            n = int(input('Enter the position of the Team to which you want to add an Employee within the Company: '))
            addEmployeeTeam(comp, n)
            printCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'APROJECT':
        if len(comp):
            n=int(input('Enter the position of the Team to which you want to add a Project within the Company: '))
            addProjectTeam(comp, n)
            printCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'DCOMPANY':
        if len(comp):
            deleteCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'DTEAM':
        if len(comp):
            n = int(input('Enter the position of the Team which you want to delete within the Company: '))
            deleteTeam(comp, n)
            printCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'DEMPLOYEE':
        if len(comp):
            n=int(input('Enter the position of the Team to which you want to delete an Employee within the Company: '))
            m=int(input('Enter the position of the Employee which you want to delete within the Team: '))
            deleteEmployee(comp, n, m)
            printCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'DPROJECT':
        if len(comp):
            n = int(input('Enter the position of the Team to which you want to delete a Project within the Company: '))
            m = int(input('Enter the position of the Project which you want to delete within the Team: '))
            deleteProject(comp, n, m)
            printCompany(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'PAY':
        if len(comp):
            comPay(comp)
            print()
        else:
            print('Your company is not created !')
    elif i == 'EXIT':
        exit()