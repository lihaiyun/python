from lecturer import Lecturer
from student import Student

nric = input('Enter lecturer NRIC: ')
name = input('Enter lecturer name: ')
staff_id = input('Enter staff Id: ')
teaching_hour = float(input('Enter teaching hour: '))
lecturer = Lecturer(nric, name, staff_id, teaching_hour)

nric = input('Enter student NRIC: ')
name = input('Enter student name: ')
admin_no = input('Enter admin No: ')
test_mark = float(input('Enter test mark: '))
exam_mark = float(input('Enter exam mark: '))
student = Student(nric, name, admin_no, test_mark, exam_mark)

print(lecturer)
print(student)
