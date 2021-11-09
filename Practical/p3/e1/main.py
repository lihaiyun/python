from employee import Employee
from student import Student

employee_list = []
student_list = []

while True:
    nric = input('Enter NRIC: ')
    name = input('Enter Name: ')
    type = input('Student or Employee? (S or E): ')
    if type.upper() == 'S':
        gpa = float(input('Enter GPA: '))
        student = Student(nric, name, gpa)
        student_list.append(student)
    elif type.upper() == 'E':
        salary = float(input('Enter salary: '))
        employee = Employee(nric, name, salary)
        employee_list.append(employee)
    command = input('Do you want to continue? (Y or N): ')
    if command.upper() == 'N':
        break

print("========== Student ==========")
for student in student_list:
    print(student)
print("========== Employee ==========")
for employee in employee_list:
    print(employee)
