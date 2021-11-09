from lecturer import Lecturer
from student import Student


def get_number(str):
    try:
        num = float(str)
        return num
    except:
        print('Invalid number')
        return None


def check_mark(mark):
    if mark < 0 or mark > 100:
        print('Mark must be between 0 to 100')
        return False
    else:
        return True


nric = input('Enter lecturer NRIC: ')
name = input('Enter lecturer name: ')

while True:
    num_str = input('Enter teaching hour: ')
    teaching_hour = get_number(num_str)
    if teaching_hour is not None:
        break

lecturer = Lecturer(nric, name, teaching_hour)

nric = input('Enter student NRIC: ')
name = input('Enter student name: ')
admin_no = input('Enter admin No: ')

while True:
    num_str = input('Enter test mark: ')
    test_mark = get_number(num_str)
    if test_mark is not None:
        if check_mark(test_mark):
            break

while True:
    num_str = input('Enter exam mark: ')
    exam_mark = get_number(num_str)
    if exam_mark is not None:
        if check_mark(exam_mark):
            break

student = Student(nric, name, admin_no, test_mark, exam_mark)

print(lecturer)
print(student)
