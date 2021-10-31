class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = []
        self.allocation = None

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4


def main():
    school_dict = {'SchoolA': 5, 'SchoolB': 5, 'SchoolC': 5}

    students = load_result()
    students.sort(key=by_score, reverse=True)

    for s in students:
        s.choices = ['SchoolA', 'SchoolB', 'SchoolC']

    for s in students:
        for c in s.choices:
            if school_dict[c] > 0:
                s.allocation = c
                school_dict[c] -= 1
                break

    for s in students:
        print(f'{s.name} scores {s.get_score():.2f}, allocated {s.allocation}')


def by_score(student):
    return student.get_score()


def load_result():
    students = []

    # implement the load result logic here
    try:
        file = open('results.txt', 'r')
        lines = file.readlines()
        for line in lines:
            values = line.split(',')
            name = values[0].strip()
            math = float(values[1].strip())
            chinese = float(values[2].strip())
            english = float(values[3].strip())
            science = float(values[4].strip())

            s = Student(name)
            s.math = math
            s.chinese = chinese
            s.english = english
            s.science = science
            students.append(s)
        file.close()
    except IOError:
        print('Error when open file')
    except:
        print('Error when process file data')

    return students


# start the test program
main()
